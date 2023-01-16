import pandas as pd   # библиотека для обработки и анализа данных. Зачастую работает вместе с библиотекой numpy
import numpy as np    # библиотека по работе с многомерными массивами и мат. функциями
import matplotlib.pyplot as plt # библиотека для визуализации данных
import sns as sns # так же библиотека для визуализации данных. Построена на основе библиотеки matplotlib
from sklearn import datasets # библиотека по машинному обучению. Здесь мы берем datasets(помогает загрузить базу данных с определённого сайта)

#это вам 100% нужно
z = datasets.load_iris() # в переменную z загружаем датасет iris
from mpl_toolkits.mplot3d import Axes3D # библиотека расширяет функционал для построения 3d осей
print("------------------------------------", "\n", z, "\n", "------------------------------------") # вывод датасета
x = z.data # теперь x равен части data из таблицы z
y = z.target # теперь y равен части target из таблицы z



#это вам тоже очень нужно 3D график
figure = plt.figure(1, figsize = (6, 6))# переменная figure теперь равна (plt.figure - создание фигуры)P.S. присваиваем переменной фигуру, которая равна 0,
# где "1" - номер фигуры, а размеры фигуры - 6 * 6
plt.clf() #отчистка текущей фигуры
ax = figure.add_subplot(projection = '3d')# вероятно это рисование осей(C документации: "Добавьте оси к текущей фигуре или извлеките существующие оси.")
plt.cla() #отчистка осей
colors = list(map(lambda x: (1, 0, 0) if x == 0 else ((0, 1, 0) if x == 1 else (0, 0, 1)), y)) # если цвет ириса 0 - то цвет красный,
# если цвет ириса 1 - то цвет зеленый, если цвет ириса 2 - то цвет синий
ax.scatter(x[:, 0], x[:, 1], x[:, 2], color = colors) # вероятно придача цветам значений
plt.show() # показ графика


# это вам нужно - 2d график
figure = plt.figure(1, figsize=(6, 6))# переменная figure теперь равна (plt.figure - создание фигуры)P.S. присваиваем переменной фигуру, которая равна 0,
# где "1" - номер фигуры, а размеры фигуры - 6 * 6
plt.clf() #отчистка текущей фигуры
ax = figure.add_subplot() # рисование осей 2d
# придача цветов координатам(данным на графике)
colors = []
for i in y:
    if i == 2:
        colors.append((0,0,1))
    elif i==1:
        colors.append((0,1,0))
    else:
        colors.append((1,0,0)) # вот перевод строки с циклом и ифами в нормальный вид
ax.scatter(x[:, 0], x[:, 1], color=colors)# вероятно придача цветам значений
plt.show() # показ графика



# это вам не очень нужно - 3d график с 2d поскостью - это нужно только тем, кто шарит
from sklearn.decomposition import PCA # *на сколько я понял* библиотека помогает переформатировать график из 3d в 2d
pca = PCA(n_components=2) # уменьшает количество измерений данных P.S. сам в шоке и нихера не понял
xpca = pca.fit_transform(x) # xpca - уже уменьшеное количество осей до 2
figure = plt.figure(1, figsize=(6, 6))# переменная figure теперь равна (plt.figure - создание фигуры), где "1" - номер фигуры, а размеры фигуры - 6 * 6
plt.clf()#отчистка текущей фигуры
ax = figure.add_subplot(projection = '3d')# вероятно это рисование осей
colors = list(map(lambda x: (1,0,0) if x==0 else ((0,1,0) if x==1 else (0,0,1)),y))# если цвет ириса 0 - то цвет красный, если цвет ириса 1 - то цвет зеленый, если цвет ириса 2 - то цвет синий
ax.scatter(xpca[:, 0], xpca[:, 1], color=colors)# вероятно придача цветам значений
plt.show()# показ фигуры
print(x) # выводим часть data из таблицы iris

# это вам совсем не нужно можно не читать
# df = z
# sns.boxplot(n = df.data)
# sns.boxplot(data = df, n = df.data, m = df.target)
# plt.show()