import numpy as np
import cv2
from pathlib import Path
import time
prev_frame_time = 0
new_frame_time = 0
time.sleep(0.1)

cap = cv2.VideoCapture(str(Path(__file__).parent.absolute()) + '/src/intro_small.mp4')

while(cap.isOpened()):
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	#gray = cv2.resize(frame, (500,300))
	
	new_frame_time = time.time() 
	fps = 1/(new_frame_time-prev_frame_time) 
	prev_frame_time = new_frame_time
	fps = str(fps)
	fps = fps.replace('.', ',')
	print(fps)

	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()