import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def MSE(y,x):
    sum = 0
    for i in range(len(y)):
        sum+=(y[i]-x[i])**2
    return sum/len(y)

def solve():
    N = int(input())
    gpa_string = input().split()
    GPA = [float(s) for s in gpa_string]
    # print(GPA)
    GPA_mean = sum(GPA)/len(GPA)
    GPA_std = np.std(GPA)
    # print(GPA_mean,GPA_var)
    # test = []
    mean_error = 99999999
    mean_idx = 1
    for i in range(1,6):
        p_str = input().split()
        # test.append([])
        test = [float(v) for v in p_str]
        test_mean = sum(test)/len(test)
        test_std = np.std(test)
        # lambda x :
        transformed = [GPA_mean + (x-test_mean)*(GPA_std/test_std) for x in test]
        # print(transformed)
        error = MSE(GPA,transformed)
        # print(error)
        if(error < mean_error):
            mean_idx = i
            mean_error = error
        # test = np.array(test).reshape(-1,1)
        # print(test)
        # clf = LinearRegression()

        # clf.fit(test,GPA)
        # pred = clf.predict(test[i])
    print(mean_idx)
        # print(pred)
    # print(test)
T = int(input())
for i in range(T):
    solve()

