import numpy as np
import cv2
import os
def nothing(x):
    pass
cv2.namedWindow("trackbar")
cv2.resizeWindow("trackbar",600,200)

cv2.createTrackbar("Hue min","trackbar",0,179,nothing)
cv2.createTrackbar("Hue max","trackbar",179,179,nothing)
cv2.createTrackbar("saturation min","trackbar",0,255,nothing)
cv2.createTrackbar("saturation max","trackbar",255,255,nothing)
cv2.createTrackbar("value min","trackbar",0,255,nothing)
cv2.createTrackbar("value max","trackbar",255,255,nothing)



cap=cv2.VideoCapture(0)
while True:
    _x,img=cap.read()
    hsvimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hmin = cv2.getTrackbarPos("Hue min", "trackbar")
    hmax = cv2.getTrackbarPos("Hue max", "trackbar")
    smin = cv2.getTrackbarPos("saturation min", "trackbar")
    smax = cv2.getTrackbarPos("saturation max", "trackbar")
    vmin = cv2.getTrackbarPos("value min", "trackbar")
    vmax = cv2.getTrackbarPos("value max", "trackbar")

    val = np.array([hmin, smin, vmin, hmax, smax, vmax])
    print(val)
    min = val[0:3]
    max = val[3:6]
    print(min, max)

    mask = cv2.inRange(hsvimg, min, max)
    cv2.imshow("masked", mask)
    cv2.imshow("image", img)

    cv2.waitKey(1)