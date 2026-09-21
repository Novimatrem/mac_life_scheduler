import os
import time
import datetime
import subprocess
import sys

time.sleep(3)

def clear_terminal():
    os.system('clear')

# Duration of the alarming in seconds
ALARMING_DURATION = 30 

def trigger_independent_popup(event_label):
    """Fires a detached, high-priority system alert."""
    script = f'display alert "{event_label}" message "- life scheduler event -" buttons {{"Thanks!"}} default button "Thanks!"'
    subprocess.Popen(["osascript", "-e", script])

def absolute_max_volume():
    """Cranks volume and overrides any 'Mute' or 'Lower Volume' attempts."""
    os.system("osascript -e 'set volume output volume 100'")
    os.system("osascript -e 'set volume without output muted'")

def run_alert(event_label):
    print(f"\n[!!!] DEPLOYING ALARMING — {event_label}")
    
    # 1. Start Persistent Volume Enforcement in the background
    # This prevents you from turning the sound down while it's playing.
    volume_lock = subprocess.Popen(["/bin/bash", "-c", f"while [ $SECONDS -lt {ALARMING_DURATION} ]; do osascript -e 'set volume output volume 100'; sleep 0.5; done"])

    # 2. PHASE 1: THE OVERLAP (Simultaneous High/Low Frequency Explosion)
    # We trigger these all at once to create a wall of noise.
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Morse.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Funk.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Sosumi.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Basso.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Blow.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Bottle.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Frog.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Funk.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Glass.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Hero.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Morse.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Ping.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Pop.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Purr.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Sosumi.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Submarine.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Tink.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Basso.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Blow.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Bottle.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Frog.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Funk.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Glass.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Hero.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Morse.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Ping.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Pop.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Purr.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Sosumi.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Submarine.aiff"])
    subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Tink.aiff"])

    # 3. PHASE 2: THE VOICES (The Trio)
    # Zarvox (Robot/Alien), Trinoids (High-pitch mechanical), and Bells (Metal clanging)
    # These play simultaneously.
    print("[!] Engaging Synthesized Voices...")
    subprocess.Popen(["say", "-v", "Bells", "e. e. e. e. e. e. e. e. e. e. e. e. e. e. e. e. e. e. e. e. e. e. e. e."]) #perfect length, do not change.
    subprocess.Popen(["say", "-v", "Trinoids", "ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT. ALERT."]) #perfect length, do not change.
    subprocess.Popen(["say", "-v", "Bells", "DING. DONG. DING. DONG. DING. DONG. DING. DONG. DING. DONG. DING. DONG. DING. DONG. DING. DONG. DING. DONG. DING. DONG. DING. DONG. DING. DONG."]) #perfect length, do not change.

    # 4. PHASE 3: THE SIREN (Blocking Loop)
    # This ensures the sound continues for the full duration.
    start_time = time.time()
    while time.time() - start_time < ALARMING_DURATION:
        # Rapid-fire 'Submarine' and 'Hero' sounds
        subprocess.run(["afplay", "-v", "4", "/System/Library/Sounds/Submarine.aiff"])
        subprocess.run(["afplay", "-v", "4", "/System/Library/Sounds/Hero.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Morse.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Funk.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Sosumi.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Basso.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Blow.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Bottle.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Frog.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Funk.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Glass.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Hero.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Morse.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Ping.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Pop.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Purr.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Sosumi.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Submarine.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Tink.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Basso.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Blow.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Bottle.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Frog.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Funk.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Glass.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Hero.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Morse.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Ping.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Pop.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Purr.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Sosumi.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Submarine.aiff"])
        subprocess.Popen(["afplay", "-v", "5", "/System/Library/Sounds/Tink.aiff"])

        time.sleep(3) # give time for the noises to stop before the speaking happens
        # 3 is the minimum. no less than 3.
        
    # 5. POST-ALARM: The Command
    subprocess.run(["say", "-v", "Alex", f"Life skheduler event: {event_label}. ..."])

    # 6. Launch Popup (Detached)
    trigger_independent_popup(event_label)
    
    # Clean up the volume lock just in case
    volume_lock.terminate()
    print(f"[SUCCESS] Alerting concluded. Resuming checking for events.")

def prevent_sleep():
    """Forces display, system, and disk to stay awake at full power."""
    try:
        subprocess.Popen(["caffeinate", "-dimu", "-t", "60"])
    except FileNotFoundError:
        pass

def check_event(now, day, hour, minute):
    return (
        now.strftime("%A") == day and
        now.hour == hour and
        now.minute == minute
    )

# --- SCHEDULE DEFINITION ---
EVENTS = [
    ("Movement Group",    "removed",     9, 55),
    ("Walking Group",     "removed", 11, 55),
    ("Shower Reminder",    "removed",    16, 3),
    ("Test event 1",    "removed",    16, 2),
    ("Test event 2",    "removed",    16, 4),
]

for weekday in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    EVENTS.append(("Wake Up Reminder", weekday, 8, 00))
    EVENTS.append(("Hair Brush Reminder", weekday, 12, 30))
    EVENTS.append(("Go Sleep Reminder", weekday, 23, 15))

def main():
    clear_terminal()
    print("--- LIFE SCHEDULER: MAC EDITION ---")
    print("Audio: Simultaneous Layers | Volume: Forced 100% | Popups: Independent")
    
    # Startup Diagnostic (WARNING: This will be 100% volume)
    run_alert("Startup Diagnostic Completed")

    last_triggered = None

    while True:
        now = datetime.datetime.now()
        time_str = now.strftime('%A %H:%M:%S')
        
        sys.stdout.write(f"\r[TICK] {time_str} | Monitoring... ")
        sys.stdout.flush()
        
        prevent_sleep()

        for label, day, hour, minute in EVENTS:
            if check_event(now, day, hour, minute):
                current_id = f"{day}_{hour}_{minute}"
                if last_triggered != current_id:
                    run_alert(label)
                    last_triggered = current_id
                break

        time.sleep(1)

if __name__ == "__main__":
    main()
