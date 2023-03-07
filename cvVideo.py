import cv2, time, numpy as np
from tkinter import *
def convert_to_ascii(image, scale=100):
    ascii_chars = ["@", "#", "S", "%", "A", "R", ";", ":", " ", " ", " ", " "]
    ascii_chars.reverse()
    ascii_char_count = len(ascii_chars)
    image = cv2.resize(image, (150, 50))
    image_array = np.array(image)
    image_array = image_array / 255
    result = ""
    for row in image_array:
        for pixel in row:
            average = int(np.average(pixel) * ascii_char_count)
            result += ascii_chars[average % ascii_char_count]
        result += "\n"
    return result
label = None
while True:
    cap = cv2.VideoCapture("C:\\Users\\Vadim\\Documents\\VFP4.mp4")
    massive = []
    count = 0
    while len(massive) <= 300:
        if count % 1 == 0:
            success, img = cap.read()
            if not success:break
            ascii_art = convert_to_ascii(img, scale=100)
            massive.append(ascii_art)
            # print(massive[-1])
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        count += 1
    with open("C:\\Users\\Vadim\\Documents\\mass.txt", "w") as file:
        for i in range(len(massive)):
            file.write(str(''.join(massive[i]) + "\n"))
        file.close()
    while True:
        for i in range(len(massive)):
            print(''.join(massive[i]))
            time.sleep(0.02)