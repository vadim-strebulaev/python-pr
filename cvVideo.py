import cv2, time
from tkinter import *
import threading

label = None
while True:
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("C:\\Users\\Вадим\\Documents\\DocVid.mp4")
    pixs = 54
    pixs1 = 160

    a = [[0] * pixs1] * pixs
    b = []
    massive = []
    count = 0
    while True:
        if count % 1 == 0:
            success, img = cap.read()

            if not success:break
            img = cv2.resize(img, (img.shape[1] // 3, img.shape[0] // 7))#D4DJ1 - 7 20 / 14 14, VFP5 - 3 10 / 7 7
            # img = cv2.flip(img, 1)
            print(img.shape)

            cv2.imshow('Name', img)
            cv2.waitKey(1)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # print(img.shape)

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
                        a[i][j] = "▇"
                        # img[i, j] = 0
                    elif (img[i, j] <= 218):
                        a[i][j] = "█"
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
    # while True:
    #     for i in range(len(massive)):
    #         print('\n'.join(massive[i]),"---")
    #         time.sleep(0.05)


    def window():
        global label

        root = Tk()
        label = Label(root, text='', fg='white')
        label.pack()

        root.mainloop()

        root.configure(bg='blue')
    thread = threading.Thread(target=window)
    thread.start()
    time.sleep(1)

    while True:
        for i in range(len(massive)):
            mytext = '\n'.join(massive[i])
            time.sleep(0.05)

            label.config(text=mytext)
            label.configure(bg="black")