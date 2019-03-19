# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 13:46:48 2018

@author: Carl
"""
import cv2
import numpy as np

origin_img = cv2.imread("D:/rose.png",0)
image=cv2.resize(origin_img,(512,512))
cv2.imshow("1",image)
cv2.waitKey(0)
#img=cv2.GaussianBlur(image,(5,5),0)
ret2,th2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(ret2)
print(type(th2))
print(th2)
cv2.imshow("1",th2)
cv2.waitKey(0)
