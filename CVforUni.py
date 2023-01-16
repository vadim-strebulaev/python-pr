import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import sns as sns
from mpl_toolkits.mplot3d import Axes3D
import ipywidgets

coins = pd.read_csv(filepath_or_buffer='C:\\Users\\Вадим\\Documents\\coins.csv')
#print(coins)


# 1
# symbols = coins.symbol
# coins_count = [symbols[1]]
# flag = True
# for i in range(len(symbols)):
#     for j in range(len(coins_count)):
#         if symbols[i] == coins_count[j]:
#             flag = False
#             break
#     if flag:
#         coins_count.append(symbols[i])
#     flag = True
# print(coins_count)
# print(len(coins_count))


# # 4
# prices = coins.price
# maxP = max(prices)
# for i in range(len(prices)):
#     if prices[i] == maxP:
#         print(coins.symbol[i],coins.date[i])


# большая 2
def plot_fancy_price_action(coins, symbol, start_date, end_date):
    new = coins
    startDate = start_date
    finishDate = end_date
    figure = plt.figure(1, figsize = (10, 10))
    needCoin = symbol
    olds = int(str(startDate)[0:4])*365 + int(str(startDate)[5:7])*365/12 + int(str(startDate)[8:10])
    news = int(str(finishDate)[0:4])*365 + int(str(finishDate)[5:7])*365/12 + int(str(finishDate)[8:10])
    l = 0
    for i in range(len(new)):
        l = int(str(new.date[i])[0:4])*365 + int(str(new.date[i])[5:7])*365/12 + int(str(new.date[i])[8:10])
        new.date[i] = l
    new = coins[coins.symbol == needCoin] # оставляет тольк строки где название монеты совападает с нужным нам названием
    new = new[new.date >= olds]
    new = new[new.date <= news]
    plt.plot(new['date'], new['price'])
    plt.show()
    return
plot_fancy_price_action(coins=coins, symbol='VERI', start_date='2013-06-01', end_date='2019-06-30')
