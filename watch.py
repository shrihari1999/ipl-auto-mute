from pathlib import Path
from mss import mss, tools as mss_tools
from tensorflow import keras
from collections import deque
import os, sys, time, cv2, numpy as np

BASE_DIR = Path(__file__).resolve(strict=True).parent

def set_system_volume(volume):
    os_name = sys.platform
    if os_name == 'win32':
        set_vol_path = os.path.join(os.path.join(BASE_DIR, 'SetVol'), 'SetVol.exe')
        os.system(f"{set_vol_path} setvol {volume}")
    elif os_name == 'linux':
        os.system(f"pactl set-sink-volume 1 {volume}%")

box = {"top": 85, "left": 255, "width": 110, "height": 90}
labels = ['csk', 'dc', 'gt', 'ipl', 'kkr', 'lsg', 'mi', 'pbks', 'rcb', 'rr', 'srh']
img_size = 90
model = keras.models.load_model('./ipl_model')

muted = False
prediction_queue = deque(maxlen=2)
max_reached = False

time.sleep(5)
with mss() as sct:
    while True:
        sct_img = sct.grab(box)
        png = mss_tools.to_png(sct_img.rgb, sct_img.size)
        nparr = np.frombuffer(png, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)[...,::-1] #convert BGR to RGB format
        resized_arr = cv2.resize(img_np, (img_size, img_size)) # Reshaping images to preferred size
        x_val = np.array([resized_arr]) / 255
        x_val.reshape(-1, img_size, img_size, 1)
        predictions = model.predict(x_val)[0]
        prediction_queue.append(max(predictions) > 0.9)
        if max_reached:
            if len(set(prediction_queue)) == 1:
                if prediction_queue[0]:
                    if muted:
                        set_system_volume(50)
                        muted = False
                    print('logo', max(predictions))
                else:
                    if not muted:
                        set_system_volume(0)
                        muted = True
                    print('break', max(predictions))
        else:
            max_reached = len(prediction_queue) == prediction_queue.maxlen
        time.sleep(0.5)

# time.sleep(5)
# with mss() as sct:
#     monitor = sct.monitors[0]
#     for i in range(0, 300):
#         sct_img = sct.grab(box)
#         mss_tools.to_png(sct_img.rgb, sct_img.size, output=os.path.join(os.path.join(BASE_DIR, 'results'), f"result{i+1}.png"))
#         time.sleep(1)
#     set_system_volume(0)
