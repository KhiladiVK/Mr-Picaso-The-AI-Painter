import numpy as np
import cv2
import os

cap=cv2.VideoCapture(0)
cap.set(3,500)
cap.set(4,600)
colors=[[35,100,102,82,252,255],#green
        [10,200,142,132,255,255],#parrot green
        [69,108,121,128,243,255],
        [142,144,130,179,255,255]]#blue,something like dark
colname=["green","parrotgreen","blue","pink"]
colorsmarker=[[0,204,0],[5,255,255],[255,255,5],[127,2,255]] #color should be in bgr format
points=[]

def drawtip(points,imgcontour,colorsmarker):
    for i,tip in enumerate(points):
        cv2.circle(imgcontour,tip, 10, colorsmarker[i%4], cv2.FILLED)




def getContours(img,imgcontour):
    x, y, w, h = 0, 0, 0, 0


    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cont in contours:
        area = cv2.contourArea(cont)
        print(area)
        if area>500:
            #cv2.drawContours(imgcontour, cont, -1, (0, 0, 255), 3)
            perim=cv2.arcLength(cont,True)
            corpoints=cv2.approxPolyDP(cont,0.2*perim,True)# for corner points
            nopoints=len(corpoints)
            x,y,w,h=cv2.boundingRect(corpoints)
            #cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),5)
            #tip=int(x+w/2),int(y)
            #return tip

            tip= int(x+w/2),int(y)
            return tip




def masking(img,colors,colorsmarker):
    hsvimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for i, col in enumerate(colors):
        col=np.array(col)
        mask=cv2.inRange(hsvimg,col[0:3],col[3:6])
        tip=getContours(mask,img)
        points.append(tip)
        drawtip(points,img,colorsmarker)

    cv2.imshow(colname[i],img)

while True:
    _suc,img=cap.read()
    cv2.imshow("image",img)

    masking(img,colors,colorsmarker)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()