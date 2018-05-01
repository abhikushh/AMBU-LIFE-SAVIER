import cv2

backsub = cv2.createBackgroundSubtractorMOG2()
capture = cv2.VideoCapture("video1.avi")
i = 0
minArea=1
while True:
    ret, frame = capture.read()
    if ret:
        fgmask = backsub.apply(frame, learningRate=0.01)
        erode=cv2.erode(fgmask,None,iterations=3)     #erosion to erase unwanted small contours
        moments=cv2.moments(erode,True)               #moments method applied
        area=moments['m00']     
        if moments['m00'] >=minArea:
            x=int(moments['m10']/moments['m00'])
            y=int (moments['m01']/moments['m00'])
            if x>4 and x<95 and y>4 and y<95:       #range of line coordinates for values on left lane
                i=i+1
                print(i)
            elif x>10 and x<110 and y>10 and y<130: #range of line coordinatess for values on right lane
                i=i+1
                print(i)
                #print(x,y)
            cv2.putText(frame,'COUNT: %r' %i, (10,30), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 2)
            #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)  
            cv2.imshow("Track", frame)
            cv2.imshow("background sub", fgmask)
            key = cv2.waitKey(100)
            if key == ord('q'):
                break