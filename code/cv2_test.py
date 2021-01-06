import numpy as np
import cv2
from pathlib import Path
import time
from globals import *
prev_frame_time = 0
new_frame_time = 0
time.sleep(0.1)

frame_rate = 24
prev = 0

cap = cv2.VideoCapture(gen_path + '/src/intro_6.mp4')

img = cv2.imread(gen_path + "/src/bar_xs.png", -1)
x_offset, y_offset = 100,100
y1, y2 = y_offset, y_offset + img.shape[0]
x1, x2 = x_offset, x_offset + img.shape[1]

alpha_s = img[:, :, 3] / 255.0
alpha_l = 1.0 - alpha_s

import cv2

def merge_image(back, front, x,y):
    # convert to rgba
    if back.shape[2] == 3:
        back = cv2.cvtColor(back, cv2.COLOR_BGR2BGRA)
    if front.shape[2] == 3:
        front = cv2.cvtColor(front, cv2.COLOR_BGR2BGRA)

    # crop the overlay from both images
    bh,bw = back.shape[:2]
    fh,fw = front.shape[:2]
    x1, x2 = max(x, 0), min(x+fw, bw)
    y1, y2 = max(y, 0), min(y+fh, bh)
    front_cropped = front[y1-y:y2-y, x1-x:x2-x]
    back_cropped = back[y1:y2, x1:x2]

    alpha_front = front_cropped[:,:,3:4] / 255
    alpha_back = back_cropped[:,:,3:4] / 255
    
    # replace an area in result with overlay
    result = back.copy()
    print(f'af: {alpha_front.shape}\nab: {alpha_back.shape}\nfront_cropped: {front_cropped.shape}\nback_cropped: {back_cropped.shape}')
    result[y1:y2, x1:x2, :3] = alpha_front * front_cropped[:,:,:3] + alpha_back * back_cropped[:,:,:3]
    result[y1:y2, x1:x2, 3:4] = (alpha_front + alpha_back) / (1 + alpha_front*alpha_back) * 255

    return result

while(cap.isOpened()):
	
	time_elapsed = time.time() - prev
	
	

	if time_elapsed > 1./frame_rate or True:
		prev = time.time()
		
		ret, frame = cap.read()
		
		gray = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
		frame = frame.swapaxes(0, 1)
		#gray = cv2.resize(frame, (500,300))
		
		new_frame_time = time.time() 
		fps = 1/(new_frame_time-prev_frame_time) 
		prev_frame_time = new_frame_time
		fps = str(fps)
		fps = fps.replace('.', ',')
		print(fps)

		cv2.rectangle(gray, (10,10), (110,110), (36, 82, 244), 2)

		
		for c in range(0, 3):
			gray[y1:y2, x1:x2, c] = (alpha_s * img[:, :, c] + alpha_l * gray[y1:y2, x1:x2, c])
		

		cv2.imshow('frame', gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			pass
		#	break


cap.release()
cv2.destroyAllWindows()
