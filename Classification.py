# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:01:32 2019

@author: Vincent Zhao
"""

from sklearn.ensemble import RandomForestClassifier

import pandas as pd
import numpy as np

df = pd.read_csv("data_wealth.csv")
df = df.drop(columns = 'Unnamed: 0')

#df = df.drop(columns = 'c1')
#df = df.drop(columns = 'c2')
#df = df.drop(columns = 'c3')
#df = df.drop(columns = 'rate')
#df = df.drop(columns = 'Max')
#df = df.drop(columns = 'Min')
#df = df.drop(columns = 'Mean')
df = df[['c1','c2','c3','label']]

X = df.drop(['label'], axis=1)
y = df['label']

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=1)


#from sklearn.preprocessing import OneHotEncoder
#
#categoricalvars = ['rate','Index']
#ohe = OneHotEncoder(sparse = False, dtype = int,handle_unknown='ignore')
#
#Xcat = pd.DataFrame(ohe.fit_transform(Xtrain[categoricalvars]), columns = ohe.get_feature_names(), index = Xtrain.index)
#
#Xtrain = pd.concat([Xtrain,Xcat], axis = 1)
#
#Xtrain = Xtrain.drop(['rate','Index'], axis = 1)

rf = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=1)

rf.fit(Xtrain, ytrain)

#Xtcat = pd.DataFrame(ohe.transform(Xtest[categoricalvars]), columns = ohe.get_feature_names(), index = Xtest.index)
#
#Xtest = pd.concat([Xtest,Xtcat], axis = 1)
#
#Xtest = Xtest.drop(['rate','Index'], axis = 1)


ypred = rf.predict(Xtest)

from sklearn import metrics
print (metrics.accuracy_score(ytest, ypred))
print (metrics.confusion_matrix(ytest, ypred))
print (metrics.classification_report(ytest, ypred))


print(rf.feature_importances_)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr')

lr.fit(Xtrain, ytrain)

ypred = lr.predict(Xtest)

from sklearn import metrics
print (metrics.accuracy_score(ytest, ypred))
print (metrics.confusion_matrix(ytest, ypred))
print (metrics.classification_report(ytest, ypred))

print(lr.predict_proba(Xtest))
















