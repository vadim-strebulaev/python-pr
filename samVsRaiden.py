import cv2
import time
while True:
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("C:\\Users\\Вадим\\Documents\\DocVid.mp4")
    success, well = cap.read()
    s = cv2.resize(well, (well.shape[1] // 3, well.shape[0] // 11))
    print(s.shape)
    pixs = 34
    pixs1 = 160

    a = [[0] * pixs1] * pixs
    b = []
    massive = []
    count = 0
    while True:
        if count % 3 == 0:
            success, img = cap.read()
            if not success:break
            img = cv2.resize(img, (img.shape[1] // 3, img.shape[0] // 11)) #D4DJ1 - 7 20, VFP5 - 3 10
            # img = cv2.flip(img, 1)

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
            # print('\n'.join(b))
            # time.sleep(0.0001)
            a = [[0] * pixs1] * pixs
            b = []
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        count += 1
    while True:
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
