#!/usr/bin/env python3

import subprocess
import time
import os
import signal

def run_script():
    script_path = "/root/grass5/localgrassdesktop_autoproxy.py"  # ganti letak folder script localgrassdesktop_autoproxy.py
    
    # Attempt to kill any existing instances of the script
    try:
        # Use pgrep to find the process ID of running script.py and kill it
        pids = subprocess.check_output(['pgrep', '-f', 'python3 ' + script_path]).decode().split()
        for pid in pids:
            os.kill(int(pid), signal.SIGTERM)
    except subprocess.CalledProcessError:
        pass  # No matching process found, which is okay

    # Run the script
    subprocess.Popen(["python3", script_path])

def main():
    while True:
        run_script()
        time.sleep(300)  # Sleep for 5 minutes (300 seconds)

if __name__ == "__main__":
    main()
