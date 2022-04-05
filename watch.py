from mss import mss
import os, sys, time

def set_system_volume(volume):
    os_name = sys.platform
    if os_name == 'win32':
        os.system(f"pactl set-sink-volume 1 {volume}%")
    elif os_name == 'linux':
        os.system(f"pactl set-sink-volume 1 {volume}%")

time.sleep(5)
with mss() as sct:
    sct.shot()
