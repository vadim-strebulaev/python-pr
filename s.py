x = 16
y = 23
z = 4
a = 12
b = 32
c = 6
n = int(input())
b = ''
while n > 0:
    b = str(n % 4) + b
    n = n // 4
    print(b)