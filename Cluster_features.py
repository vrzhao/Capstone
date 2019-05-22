# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 06:08:51 2019

@author: Vincent Zhao
"""

cluster1 = 25222
cluster2 = 25630
cluster3 = 25993

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

a = list(set(EV['Account Number']))
b = list(set(Unknown['Account Number']))

t = a + b
z = [cluster1,cluster2,cluster3]

acct = pd.concat([EV,Unknown])

matrix = np.zeros((len(z),len(t)))
#matrix = np.zeros((len(a),len(a)))

#for i, x in zip(a,range(0,len(a))):
for i, x in zip(z,range(0,len(z))):
    for j, y in zip(t,range(0,len(t))):
        q = acct[acct['Account Number']==i].sort_values(['Account Number','Conv_date','Hour'],ascending = [1,1,1])['value']
        p = acct[acct['Account Number']==j].sort_values(['Account Number','Conv_date','Hour'],ascending = [1,1,1])['value']

        matrix[x][y] = dtw(np.asarray(q[0:167]),np.asarray(p[0:167]))

        
classification = [1]*len(a) + [0] * len(b)

data = np.concatenate((matrix, [classification]), axis = 0)

dataset = pd.DataFrame({'Account Number':t, 'c1':data[0,:],'c2':data[1,:],'c3':data[2,:],'label':np.int_(data[3,:])})


dataset.to_csv("cluster_factors.csv")


print("--- %s seconds ---" % (time.time() - start_time))




















