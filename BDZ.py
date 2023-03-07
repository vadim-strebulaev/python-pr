# # n = str(input())
# # p = [""] * len(n)
# #
# # k = "abcdefghijklmnopqrstuvwxyz"
# # for i in range(len(n)):
# #     for j in range(len(k)):
# #         if n[i] == k[j]:
# #             p[i] = j
# # print(p)
#
# # x=int(input())
# # while(x!=0):
# #     x=int(input())
# #
#
# #1
# # 118
# #2
# # 10
# #3
# # 78
# #4
# # 20
# #5
# # 5
# #6
# # 2
# #7
# # 6
# #8
# # 10
# #9
# # 12
# #10
# # 14
# #11
# # 64
# #12
# #13
# #14
# # 4000
# #15
# # 81
# #16
# # 2^11
# #17
# # 4
# #18
# # 2
# #19
# # 4
# #20
# # 26
# #21
# # 100
# #22
# # 10
# #23
# # 48
# #24
# #25
# #a48 секунд
# #32
# # xyzw
# #33
# # zwyx
# # 34
# x = int(input())
# print(x % 10)
# x //= 10
# print(x % 10)
# #35
# x = input()
# x *= 100
# print(int(x) ** 2)
# #36
# x = int(input())
# a = int(input())
# b = int(input())
# k = a - b
# x = (x - a) // k + 1
# print(x + (x - a) % k)
# #37
# #бяка задача фу нехочу решать
# #38
# a = int(input())
# b = int(input())
# if (a - 1) % (b - a + 1) == 0 and b % (b - a + 1) == 0:
#     print('YES')
# else:
#     print('NO')
# #39
# x1=int(input())
# y1=int(input())
# x2=int(input())
# y2=int(input())
# if(x2 + y2) % 2 == 0 and y1 < y2 and abs(x2 - x1) <= abs(y2 - y1):
#     print('YES')
# else:
#     print('NO')
# #40
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# if(a <= d and b <= e or a <= e and b <= d):
#     print('YES')
# elif (c <= d and b <= e or c <= e and b <= d):
#     print("YES")
# elif(a <= d and c <= e or a <= e and c <= d):
#     print("YES")
# else:
#     print("NO")
#
# #41
# n = int(input())
# x = 0
# y = 0
# while n != 0:
#     y += 1
#     x += n
#     n = int(input())
# print(b / c)
#
#
# #42
# n = int(input())
# max = n
# count = 0
# while n != 0:
#     if n > max:
#         count += 1
#     max = n
# print(count)
#
# #43
# n = int(input())
# ForCount = 1
# count = 0
# x = n
# while n != 0:
#     if x == n:
#         ForCount+=1
#     else:
#         ForCount = 1
#     if ForCount > count:
#         count = ForCount
#     x = n
#     n = int(input())
# print(count)
# #44
# #не хочу делать
#
#

path="C:\\Users\\Vadim\\Downloads\\17 (1).txt"
file=open(path)
A=[]
for x in file:
    A.append(int(x))
B=[]
for i in range(0,len(A)-1):
    if(A[i]+A[i+1])>=100 and (A[i]<0 or A[i+1]<0):
        B.append(A[i]*A[i+1])
print(len(B),max(B))