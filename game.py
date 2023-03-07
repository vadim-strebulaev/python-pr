import numpy as np
import cv2
import pyautogui
import time
import imutils


# ball = []
# img = cv2.imread("C:\\Users\\Vadim\\Desktop\\BallImg1.png")

# # приводим изображение мяча к 11 * 11
# a = img.shape[1]
# b = img.shape[0]
# img = cv2.resize(img, (img.shape[1] // (img.shape[1] // 11), img.shape[0] // (img.shape[1] // 11)))
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# for i in range(11):
#     for j in range(11):
#         print(img1[i][j], end=" ")
#     print(" ")
# img = cv2.resize(img, (img.shape[1] * (a // 11), img.shape[0] * (b // 11)))
# cv2.imshow("1", img)
# cv2.waitKey(0)
f = 0
# берем изображение с компьютера
for i in range (20):
    img = pyautogui.screenshot(region=(250, 600, 450, 400))
    img = np.array(img)

    for i in range(img.shape[1]):
        for j in range(img.shape[0]):
            if img[i][j][0] <= 5 and img[i][j][1] <= 5 and img[i][j][2] <= 5:
                img[i][j] = [255, 255, 255]
                cv2.imshow("", img)
                cv2.waitKey(1)  
                pyautogui.click(i + 250, j + 450)
                f = 1
            if f == 1:
                break
        if f == 1:
            f = 0
            break
