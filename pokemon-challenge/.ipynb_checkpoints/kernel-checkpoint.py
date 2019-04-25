from subprocess import check_output

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('a');


print(check_output(["ls","./input"]).decode("utf8"))

data = pd.read_csv('input/pokemon.csv')
print(data.info())
# print(data.corr())
# f,ax = plt.subplots(figsize=(18,18))
# sns.heatmap(data.corr(), linewidths=5, fmt= '.1f',ax=ax)
# plt.show()
##
data.Speed.plot(kind = 'line', color = 'g',label = 'Speed',linewidth=1,alpha = 0.5,grid = True,linestyle = ':')
data.Defense.plot(color = 'r',label = 'Defense',linewidth=1, alpha = 0.5,grid = True,linestyle = '-.')

plt.legend(loc='upper right')     # legend = puts label into plot
plt.xlabel('x axis')              # label = name of label
plt.ylabel('y axis')
plt.title('Line Plot')            # title = title of plot
plt.show()
data.corr()
##
# Scatter Plot
# x = attack, y = defense
data.plot(kind='scatter', x='Attack', y='Defense',alpha = 0.5,color = 'red')
plt.xlabel('Attack')              # label = name of label
plt.ylabel('Defence')
plt.title('Attack Defense Scatter Plot')            # title = title of plot
##

# Histogram
# bins = number of bar in figure
data.Speed.plot(kind = 'hist',bins = 50,figsize = (12,12))
plt.show()

##
data.Speed.plot(kind = 'hist',bins = 50,figsize = (12,12))
plt.clf()
##

d_d = data['Defense']
d_a = data['Attack']
sumad = d_a+d_d
# sorted = sumad.sort_index()
# sorted
##
data['Legendary']
data['Name'][796]
##
data[np.logical_and(data['Defense']>200, data['Attack']>100 )]
##


# Conditionals on iterable
num1 = [5,10,15]
num2 = [i**2 if i == 10 else i-5 if i < 7 else i+5 for i in num1]
print(num2)
##
data["speed_level"] = ['low' if spd < 80 else 'high' for spd in data.Speed]
data.loc[:10,["speed_level","Speed"]]
##
data.columns
data.shape
##
print(data['Type 1'].value_counts(dropna =False))  # if there are nan values that also be counted
print(data['Type 2'].value_counts(dropna =False))  # if there are nan values that also be counted
##
data.describe()

##
# For example: compare attack of pokemons that are legendary  or not
# Black line at top is max
# Blue line at top is 75%
# Red line is median (50%)
# Blue line at bottom is 25%
# Black line at bottom is min
# There are no outliers
data.boxplot(column='Attack',by = 'speed_level')
##
