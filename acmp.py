# a = int(input())
# b = [0] * a
#
# for i in range(a):
#     b[i] = list(map(int, input().split()))
# for i in range(len(b)):
#     b[i] = b[i][::-1]
# x = [b[i].copy() for i in range(a)]
#
# for i in range(len(b)):
#     for n in range(len(b)):
#         x[i][n] = b[n][i]
#
# for i in range(len(x)):
#     x[i] = x[i][::-1]
# for i in range(len(x)):
#     for n in range(len(x[i])):
#         print(x[i][n], end=" ")
#     print("")



#транспон - 3
#
# l, k = map(int, input().split())
# a = [0] * l
# for i in range(l):
#     a[i] = list(map(int, input().split()))
# for i in range(len(a)):
#     a[i] = a[i][::-1]
# for i in range(len(a)):
#     for n in range(len(a[i])):
#         print(a[i][n], end=" ")
#     print("")
#транспон - 4
#
# l, k = map(int, input().split())
# a = [0] * l
# for i in range(l):
#     a[i] = list(map(int, input().split()))
#
# b = [a[i].copy() for i in range(l)]
#
# for i in range(l//2):
#     a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
#
#
# for i in range(len(a)):
#     for n in range(len(a[i])):
#         print(a[i][n], end=" ")
#     print("")


# stack
# a = [2, 3, 4, 5, 6]
# def pop(a):
#     if(len(a) > 0):
#         a.pop(0)
#         return 0
#     else:
#         return 1
# def get(a):
#     return a[0]
# def popvalue(a):
#     if(len(a) > 0):
#         i = a[0]
#         a.pop(0)
#         return i
#     else:
#         return
# def get_ind(a, i):
#     g = 0
#     if(i <= len(a)):
#         t = []
#         for j in range(i):
#             t.append(a[0])
#             a.pop(0)
#         g = a[0]
#         for j in range(i):
#             a.insert(0, t[-1])
#             t.pop(-1)
#     return g
#
#
# def push(a, n):
#     a = a + [n]
#     return 0
# print(get_ind(a, 2))

# ПОЛКА

# n = int(input())
# a = []
# while n != 0:
#     x, y = map(int, input().split())
#     if x == 1:
#         a.insert(0, str(str(x) + " " + str(y)))
#     if(x == 2):
#         a.append(str(str(x) + " " + str(y)))
#     n -= 1
# print(a)
#
#


# leetcode
# nums = [2, 7, 11, 15]
# target = 9
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i != j:
#             if nums[i] + nums[j] == target:
#                 print([i, j])




#
# k = int(input())
# i = k
# s = 0
# while i != 0:
#     i //= 2
#     s += i
#     print(i)

# a = [i for i in range(1, k + 1)]
# lenght = 0 
# n = 1
# while True:
#     n += 1
#     if 2 ** n > len(a) - 1:
#         a.extend([0] * (2 ** n - len(a)))
#         break
# c = 0
# while c < len(a) - 1:
#     a.append(a[c] + a[c + 1])
#     c += 2
# print(a)


import cv2 
import numpy as np
def convert_to_ascii(image, scale=100):
    ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ","]
    ascii_char_count = len(ascii_chars)
    
    # Open the image and resize it

    image = cv2.resize(image, (100, 50))
    image_array = np.array(image)

    # Normalize the image array so that the values are between 0 and 1
    image_array = image_array / 255

    # Convert the image array to ASCII characters
    result = ""
    for row in image_array:
        for pixel in row:
            average = int(np.average(pixel) * ascii_char_count)
            result += ascii_chars[average % ascii_char_count]
        result += "\n"

    return result
image_path = "C:\\Users\\Vadim\\Documents\\photo_2022-03-07_15-58-05.jpg"
image = cv2.imread(image_path)
ascii_art = convert_to_ascii(image, scale=100)
print(ascii_art)