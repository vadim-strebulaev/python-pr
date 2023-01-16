# прога
# 10
for x in range(44):
    a = 44 ** 3 + x * 44 ** 2 + 2 * 44 + 3 # первая часть выражения
    b = 44 ** 3 * 3 + 44 ** 2 * 2 + x * 44 + 1 # вторая часть выражения
    if (a + b) % 42 == 0: # скадываем обе части и проверяем деление на 42
        max = (a + b) // 42 #в максимум записываем число которое кратно 42 и подходит в выражение
print(max) # выводим максимум
# 10140
print("---")

# 11
n = 0
flag = 0
while flag != 1:
    for x in range(13):
        for y in range(13):
            a = 2 * 15 ** 5 + y * 15 ** 4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 + 5 # первая часть выражения
            b = 6 * 13 ** 4 + 7 * 13 ** 3 + x * 13 ** 2 + 9 * 13 + y # вторая часть выражения
            if (a + n) % b == 0: # ищем минимальное число, которому кратна сумма
                print(n)
                flag = 1
    n = n + 1
# 1535
print("---")

# 12
x = 0
sum = 0
while sum != 71:
    a = []
    A = 64 ** 11 - 4 ** 10 + 96 - x
    sum = 0
    while A > 0:
        a.append(A % 4)
        A = A // 4
    for i in range(len(a)):
        sum = sum + a[i]
    x = x + 1
else:
    x -= 1
    print(x)
# 16
print("---")

# 13
A = 4*25**4 - 5**4 + 14
a = []
sum = 0
while A > 0:
    a.append(A % 5)
    A = A // 5
for i in range(len(a)):
    sum = sum + a[i]
print(sum)
# 25


A = 2*27**7 + 3**10 - 9
a = []
count = 0

while A > 0:
    a.append(A % 3)
    A = A // 3
for i in range(len(a)):
    if a[i] == 0:
        count = count + 1
print(count)
# 13
print("---")

# 14
a = []
for i in range(0, 30, 2):
    for n in range(1, 30, 2):
        N = (2 ** i) * (3 ** n)
        if 150000000 <= N <= 300000000:
            a.append([N, i + n])
            break
a.sort()
for i in range(len(a)):
    print(*a[i])
# 181398528 21
# 201326592 27
# 229582512 19
# 254803968 25
print("---")

# 15
for C in range(326496, 649632):
    count2 = 0
    count1 = 0
    for divisor in range(2, int(C ** 0.5)):
        if C % divisor == 0:
            div1 = C // divisor
            div2 = divisor
            if div1 % 2 == 0:
                count2 = count2 + 1
            else:
                count1 = count1 + 1
            if div2 % 2 == 0:
                count2 = count2 + 1
            else:
                count1 = count1 + 1
    if count2 == count1 and count1 >= 70:
        print(C, end=' ')
        for div in range(1000, C):
            if C % div == 0:
                print(div)
                break
# 450450 1001
# 589050 1050
# 630630 1001
print("---")

# 16
a = []
for i in range(159264873, 973146286):
    if i ** 0.5 == int(i ** 0.5):
        a.append(i)
print(a)
for i in range(1, len(a) + 1, 2000):
    print(a[i], end=' ')
    count = -1
    for divisor in range(2, int(a[i]**0.5) + 1):
        if a[i] % divisor == 0:
            count = count + 2
    print(count)
# 159314884 7
# 213802884 25
# 276290884 7
# 346778884 7
# 425266884 79
# 511754884 7
# 606242884 25
# 708730884 187
# 819218884 25
# 937706884 25
print("---")


