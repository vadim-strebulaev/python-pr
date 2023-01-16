import TgBotFormula


# x = int(input())
# y = int(input())
# max = 0
# i = max(x, y)
# print(i)
# while i > 2:
#     if x % i == 0 and y % i == 0:
#         max = i
#         break
#     i += 2
# print(i)
#####
# for i in range(1001, 5000, 2):
#     a = 1
#     count = 0
#     while y <= int(x ** 0.5) + 1:
#         if x % a == 0:
#             count += 1
#             if x % (x // a) == 0:
#                 count += 1
#         a += 1
#         if(count > 2):
#             break
#     if(count == 2):
#         print(x)

####
# x = float(input())
# if (x % 1 == 0 and x > 0):
#     print("натуральное")
# else:
#     print("нет")
# #####
# for x in range(1000, 5000, 1):
#     y = x ** 0.5
#     z = 0
#     if y % 1 == 0:
#         z += 1
# print(z)


#
# delitel = 0
# colichestvoDelitelei = 3
# nachaloDiaposona = 174457
# konecDiaposona = 17450600
# for i in range(nachaloDiaposona, konecDiaposona):
#     count = 0
#     for n in range(2, int(i ** 0.5)):
#         if i % n == 0:
#             count += 1
#             if i % (i // n) == 0:
#                 count += 1
#     if(count == 2):
#         print(n, i // n)
#1
# maxi = 0
# for i in range(286564, 287271):
#     count = 0
#     for n in range(2, int(i ** 0.5) + 1):
#         if i % n == 0:
#             if count == 0:
#                 min = n
#             count += 2
#             maxdiv = n
#     if count > maxi:
#         maxi = count
#         max = i // min
# maxi += 2
# print(maxi, max)
#
# #2
# for i in range(87921, 88188):
#     sum = 0
#     proiz = 1
#     while i != 0:
#         sum += i % 10
#         proiz *= i % 10
#         i //= 10
#     if (proiz % 18 == 0 and proiz != 0):
#         if(sum % 14 == 0):
#             print(sum, proiz)
#
# #3
# count = 1
# for i in range(245690, 245756):
#     for n in range(2, i):
#         if (i % n == 0):
#             break
#         if(n == i - 1):
#             print(count, i)
#     count += 1
#
# #4
# for count in range(6):
#     for n in range(18, 500001, 10):
#         if number % n == 0:
#             print(number, n)
#             count = count + 1
#             break
#     number = number + 1

#######

# 2
# for i in range(1000, 10001):
#     if int(i ** 0.5) == i ** 0.5:
#         count = -1
#     else:
#         count = 0
#     l = 0
#     k = 0
#     for n in range(2, int(i ** 0.5) + 2):
#         if i % n == 0:
#             count += 2
#             if l == 0:
#                 l = n
#             else:
#                 if k == 0:
#                     k = n
#             if count > 4:
#                 break
#     if count == 4:
#         print(i, i // l, i // k)
# # 3
# count = 0
# k = 0
# l = 0
# for i in range(210235, 210301):
#     k = 0
#     l = 0
#     if int(i ** 0.5) == i ** 0.5:
#         count = -1
#     else:
#         count = 0
#     for n in range(2, int(i ** 0.5) + 1):
#         if i % n == 0:
#             count += 2
#             if k == 0:
#                 k = n
#             elif l == 0:
#                 l = n
#             if count >= 5:
#                 break
#     if count == 4:
#         print(k, l, i // l, i // k)
#
#

#задача класс
# delit1=0
# delit2=0
# for i in range(5,9):
#     del1=0
#     for j in range(2,i//2+1):
#         if(i%j==0):
#             del1 = del1+1
#             delit2=delit1
#             delit1=j
#     if(del1==2):
#         print(delit1,delit2)


#дз




#1
# for i in range(81234000, 134690000):
#     count = 0
#     if i ** 0.5 == int(i ** 0.5):
#         for n in range(2, int(i ** 0.5) + 1 - 1):
#             if i % n == 0:
#                 count += 2
#                 a = n
#     if(count == 2):
#         print(n, int(i ** 0.5), i // n, "у числа", i)




