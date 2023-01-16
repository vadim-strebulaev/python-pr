import numpy as np
import pandas
data = pandas.read_csv(filepath_or_buffer='C:\\Users\\Вадим\\Desktop\\Титаник.csv')
countMale = data.groupby(["Sex"])["Sex"].count()["male"]
countSurv = data.groupby(["Survived"])["Survived"].count()[1]
SurvProp = countSurv / (891 / 100)
countClassTwo = data.groupby(["Pclass"])["Pclass"].count()[2]
ClassTwoProp = countClassTwo / (891 / 100)
Ages = data["Age"]
SumAge = 0
countAges = 0
arrAge = [0] * 891
for i in range(len(Ages)):
    if str(Ages[i]) == "nan":
        SumAge = SumAge
    else:
        if(Ages[i] == 0):
            arrAge.pop()
        else:
            arrAge[i] = Ages[i]
        SumAge += Ages[i]
        countAges += 1
arrAge.sort()
for p in range(len(arrAge)):
    if(arrAge[0] == 0):
        arrAge.remove(0)
    else:
        break
print(countMale, SurvProp, ClassTwoProp, SumAge / countAges, arrAge[len(arrAge) // 2])
#1 для заданной таблицы вывести на экран последние 2 столбца
dataS = data[data.columns[len(data.columns) - 2]] + data[data.columns[len(data.columns) - 1]]
print(dataS)
#2 вывести 1 столб - age, 2 - fair среднее и медиану
print("------------")

NewData = {"Медиана":[data['Age'].median(), data['Age'].mean()], "Среднее": [data['Fare'].median(), data['Fare'].mean()]}
ND = pandas.DataFrame(NewData).T
print(ND)
