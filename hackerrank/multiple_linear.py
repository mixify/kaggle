import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

in_str = input()
F = int(in_str.split()[0])
N = int(in_str.split()[1])
X_train = []
Y_train = []
for i in range(N):
    in_str = input()
    datas = in_str.split()
    X_train.append([])
    for j in range(F):
        X_train[i].append(float(datas[j]))
    Y_train.append(float(datas[-1]))

# print(X_train)
# print(Y_train)

X_train = np.array(X_train)
Y_train = np.array(Y_train)
# print(X_train)
# print(Y_train)
lm = LinearRegression()
model = lm.fit(X_train,Y_train)

predict_num = int(input())
X_test = []
for i in range(predict_num):
    in_str = input()
    datas = in_str.split()
    X_test.append([])
    for j in range(F):
        X_test[i].append(float(datas[j]))

res = lm.predict(X_test)
for r in res:
    print(r)
