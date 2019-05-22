# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:58:39 2019

@author: Vincent Zhao
"""

import pandas as pd
import numpy as np

cluster = pd.read_csv("cluster_factors.csv")
cluster = cluster.drop('Unnamed: 0', axis = 1)

unknown = pd.read_csv("FY18_All_Usage_Data_With_Month.csv")

acct = pd.read_csv("MSBA Spring 19/EV Acct Data.csv")
acct = acct[['Account Number','Charger Type']]

acct_list = set(acct[acct['Charger Type']=='Level 2']['Account Number'])

df = pd.read_csv("Cb_EV_Customer_FY18_Usage.csv")

acct_list2 = []

for i in acct_list:
    target = df[df['Account Number'] == i].drop(['Account Number','Conv_date','Weekday','rate'], axis = 1)
    if target.max().max() >= 4:
        acct_list2.append(i)

df = df[df['Account Number'].isin(acct_list2)]

EV = df

raw = pd.concat([EV,unknown])

raw = raw.drop(['Conv_date','Weekday'], axis = 1)

maximum = []

for i in set(raw['Account Number']):
    temp = raw[raw['Account Number'] == i]
    row = [i]
    for j in range(1,13):
        row.extend([temp[temp['Month'] == j].drop(['Account Number','rate','Month'], axis = 1).values.max(),
                        temp[temp['Month'] == j].drop(['Account Number','rate','Month'], axis = 1).values.min(),
                        temp[temp['Month'] == j].drop(['Account Number','rate','Month'], axis = 1).values.mean()])
    maximum.append(row)

raw = raw.drop(['HE01','HE02','HE03','HE04','HE05','HE06','HE07','HE08','HE09','HE10','HE11','HE12','HE13',
                'HE14','HE15','HE16','HE17','HE18','HE19','HE20','HE21','HE22','HE23','HE24'], axis = 1)


raw = raw.groupby(['Account Number']).agg({'rate':'first'}).reset_index()

aggreg = pd.DataFrame(maximum, columns = ['Account Number','Max1','Min1','Mean1','Max2','Min2','Mean2','Max3','Min3','Mean3','Max4','Min4','Mean4','Max5','Min5','Mean5','Max6','Min6','Mean6',
                                          'Max7','Min7','Mean7','Max8','Min8','Mean8','Max9','Min9','Mean9','Max10','Min10','Mean10','Max11','Min1','Mean11','Max12','Min12','Mean12'])


data = aggreg.set_index('Account Number').join(raw.set_index('Account Number'))
data = data.join(cluster.set_index('Account Number'))

data.to_csv("dataset_full.csv")









