# задача
#
#
# x = int(input())
# for i in range(x):
#     print("начался бег", i + 1, "большого круга")
#     print("стрельба началась")
#     y = int(input())
#     for t in range(y):
#         print("бегу", t + 1, "маленький круг")
#         y -= 1
# a = 82 // 3 ** 2 % 7
# print(a)

#задача

# x = 0
# y = 0
# z = 0
# days = 0
# while x != 23 and z == 59 and y == 59:
#     z += 1
#     if(z == 60):
#         y += 1
#         z = 0
#     if(y == 60):
#         x += 1
#         y = 0
#     if(x == 24):
#         days += 1
#         x = 0
#     print(days, ":", x, ":", y, ":", z, sep = "")


#acmp
# max = 0
# maxind = 0
#
# n = int(input())
#
# a = []
# a = list(map(int, input().split()))
# l, r = map(int, input().split())
#
# for i in range(l - 1, r):
#     if a[i] > max:
#         max = a[i]
#         maxind = i + 1
#         break
# print(max, maxind)
#
# count = 0
# n = int(input())
# a = []
# a = list(map(int, input().split()))
# l = int(input())
# for i in range(len(a)):
#   if a[i] == l:
#    	count += 1
#
# print(count)


#
# n = input()
# a = list(map(int, input().split()))
# n = min(a)
# k = max(a)
# for i in range(len(a)):
#     if (a[i] == k):
#         a[i] = n
# for i in range(len(a)):
#     print(a[i], end = " ")

#
# n = input()
# a = list(map(int, input().split()))
# maks = 0
# o = 0
# t = 0
# f = 0
# def three(a,b,c):
#     return a + b + c
# for i in range(len(a)):
#     o = (i - 1) % len(a)
#     t = i % len(a)
#     f = (i + 1) % len(a)
#     if(three(a[o], a[t], a[f]) > maks):
#         maks = a[o] + a[t] + a[f]
# print(maks)

#
# n = int(input())
# a = list(map(int, input().split()))
# l = int(input())
# min = 0
# max = 0
# a.sort()
# for i in range(len(a)):
#     if(a[i] < l and a[i] > min):
#         min = a[i]
#     if(a[i] > l):
#         max = a[i]
#         break
# if(max - l >= l - min):
#     print(max)
# else:
#     print(min)

#ЗАДАЧА №149acmp
# input()
# a = list(map(int, input().split()))
# for i in reversed(a):
#     print(i, end = " ")



#1 ljvfirf
#x/d=l



# if(d==x//d):
#     count+=1
# else:
#     count+=2


# for i in range(81239, 134689+1, 1):
#     countj = 0
#     for j in range(2, int(i**0.5)+1, 1):
#         if i%j==0:
#             if j == i//j:
#                 b = j
#                 countj += 1
#             else:
#                 a = j
#                 c = i//j
#                 countj = countj + 2
#     if countj==3:
#         print(i, a, b, c)


#5
# x=int(input())
# for i in range(1,x//2):
#     if(x%i==0):
#         print(i,x//i)
# for i in range(1000000,2000000):


# x=int(input())
# cold=0
# for i in range(1,int(x**0.5)+1):
#     if(x%i==0):
#         if i==x//i:
#             print(i)
#             cold+=1
#         else:
#             print(i,x//i)
#             cold+=2
#
# print(cold)


# for i in range(1000000,2000000):
#     count=0
#     for j in range(1,int(i**0.5)+1):
#         if(i%j==0):
#             if(i/j-j<100):
#                 count+=1
#                 if(count==3):
#                     break
#         if(count>3):
#             print(i)
#$&

for i in range(289_123_456, 389_123_456, 1):
    count = 0
    if i**0.5 == int(i**0.5):
        for j in range(2, int(i**0.5) + 1):
            if i%j==0:
                if j==i//j:
                    count += 1
                else:
                    count +=2
                if count > 3:
                    break
        if count == 3:
            print(i)