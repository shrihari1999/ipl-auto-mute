from pathlib import Path
from mss import mss, tools as mss_tools
from tensorflow import keras
from collections import deque
import os, sys, time, cv2, numpy as np

OS_NAME = sys.platform
BASE_DIR = Path(__file__).resolve(strict=True).parent
MODEL_MONITOR_DIMENSIONS = {'width': 1440, 'height': 900}
MODEL_MONITOR_BOX = {'top': 85, 'left': 255, 'width': 110, 'height': 90}

def set_system_volume(volume):
    if OS_NAME == 'win32':
        set_vol_path = os.path.join(os.path.join(BASE_DIR, 'SetVol'), 'SetVol.exe')
        os.system(f"{set_vol_path} setvol {volume}")
    elif OS_NAME == 'linux':
        os.system(f"pactl set-sink-volume 1 {volume}%")

# labels = ['csk', 'dc', 'gt', 'ipl', 'kkr', 'lsg', 'mi', 'pbks', 'rcb', 'rr', 'srh']
img_size = 90
model = keras.models.load_model('./ipl_model')

muted = False
prediction_queue = deque(maxlen=3)
max_reached = False

print('Waiting 5 secs, open the hotstar window in full screen.')
time.sleep(5)
print('Program is active. Sit back, relax and enjoy the game!')
with mss() as sct:
    monitor = sct.monitors[0]
    height_correction = -35 if monitor['width'] / monitor['height'] > 1.7 else 0
    width_factor = (monitor['width']+height_correction) / MODEL_MONITOR_DIMENSIONS['width']
    height_factor = (monitor['height']+height_correction) / MODEL_MONITOR_DIMENSIONS['height']
    client_monitor_box = {
        'top': round(height_factor * MODEL_MONITOR_BOX['top']) + monitor['top'],
        'left': round(width_factor * MODEL_MONITOR_BOX['left']) + monitor['left'],
        'width': round(width_factor * MODEL_MONITOR_BOX['width']),
        'height': round(height_factor * MODEL_MONITOR_BOX['height'])
    }
    while True:
        sct_img = sct.grab(client_monitor_box)
        png = mss_tools.to_png(sct_img.rgb, sct_img.size)
        nparr = np.frombuffer(png, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)[...,::-1] #convert BGR to RGB format
        resized_arr = cv2.resize(img_np, (img_size, img_size)) # Reshaping images to preferred size
        x_val = np.array([resized_arr]) / 255
        x_val.reshape(-1, img_size, img_size, 1)
        predictions = model.predict(x_val)[0]
        prediction_queue.append(predictions[0] > predictions[1])
        if max_reached:
            if len(set(prediction_queue)) == 1:
                if prediction_queue[0]:
                    if muted:
                        set_system_volume(50)
                        muted = False
                    # print('logo', predictions)
                else:
                    if not muted:
                        set_system_volume(0)
                        muted = True
                    # print('break', predictions)
        else:
            max_reached = len(prediction_queue) == prediction_queue.maxlen
        time.sleep(0.1)

# Used for gethering dataset
# time.sleep(5)
# with mss() as sct:
#     monitor = sct.monitors[0]
#     height_correction = -35 if monitor['width'] / monitor['height'] > 1.7 else 0
#     width_factor = (monitor['width']+height_correction) / MODEL_MONITOR_DIMENSIONS['width']
#     height_factor = (monitor['height']+height_correction) / MODEL_MONITOR_DIMENSIONS['height']
#     client_monitor_box = {
#         'top': round(height_factor * MODEL_MONITOR_BOX['top']) + monitor['top'],
#         'left': round(width_factor * MODEL_MONITOR_BOX['left']) + monitor['left'],
#         'width': round(width_factor * MODEL_MONITOR_BOX['width']),
#         'height': round(height_factor * MODEL_MONITOR_BOX['height'])
#     }
#     print(client_monitor_box)
#     for i in range(0, 300):
#         sct_img = sct.grab(client_monitor_box)
#         mss_tools.to_png(sct_img.rgb, sct_img.size, output=os.path.join(os.path.join(BASE_DIR, 'results'), f"result{i+1}.png"))
#         time.sleep(1)
#     set_system_volume(0)
