import cv2
import numpy as np

import os
import glob

img = cv2.imread('task_002/train_imgs/001_roundShape.jfif')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,200,apertureSize=3)
cv2.imwrite('hogulines2.jpg', edges)
minn = 180
lines = cv2.HoughLines(edges,1,np.pi/180,minn)
print(len(lines))
for i in range(len(lines)):
   for rho,theta in lines[i]:
       a = np.cos(theta)
       b = np.sin(theta)
       x0 = a*rho
       y0 = b*rho
       x1 = int(x0 + 1000*(-b))
       y1 = int(y0 + 1000*(a))
       x2 = int(x0 - 1000*(-b))
       y2 = int(y0 - 1000*(a))
       cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow(img)


"https://note.com/upyc101/n/n856e3ad50a57"
