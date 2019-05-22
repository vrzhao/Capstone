
import numpy as np
import pandas as pd

from tslearn.metrics import dtw
import time

start_time = time.time()

EV = pd.read_csv("Cb_EV_Customer_FY18_Usage.csv")
EV = EV[EV['Month'] == 1]

jan = EV.drop(['rate','Month','Weekday'], axis = 1)

df = pd.melt(jan, id_vars=['Account Number', 'Conv_date'], var_name='Hour')

a = set(df['Account Number'])

matrix = np.zeros((len(a),len(a)))

for i, x in zip(a,range(0,len(a))):
    for j, y in zip(a,range(0,len(a))):
        q = df[df['Account Number']==i].sort_values(['Account Number','Conv_date','Hour'],ascending = [1,1,1])['value']
        p = df[df['Account Number']==j].sort_values(['Account Number','Conv_date','Hour'],ascending = [1,1,1])['value']
        
        t = np.asarray(q[0:167])
        r = np.asarray(p[0:167])
        
        matrix[x][y] = dtw(t,r)
        
        
z = np.copy(matrix)
np.fill_diagonal(z, np.inf)

np.savetxt("EV_Similarity_Matrix.csv", matrix, delimiter=",")

print("--- %s seconds ---" % (time.time() - start_time))
