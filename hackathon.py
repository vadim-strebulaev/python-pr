# и так
# 19:28 21.12.22 начал
import cv2, numpy, time, os
import tifffile as tiff
from PIL import Image
# im = Image.open('C:\\Users\\Вадим\\PycharmProjects\\pythonProject1\\Files for Hackathon\\Files for Hackathon\\003.tif')
# im.save('test.png')
for infile in os.listdir("./"):
    print("file : " + infile)
    if infile[-3:] == "tif" or infile[-3:] == "bmp" :
       # print "is tif or bmp"
       outfile = infile[:-3] + "jpeg"
       im = Image.open(infile)
       print("nju filename : " + outfile)
       out = im.convert("RGB")
       out.save(outfile, "JPEG", quality=90)
# загружаем файл
img = tiff.imread('C:\\Users\\Вадим\\PycharmProjects\\pythonProject1\\Files for Hackathon\\Files for Hackathon\\test.png')

cv2.imshow('Name', img)
print(img.shape)
cv2.waitKey(0)

img = cv2.resize(img, (img.shape[1] // 6, img.shape[0] // 6)) # меняем размер в 6 раз
cv2.imshow('Name', img)
cv2.waitKey(0)

print(img.shape)


# img = img[0:img.shape[1], 0:img.shape[0]]
crop_img = img[0:20, 0:20]

# Show image
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)

