import cv2 as cv
import time
import numpy as np


cam=cv.VideoCapture(1)
cam.set(3,320)
cam.set(4,240)

while 1:
	ret,frame=cam.read()
	B,G,R=cv.split(frame)
	HSV=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
	H,S,V=cv.split(HSV)
	bin=cv.inRange(S,150,255)
	cv.namedWindow("ball",cv.WINDOW_AUTOSIZE)
	cv.imshow("ball",bin)
	cv.waitKey(50)
	contours, hierarchy = cv.findContours(bin,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
	for i in range(0,len(contours)):
		if cv.contourArea(contours[i]) > 500:
			x,y,width,height=cv.boundingRect(contours[i])
			if abs(width-height)<5 and abs((3.14*width*width)/4 - cv.contourArea(contours[i]))<400:
				print "Ball is present\n"
				print "x coord: ",x+width/2,"\n"
				print "y coord: ",y+height/2,"\n"
				print "width: ",width,"\n"
				print "height: ",height,"\n"
				print "Area: ",(3.14*(width)*(width))/4,"\n"
				print "Contour Area: ",cv.contourArea(contours[i])
			else:
				print "Ball is not present"
				
