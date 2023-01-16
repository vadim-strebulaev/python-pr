import numpy as np
import cv2, sys
import time
img = cv2.imread('111.jpg')#переменная img - картинка 111
newimg = cv2.resize(img, (640, 853))# новая переменная newimg - это картинка img с размерами 640 - ширина и 853 - высота

print(img.shape)# выводит размер картинки img 1 параметр - высота, 2 параметр - ширина, 3 параметр - цветовой фон(RGB) P.S. тут BGR
# cv2.imshow('Name', img)# показывает картинку img
# cv2.waitKey(0)# задержка перед закрытием в миллисекундах, 0 - бесконечность

newimg = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2)) # меняем размер в 2 раза
cv2.imshow('Name', newimg[0:100, 0:150])# показывает картинку newimg, только обрезает(её верхние левые пиксели)

newimg = cv2.GaussianBlur(newimg, (3, 3), 0)# размытие с силой 3 и 3 (только нечет значения) и 0 - что-то типа силы размытия
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# приводим картинку к черно-белому цвету
img = cv2.Canny(img, 90, 90)# указывает края цветов с точносью 90(чувствительность больше, при меньшем значении)

kernel = np.ones((5,5), np.uint8)#создает матрицу со всеми единицами 5 * 5 все значения - int
arr = []
img = cv2.dilate(img, kernel,iterations=1) #утолщаем обводки
img = cv2.erode(img, kernel, iterations=1) #утончаем обводку(+убираем тонкие места)
# cap = cv2.VideoCapture("C:\\Users\\Вадим\\Documents\\VFP4.mp4")
massive = []

while True:
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture("C:\\Users\\Вадим\\Documents\\D4DJ1.mp4")
    pixs = 32
    pixs1 = 160

    a = [[0] * pixs1] * pixs
    b = []
    count = 0
    while True:
        if count % 3 == 0:
            success, img = cap.read()
            if not success:break
            img = cv2.resize(img, (img.shape[1] // 4, img.shape[0] // 15)) #D4DJ1 - 7 20
            img = cv2.flip(img, 1)

            cv2.imshow('Name', img)
            cv2.waitKey(1)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            print(img.shape)

            for i in range(pixs):
                # cv2.imshow('IN', img)
                # cv2.waitKey(1)
                for j in range(pixs1):
                    if (img[i, j] == 0):
                        a[i][j] = "▁"
                        # img[i, j] = 0
                    elif (img[i, j] < 33):
                        a[i][j] = "▂"
                        # img[i, j] = 0
                    elif (img[i, j] <= 70):
                        a[i][j] = "▃"
                        # img[i, j] = 0
                    elif (img[i, j] <= 107):
                        a[i][j] = "▅"
                        # img[i, j] = 0
                    elif (img[i, j] <= 144):
                        a[i][j] = "▅"
                        # img[i, j] = 0
                    elif (img[i, j] <= 181):
                        a[i][j] = "▆"
                        # img[i, j] = 0
                    elif (img[i, j] <= 218):
                        a[i][j] = "▇"
                        # img[i, j] = 0
                    elif (img[i, j] <= 255):
                        a[i][j] = "█"
                        # img[i, j] = 0
                b.append(''.join(a[i]))
            massive.append(b)
            print('\n'.join(b))
            # time.sleep(0.0001)
            a = [[0] * pixs1] * pixs
            b = []
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        count += 1
    # while True:
    for i in range(len(massive)):
        print('\n'.join(massive[i]),"---")
        time.sleep(0.05)
    #
    # for i in range(img.shape[1] - 1):
    #     for n in range(img.shape[0] - 1):
    #         if(img[n, i] == 255):
    #             countBlack = 0
    #             if(img[n - 1, i - 1] == 255):
    #                 countBlack += 1
    #             if(img[n, i - 1] == 255):
    #                 countBlack += 1
    #             if (img[n , i + 1] == 255):
    #                 countBlack += 1
    #             if (img[n - 1, i] == 255):
    #                 countBlack += 1
    #             if (img[n + 1, i] == 255):
    #                 countBlack += 1
    #             if (img[n + 1, i - 1] == 255):
    #                 countBlack += 1
    #             if (img[n + 1, i] == 255):
    #                 countBlack += 1
    #             if (img[n + 1, i + 1] == 255):
    #                 countBlack += 1
    #             arr.append([i, n, countBlack])
    # print(arr)
    # # cv2.imshow('Name', img) # показывает картинку img
    # # cv2.waitKey(0) # задержка перед закрытием в миллисекундах, 0 - бесконечность
    # k = 0
    # l = 0
    # newimage = np.zeros((853, 640, 3), dtype='uint8')
    # for i in range(len(arr)):
    #     k = arr[i]
    #     cv2.imshow('Name', newimage)  # показывает картинку newimage
    #     cv2.waitKey(1)  # задержка перед закрытием в миллисекундах, 0 - бесконечность
    #     newimage[k[1], k[0]] = [255, 255, 255]
    # print("------")
    # cv2.imshow('Name', newimage) # показывает картинку newimage
    # cv2.waitKey(0) # задержка перед закрытием в миллисекундах, 0 - бесконечность
