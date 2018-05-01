# -*- coding: utf-8 -*-

import cv2
print(cv2.__version__)

cascade_src = 'cars.xml'
video_src = 'video1.avi'
counter=0
i=0
#video_src = 'dataset/video2.avi'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    
   
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)  
        if x>4 and x<95 and y>4 and y<95:       #range of line coordinates for values on left lane
                i=i+1
                print(i)
        elif x>10 and x<110 and y>10 and y<130: #range of line coordinatess for values on right lane
                i=i+1
                print(i)

    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows 