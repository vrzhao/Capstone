# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:48:51 2019

@author: Vincent Zhao
"""

import numpy as np
import pandas as pd

from tslearn.metrics import dtw
import time

start_time = time.time()

EV = pd.read_csv("Cb_EV_Customer_FY18_Usage.csv")
Unknown = pd.read_csv("FY18_All_Usage_Data_With_Month.csv")
EV = EV[EV['Month'] == 1]
Unknown = Unknown[Unknown['Month'] == 1]

jan = EV.drop(['rate','Month','Weekday'], axis = 1)
jan2 = Unknown.drop(['rate','Month','Weekday'], axis = 1)

EV = pd.melt(jan, id_vars=['Account Number', 'Conv_date'], var_name='Hour')
Unknown = pd.melt(jan2, id_vars=['Account Number', 'Conv_date'], var_name='Hour')

print(EV)
print(Unknown)

a = list(set(EV['Account Number']))
b = list(set(Unknown['Account Number']))
z = list(np.random.choice(a,size=30,replace=False))
t = list(np.random.choice(b,size=200,replace=False))

t = t + z
a = set(a) - set(z)

acct = pd.concat([EV,Unknown])

print(acct)

matrix = np.zeros((len(a),len(t)))

for i, x in zip(a,range(0,len(a))):
    print(x)
    for j, y in zip(t,range(0,len(t))):
        q = acct[acct['Account Number']==i].sort_values(['Account Number','Conv_date','Hour'],ascending = [1,1,1])['value']
        p = acct[acct['Account Number']==j].sort_values(['Account Number','Conv_date','Hour'],ascending = [1,1,1])['value']

        matrix[x][y] = dtw(np.asarray(q[0:167]),np.asarray(p[0:167]))

print(matrix)
        
EV = [list(t)[n] for n in np.where(matrix < 5)[1]]

print(set(EV), len(set(EV)))

tp = [i for i in z if i in list(set(EV))]

print(tp, len(tp))

np.savetxt("Similarity_Matrix_type2.csv", matrix, delimiter=",")
np.savetxt("Similarity_Matrix_Users_type2.csv", list(set(EV)), delimiter=",")
np.savetxt("Similarity_Matrix_test_type2.csv", t, delimiter=",")
np.savetxt("Similarity_Matrix_tp_type2.csv", z, delimiter=",")


print("--- %s seconds ---" % (time.time() - start_time))

