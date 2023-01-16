# from math import floor
# from math import ceil
#
# n = int(input())
# m = int(input())
# k = int(input())
# t = 0
# count = n / m
# ost = n
# for i in range(m):
#     if ost > ceil(count):
#         ost -= ceil(count)
#         t += ceil(ceil(count) / k)
#         continue
#     else:
#         ost -= floor(count)
#         t += ceil(floor(count) / k)
# print(t)


#2
# arr = [] * 100
# x = str(input())
# countM = 0
# countL = 0
# countR = 0
# countStr = 0
# i = 0
# for iterat in range(500):
#     while i <= len(x):
#         if(x[0] == "-"):
#             for i in range(len(x)):
#                 if(x[i + 1] == "-"):
#                     countM += 1
#                 else:
#                     break
#
#             i += countM - 1
#         if (x[0] == "<"):
#             countL += 1
#             for i in range(len(x)):
#                 if (x[i + 1] == "<"):
#                     countL += 1
#                 else:
#                     break
#             i += countL - 1
#         if (x[0] == ">"):
#             countR += 1
#             for i in range(len(x)):
#                 if (x[i + 1] == ">"):
#                     countR += 1
#                 else:
#                     break
#             i += countR - 1
#     print(i, countM)
#     i = 0
#
#     if (countM > 0):
#         if(countM >= len(x)):
#             break
#         if(x[countM + 1] == ">"):
#             for i in range(len(x) - countM):
#                 if(x[i + countM] == ">"):
#                     countR += 1
#                 else:
#                     arr[iterat] = x[countM + countR:]
#                     print("T")
#                     x = x - x[countM + countR:]
#                     continue
#         i += 1
#
# print(arr)

countM = 0
countR = 0
countL = 0

arr = [""] * 200
x = input()
for p in range(100):
    i = 0
    if(x):
        if(x[0] == "-"):
            for i in range(len(x)):
                if(x[i] == "-"):
                   countM += 1

            count = 0


            while count != countM:
                arr[p] += x[:1]
                x = x[1:]
                count += 1


            for i in range(len(x)):
                if(x[i] == ">"):
                   countR += 1

            count = 0
            while count != countR:
                arr[p] += x[:1]
                x = x[1:]
                count += 1
            print(arr[p])
        #####
        else:
            for i in range(len(x)):
                if (x[i] == "<"):
                    countL += 1

            count = 0

            while count != countL:
                arr[p] += x[:1]
                x = x[1:]
                count += 1

            for i in range(len(x)):
                if (x[i] == "-"):
                    countM += 1

            count = 0
            while count != countM:
                arr[p] += x[:1]
                x = x[1:]
                count += 1
            print(arr[p])
            break
    countM = 0
    countR = 0
    countL = 0
# print(arr[0])
# print (''.join(arr))