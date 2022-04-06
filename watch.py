from mss import mss, tools as mss_tools
from pathlib import Path
import os, sys, time

BASE_DIR = Path(__file__).resolve(strict=True).parent

def set_system_volume(volume):
    os_name = sys.platform
    if os_name == 'win32':
        set_vol_path = os.path.join(BASE_DIR, 'SetVol.exe')
        print(set_vol_path)
        os.system(f"{set_vol_path} setvol {volume}")
    elif os_name == 'linux':
        os.system(f"pactl set-sink-volume 1 {volume}%")

time.sleep(5)
with mss() as sct:
    monitor = sct.monitors[0]
    box = {"top": 85, "left": 255, "width": 110, "height": 90}
    for i in range(0, 60):
        sct_img = sct.grab(box)
        mss_tools.to_png(sct_img.rgb, sct_img.size, output=f"result{i+1}.png")
        time.sleep(2)
    set_system_volume(0)
