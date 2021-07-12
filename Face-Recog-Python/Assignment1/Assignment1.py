import cv2
import numpy as np

cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
	success, frame = cap.read()
	if success:
		gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
		cv2.imshow('Gray Frame', gray_frame) 
		cv2.imshow('Frame',frame)
		zeros = np.zeros((frame.shape[0],frame.shape[1]),np.uint8)
		b,g,r = cv2.split(frame)
		cv2.imshow('Blue',b)
		cv2.imshow('Green',g)
		cv2.imshow('Red',r)
		blue = cv2.merge((b,zeros,zeros))
		red = cv2.merge((zeros,zeros,r))
		green = cv2.merge((zeros,g,zeros))
		#cv2.imshow('Blue',blue)
		#cv2.imshow('Green',green)
		#cv2.imshow('Red',red)
		k = cv2.waitKey(10) 
		if k & 0xff == ord('q'):
			break
	else:
		break

cap.release()
cv2.destroyAllWindows()