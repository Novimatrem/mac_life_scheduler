import os
import time
import re
import subprocess
import sys
from datetime import datetime


LOG_PATH = os.path.expanduser(
    "~/Library/CloudStorage/Dropbox/96 Just Monika/zoey"
    "/AppData/Roaming/itch/apps/ddlc/DDLC-1.1.1-pc/log/aff_log.log"
)

POLL_INTERVAL = 0.5
SOUND = "Ping"           # None to mute; try "Glass", "Hero", "Submarine"

# Matches:  ...| X -> Y | before -> after
LINE_RE = re.compile(
    r".*\|\s*[\d\.]+\s*->\s*[\d\.]+\s*\|\s*"
    r"(?P<before>[\d\.]+)\s*->\s*(?P<after>[\d\.]+)"
)


# ---------- logging ----------

def ts():
    return datetime.now().strftime("%H:%M:%S.%f")[:-3]


def log(msg, level="info"):
    tag = {
        "info": "INFO ", "poll": "POLL ", "file": "FILE ",
        "line": "LINE ", "notif": "NOTIF", "warn": "WARN ",
        "err": "ERR  ",
    }.get(level, "INFO ")
    print(f"[{ts()}] {tag} {msg}", flush=True)


def shorten(s, n=140):
    s = s.rstrip("\n")
    return s if len(s) <= n else s[:n] + "…"


# ---------- notifications ----------

def _escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def notify(title, message):
    t, m = _escape(title), _escape(message)
    sound = f' sound name "{SOUND}"' if SOUND else ""
    script = f'display notification "{m}" with title "{t}"{sound}'
    try:
        r = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True, text=True, timeout=5,
        )
        if r.returncode != 0:
            log(f'osascript rc={r.returncode} stderr={r.stderr.strip()!r}',
                "err")
        else:
            log(f'NOTIFIED  "{title}"  —  {message}', "notif")
    except Exception as e:
        log(f'notify exception: {e!r}', "err")


# ---------- parsing ----------

def parse(line):
    """Return (before, after) floats if the line looks like an affection line."""
    if "->" not in line or "|" not in line:
        return None
    m = LINE_RE.match(line)
    if not m:
        return None
    return float(m.group("before")), float(m.group("after"))


# ---------- file IO ----------

def stat_file():
    try:
        st = os.stat(LOG_PATH)
        return st.st_size, st.st_mtime
    except FileNotFoundError:
        return None


def read_lines():
    try:
        with open(LOG_PATH, "r", encoding="utf-8", errors="ignore") as f:
            return f.readlines()
    except FileNotFoundError:
        return None


# ---------- event handling ----------

def handle_line(line, current_total, anchor_line):
    """
    Given a new line, update tracking and fire a notification if the
    affection level changed. Returns the (possibly new) current_total.
    """
    p = parse(line)
    if p is None:
        log(f"  (not an affection line, skipped) {shorten(line)}", "line")
        return current_total

    before, after = p
    is_freeze = "!FREEZE!" in line

    log(
        f"  parsed: before={before:.2f} after={after:.2f} "
        f"freeze={is_freeze}  current_tracked={current_total}",
        "line",
    )

    # FREEZE is always its own event.
    if is_freeze:
        notify(
            "Monika Affection  ❄ FREEZE",
            f"Daily cap reached — total {after:.2f}",
        )
        return after

    # First-ever value.
    if current_total is None:
        notify("Monika Affection", f"Total {after:.2f}")
        return after

    # No actual change in the tracked total — do nothing.
    if after == current_total:
        log(f"  no change (after == current_tracked), no notification", "line")
        return current_total

    # Change! Direction determined by comparison to last known total.
    if after > current_total:
        notify(
            "Monika Affection  ↑ UP",
            f"Now {after:.2f}   (was {current_total:.2f})",
        )
    else:
        notify(
            "Monika Affection  ↓ DOWN",
            f"Now {after:.2f}   (was {current_total:.2f})",
        )
    return after


# ---------- main loop ----------

def watch():
    log(f"Watching: {LOG_PATH}")
    log(f"Poll interval {POLL_INTERVAL}s   Sound {SOUND!r}")

    current_total = None     # last affection level we've reported
    anchor_line = None       # last line we've processed
    last_stat = stat_file()

    if last_stat is None:
        log("File not present yet.", "warn")
    else:
        log(f"Initial stat: size={last_stat[0]} mtime={last_stat[1]:.3f}")

    lines = read_lines()
    if lines:
        log(f"Initial read: {len(lines)} line(s)")
        # Bootstrap: find the latest parseable line to seed current_total,
        # then notify the user of the starting state.
        for ln in reversed(lines):
            p = parse(ln)
            if p is not None:
                current_total = p[1]
                break
        if current_total is not None:
            notify("Monika Affection — current level", f"Total {current_total:.2f}")
        else:
            notify("Monika Affection", "Watching log…  no events yet")
        anchor_line = lines[-1]
        log(f"Anchor set to: {shorten(anchor_line)}")
    else:
        log("Log empty or missing; will keep polling.", "warn")

    poll_count = 0
    while True:
        time.sleep(POLL_INTERVAL)
        poll_count += 1

        cur_stat = stat_file()

        # --- file appearance / disappearance ---
        if last_stat is None and cur_stat is not None:
            log("File has appeared.", "file")
            last_stat = cur_stat
        elif last_stat is not None and cur_stat is None:
            log("File disappeared.", "file")
            last_stat = None
            continue
        elif cur_stat is None:
            if poll_count % 10 == 0:
                log("still waiting for file…", "poll")
            continue

        size_changed = cur_stat[0] != last_stat[0]
        mtime_changed = cur_stat[1] != last_stat[1]

        if not (size_changed or mtime_changed):
            if poll_count % 10 == 0:
                log(f"no change (size={cur_stat[0]} mtime={cur_stat[1]:.3f})",
                    "poll")
            continue

        log(
            f"FILE CHANGE  size {last_stat[0]}→{cur_stat[0]}  "
            f"mtime {last_stat[1]:.3f}→{cur_stat[1]:.3f}",
            "file",
        )
        last_stat = cur_stat

        lines = read_lines()
        if not lines:
            log("Read failed/empty right after change; will retry.", "warn")
            continue

        log(f"Re-read {len(lines)} line(s).", "file")

        # --- find where we left off ---
        start = 0
        if anchor_line is not None:
            found = None
            for i in range(len(lines) - 1, -1, -1):
                if lines[i] == anchor_line:
                    found = i
                    break
            if found is None:
                log("Anchor line not found — file was rewritten.", "warn")
                # Fall back: only inspect the final line to catch a change.
                tail = lines[-1:]
                for line in tail:
                    current_total = handle_line(line, current_total, anchor_line)
                anchor_line = lines[-1]
                log(f"Re-anchored to: {shorten(anchor_line)}")
                continue
            start = found + 1

        new_lines = lines[start:]
        if not new_lines:
            log("No new lines past anchor.", "file")
            continue

        log(f"{len(new_lines)} new line(s) past anchor:", "file")
        for line in new_lines:
            current_total = handle_line(line, current_total, anchor_line)

        anchor_line = lines[-1]
        log(f"Anchor advanced to: {shorten(anchor_line)}")


if __name__ == "__main__":
    try:
        watch()
    except KeyboardInterrupt:
        log("Interrupted by user.", "warn")
        sys.exit(0)