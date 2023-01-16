import cv2, imutils, numpy as np
from matplotlib import pyplot as pl
img = cv2.imread('LKPY.png')
cv2.imshow('Микроскоп', img)
cv2.waitKey(0)

img = cv2.Canny(img, 1, 200)

cv2.imshow('Микроскоп', img)
cv2.waitKey(0)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_filter = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(img_filter, 0, 50)
cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
cont = sorted(cont, key=cv2.contourArea, reverse=True)

pos = []
for c in cont:
    approx = cv2.approxPolyDP(c, 1, True)
    print(approx)
masks = np.zeros(img.shape, np.uint8)
print(1)
new_img = cv2.drawContours(masks, [pos], 0, 255, -1)
print(1)
btws = cv2.bitwise_and(img, img, masks)
cv2.imshow('Микроскоп', btws)
cv2.waitKey(0)
print(1)
pl.imshow(cv2.cvtColor(btws, cv2.COLOR_BGR2RGB))
print(1)
pl.show()