import numpy as np
import cv2, time
img = cv2.imread('111.jpg')
cv2.imshow('pic', img)
cv2.waitKey(0)

img = cv2.Canny(img, 200, 0)
cv2.imshow('pic', img)
cv2.waitKey(0)
a = []
count = 0
for i in range(80, img.shape[0]):
    time.sleep(0.05)
    for j in range(img.shape[1]):
        if(img[i, j] != 0):
            img[i, j] = 0
            # a.append([i, j])
            # count += 1
        cv2.imshow('pic', img)
        cv2.waitKey(1)
print(a)
