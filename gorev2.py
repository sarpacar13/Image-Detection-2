import cv2
import numpy as np
import datetime

video = cv2.VideoCapture('gorev2.mp4')
#object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

lower = np.array ([0,0,0])
upper = np.array([45,45,255])


flag =0

while(video.isOpened()):
  ret, frame=video.read()
  h,w,_ = frame.shape
  
  

  upperBound=int(h/10)
  lowerBound=int(h*9/10)
  leftBound=int(w/4)
  rightBound=int(w*3/4)
  
  cood1 = (leftBound, upperBound)
  cood2 = (rightBound, lowerBound)
  
  
  mask = cv2.inRange(frame,lower,upper) 
  _, mask = cv2.threshold(mask, 254,255, cv2.THRESH_BINARY)
  countors, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  frame=cv2.rectangle(frame, (cood1),(cood2), (0, 0, 255), 10)
  
  
  for i in countors:
    area = cv2.contourArea(i)
    
    
    
    x,y,wi,hi = cv2.boundingRect(i)
    if x+wi<=cood2[0] and x>=cood1[0] and y>=cood1[1] and y+hi<=cood2[1] and wi/w>=0.1 and hi/h>=0.1 and flag==0:
      frame=cv2.rectangle(frame, ((x),(y)),((x+wi) ,(y+hi)), (0, 255, 0), 1)
      cv2.drawContours(frame, [i], -1, (255,255,255), 2)
      frame=cv2.putText(frame, "Kilitlenme Dortgeni", (x-10,y+125), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
      print("Frame'i %", (hi/h)*100,"yatayda ve %", (wi/w)*100 ,"dikeyde kapsayan hedef, hedef vuruş alanında")
      
      if (time1)!=0:
        time2 =datetime.datetime.now()
      else:
        time1 = datetime.datetime.now()
        time2 = datetime.datetime.now()
      print("TIME: ", ((time2-time1).seconds),".", ((time2-time1)).microseconds) 
      if (time2-time1).seconds>=5:
        
        print("Hedefe kitlenme basarili.")
        flag =1
      
    else:
      time1=0
      time2=0
      
      
      
    


      
      
  

  cv2.imshow("frame", frame)
  #cv2.imshow("mask", mask)
  if cv2.waitKey(25) & 0xFF == ord('q'):
    break

video.release()
cv2.destroyAllWindows()