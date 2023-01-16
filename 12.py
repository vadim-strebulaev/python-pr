#дз
path = "C:\\Users\\Вадим\\Downloads\\Telegram Desktop\\17.txt"
file = open(path)
A = []
for x in file:
    A.append(int(x))
print(A)
#1
max = -10000
count = 0
for i in range(len(A) - 1):
    if(A[i] % 3 == 0 or A[i + 1] % 3 == 0):
        if A[i] + A[i + 1] > max:
            max= A[i] + A[i + 1]
        count += 1
print(count, max)
#2
a = A
max = 0
p = 7
d = 160
count = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] % d != a[j] % d) and ((a[i] % p == 0) or (a[j] % p == 0)):
            count += 1
            if(a[i] + a[j] > max):
                max = a[i] + a[j]
print(count, max)
#3
count = 0
max = -10000
for i in range(len(a) - 2):
    x = abs(a[i])
    y = abs(a[i + 1])
    z = abs(a[i + 2])
    b = [x, y, z]
    b.sort()
    if(b[0] ** 2 + b[1] ** 2 < b[2] ** 2 and b[0] + b[1] > b[2]):
        count += 1
        if(b[0] + b[1] + b[2] > max):
            max = b[0] + b[1] + b[2]
print(count, max)
#4
max = -10000
count = 0
c = 0
sum = 0
for i in range(len(a)):
    if(a[i] % 2 == 0):
        sum += 1
        c += 1
f = sum / c

for i in range(len(a) - 1):
    if(a[i] % 3 == 0 or a[i + 1] % 3 == 0 and a[i] < f or a[i + 1] < f):
        if a[i] + a[i + 1] > max:
            max = a[i] + a[i + 1]
        count += 1
print(count, max)
#5
count += 1
for i in range(len(a)):
    for j in range(i, len(a)):
        if(a[i] + a[j] % 7 == 0):
            count += 1
            if(max < a[i] + a[j]):
                max = a[i] + a[j]
print(count, max)
