import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
	success, frame = cap.read()
	if success:
		bg1 = cv2.imread('bg1.jpg')
		bg2 = cv2.imread('bg2.jpg')
		bg3 = cv2.imread('bg3.jpg')
		bg4 = cv2.imread('bg4.jpg')
		bg5 = cv2.imread('bg5.jpg')
		bg6 = cv2.imread('bg6.jpg')
		bg1 = cv2.resize(bg1, (frame.shape[1],frame.shape[0]))
		blended_video1 = cv2.addWeighted(frame, 0.7, bg1, 0.3, 0.1)
		bg2 = cv2.resize(bg2, (frame.shape[1],frame.shape[0]))
		blended_video2 = cv2.addWeighted(frame, 0.7, bg2, 0.4, 0.1)
		bg3 = cv2.resize(bg3, (frame.shape[1],frame.shape[0]))
		blended_video3 = cv2.addWeighted(frame, 0.7, bg3, 0.5, 0.1)
		bg4 = cv2.resize(bg4, (frame.shape[1],frame.shape[0]))
		blended_video4 = cv2.addWeighted(frame, 0.7, bg4, 0.6, 0.1)
		bg5 = cv2.resize(bg5, (frame.shape[1],frame.shape[0]))
		blended_video5 = cv2.addWeighted(frame, 0.7, bg5, 0.7, 0.1)
		bg6 = cv2.resize(bg6, (frame.shape[1],frame.shape[0]))
		blended_video6 = cv2.addWeighted(frame, 0.7, bg6, 0.8, 0.1)
		added6 = frame + bg6
		cv2.imshow("Blended Video 1", blended_video1)
		cv2.imshow("Blended Video 2", blended_video2)
		cv2.imshow("Blended Video 3", blended_video3)
		cv2.imshow("Blended Video 4", blended_video4)
		cv2.imshow("Blended Video 5", blended_video5)
		cv2.imshow("Blended Video 6", blended_video6)
		cv2.imshow("Added", added6)
		#cv2.imshow("Actual", frame)
		k = cv2.waitKey(10)
		if k & 0xff == ord('q'):
			break
	else:
		break

cap.release()
cv2.destroyAllWindows()
