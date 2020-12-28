import cv2 
import numpy as np
import time
import pyautogui 
url = 'http://192.168.43.1:8080/video'
cap = cv2.VideoCapture(url)
flag=0
flag2=0
while(True):
    ret, frame = cap.read()
    if frame is not None:
        if(flag==0):
            firstframe=frame.copy()
            
            flag=1 
        diff=cv2.subtract(firstframe,frame);
        b,g,r=cv2.split(diff);
       	
        if(cv2.countNonZero(b)>1300000 and cv2.countNonZero(g)>1300000 and cv2.countNonZero(r)>1300000):
        	   pyautogui.hotkey('ctrl','alt','d')
        	   break

    q = cv2.waitKey(1)
    if q == ord("q"):
        break
    
cv2.destroyAllWindows()
