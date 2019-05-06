import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import os

df = pd.DataFrame();

ft = []
pred = []
price = []

s1 = input()
lis = s1.split()
F = int(lis[0])
N = int(lis[1])
for i in range(N):
    feature = input()
    data = feature.split()
    ft.append([])
    for j in range(F):
        # feature_str = 'f'+str(j+1)
        ft[i].append(float(data[j]))
    price.append(float(data[F]))

T = int(input())
for i in range(T):
    feature = input()
    data = feature.split()
    pred.append([])
    for j in range(F):
        pred[i].append(float(data[j]))


poly1 = PolynomialFeatures(degree=1)
poly2 = PolynomialFeatures(degree=2)
poly3 = PolynomialFeatures(degree=3)

X1 = poly1.fit_transform(ft)
X2 = poly2.fit_transform(ft)
X3 = poly3.fit_transform(ft)

predict1 = poly1.fit_transform(pred)
predict2 = poly2.fit_transform(pred)
predict3 = poly3.fit_transform(pred)

clf1 = LinearRegression()
clf1.fit(X1,price)
clf2 = LinearRegression()
clf2.fit(X2,price)
clf3 = LinearRegression()
clf3.fit(X3,price)

# print(clf1.predict(predict1))
# print('0000')
# print(clf2.predict(predict2))
# print('0000')
for val in clf3.predict(predict3):
    print(val)
######

# T = input()
# for i in range(T):

