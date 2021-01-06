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
