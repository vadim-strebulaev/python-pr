import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets

z = pd.DataFrame(datasets.load_wine().data)
print(z[0],z[1],z[2])
#1 - вывести 3d график первых 3-х столбцов
figure = plt.figure(1, figsize = (6, 6))
plt.clf()
ax = figure.add_subplot(projection = '3d')
plt.cla()
ax.scatter(z[0], z[1], z[2],color = (1,0,0))
plt.show()

#2 - вывести 2d график значений всех столбцов
figure = plt.figure(1, figsize = (6, 6))
plt.clf()
plt.cla()
plt.plot(z)
plt.show()

#3 - вывести коррелирующую матрицу по всей таблице
figure = plt.figure(1, figsize = (6, 6))
plt.clf()
plt.cla()
corr_matrix = z.corr()
print(corr_matrix)
sns.heatmap(corr_matrix)
plt.show()



#ВАРИАНТ МАКСИМА ЕВГЕНЬЕВИЧА

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from mpl_toolkits.mplot3d import Axes3D

# 1 изобразить данные в двумерной плоскости(первые 2 столбца)
p1 = datasets.load_wine()
X = p1.data
y = p1.target
plt.plot(X[y == 0, 0], X[y == 0, 1], 'bo')
plt.plot(X[y == 1, 0], X[y == 1, 1], 'go')
plt.plot(X[y == 2, 0], X[y == 2, 1], 'ro')
plt.show()
# 2 изобразить график распределения каждого столбца, а также в boxplot
df = pd.DataFrame(X)
sns.distplot(df[0])
sns.boxplot(data=df[0], orient="h")
plt.show()

# 3 изобразить корреляционную матрицу по всей таблице
corr_matrix = df.corr()
sns.heatmap(corr_matrix)
plt.show()