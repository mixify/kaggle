import pandas as pd
import math
import itertools


atr = dict()
feat = []

num_attr = int(input())
thres = float(input())
num_rows = int(input())

full = input()
l= full.split()
for line in l:
    for i in range(num_rows):
        word = line.split(',')
        all_attr_len = len(word)
        feat.append([])
        for w in word:
            attr_val = w.split('=')
            attr = attr_val[0]
            if(i==0):
                atr.setdefault(attr,[])
            val = attr_val[1]
            atr[attr].append(val)


df = pd.DataFrame(atr)
# df = df.apply(pd.value_counts).fillna(0)

comb = itertools.combinations(df.columns,num_attr)

for c in comb:
    # print(c)
    mt = pd.melt(df, id_vars=c)
    total_len = len(mt)
    # print(mt)
    res = mt.groupby(c)
    for grp in res:
        if(len(grp[1])/total_len >= thres):
            rs = ''
            for key in c:
                rs += key+'='+str(grp[1].iloc[0][key])+','
                # print(rs)
            rs = rs[:-1]
            print(rs)

