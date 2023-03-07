import turtle as t
massive = []
file = open("C:\\Users\\Vadim\\Documents\\mass.txt", "r")
while True:
    # считываем строку
    line = file.readline()
    print(line)
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    line.strip()

print(massive)
while True:
    t.goto(-300, -300)
    t.goto(-300, 300)
    