# 2
# for i in range( 154026, 154044):
#     max1 = -99 ** 99
#     count = 0
#     if i ** 0.5 != int(i ** 0.5):
#         for n in range(2, int(i ** 0.5)):
#             if i % n == 0:
#                 count += 2
#                 max1 = i // dil
#     if count == 2:
#         print(i, '-',i, max1,)
# # 3
# i = 150000
# while True:
#     x = 0
#     for n in range(2, int(i ** 0.5) + 1):
#         if n == i ** 0.5:
#             x += n
#         else:
#             if i % n == 0:
#                 x += n + i // n
#     if x % 13 == 10:
#         print(i)
#     else:
#         print('0')
#     i += 1
# # 4
# i = 550000
# while True:
#     x = 0
#     count = 0
#     for n in range(2, int(i ** 0.5) + 1):
#         if n == i ** 0.5:
#             x += n
#             count += 1
#         else:
#             if i % n == 0:
#                 x += dil + i // n
#                 count += 2
#     if count != 0:
#         y = x // count
#         if y % 31 == 13:
#             print(i)
#         else:
#             print('0')
#     else:
#         print('0')
#     i += 1
#
#
# #5
# count = 0
# for i in range(2000000, 1000001, -2):
#     c = 0
#     for n in range(int(i ** 0.5) + 1, 2, -1):
#         if i % n == 0:
#             if i // n - n <= 100:
#                 c += 1
#             if c == 3:
#                 break
#     if c == 3:
#         print(i)
#         count += 1
# print(count)
# i = 150000
# while True:
#     S = 0
#     for dil in range(2, int(i ** 0.5) + 1):
#         if dil == i ** 0.5:
#             S += dil
#         else:
#             if i % dil == 0:
#                 S += dil + i // dil
#     if S % 13 == 10:
#         print(i)
#     else:
#         print('', end = "")
#     i += 1

# print("Вы ели шаурму?")
# import math
# sum = 0
# n = 0
# count = 0
# while n != 5000:
#     for i in range(1, n):
#         if n % i == 0:
#             sum += math.factorial(i)
#             count += 1
#         if count == 5:
#             break
#     if sum % 3 == 0 and count == 5:
#         print(n)
#     n += 1
#     sum = 0
#     count = 0


# n = 1000000
# count = 0
# while count != 5:
#     for i in range(2, n ** 0.5, 2):
#         while True:
#             if

# x=int(input())
# for i in range(1,int(x**0.5)+1):
#     if(x%i==0):
#         if (i == x / i):
#             print(i)
#         else:
#             print(i,int(x/i))


#
# for i in range(1,10):
# #     print([[i2 for i3 in range(i2)] for i2 in range(i)])
#
# for i in range(1,10):
#     for i2 in range(i):
#         z=[]
#         for i3 in range(i2):
#             z.append(i2)
#         print(z, end="")
# A = [4,3,5,5,5]
# for i in A:
#     i = i + 1
#     print(i)
# print(A)


# x = int(input())
# a = [0]*50
# count = 0
# while x != 0:
#     a[count] = x
#     for n in a:
#         if(n != 0):
#             print(n, " ", end = "")
#     print("")
#     x = int(input())
#     count += 1

#
# a, count = [5,4,3,2,1], 0
# b = [0] * len(a)
# for i in range(len(a) // 2):a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]; print(a)

# leetcode 905
# n = int(input())
# s = []
# count = 0
# for i in range(n):
#     a = int(input())
#     if a % 2 == 0:
#       s.reverse()
#       s.append(a)
#       s.reverse()
#     else:
#         s.append(a)
#         count -= 1
#     count += 1
# print(s)


# def sortArrayByParity(self, nums):
#     nums = sorted(nums, key=lambda A: random.random())
#     return nums
#
# print(sortArrayByParity(1, [1,2,3,4,35,6,7,8,8,8,89,29,9]))






# from sklearn import datasets
# import pandas as pd
# digits = datasets.load_digits()
# digits = pd.DataFrame([i for i in range(digits)])
# print(digits)