import cv2
import numpy as np
def dealMonkeyPicture():
    img=cv2.imread('D:\\zhaoyq\\screen\\allScreen.png',cv2.IMREAD_COLOR)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([0, 60, 10])
    upper_blue = np.array([50, 255, 255])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    res=cv2.bitwise_and(img,img,mask=mask)
    # cv2.imshow('hsv',hsv)
    # //cv2.imshow('mask',mask)
    # cv2.imshow('res',res)
    # //cv2.imshow('img',img)
    cv2.imwrite('D:\\zhaoyq\\screen\\monkey\\allScreen.png',res, [int(cv2.IMWRITE_PNG_COMPRESSION), 1])
