a = list(map(int, input().split()))
b = int(input()) - 1
max = 0
for i in range(len(a) - b):
    sum = 0
    t = i + 1
    for n in range(i, t + b):
        sum += a[n]
    if(sum >= max):
        max = sum
        sum = i
print(max)
# a = list(map(int, input().split()))
# narushenie = 0
# if len(a) == 1:
#     print("true")
# else:
#     for i in range(len(a) - 1):
#         if a[i + 1] <= a[i]:
#             narushenie += 1
#             if i < len(a) - 3:
#                 if a[i + 2] <= a[i]:
#                     narushenie += 1
#     if narushenie > 1:
#         print("false")
#     else:
#         print("true")

# upSpeed = int(input())
# downSpeed = int(input())
# desiredHeight = int(input())
#
# days = int((-(desiredHeight - upSpeed)/(upSpeed - downSpeed)) // 1)
# if days > 0:
#     print(1)
# else:
#     print(-days + 1)