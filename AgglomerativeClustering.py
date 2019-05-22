import pandas as pd
import numpy as np

from tslearn.metrics import dtw

EV = pd.read_csv("Cb_EV_Customer_FY18_Usage.csv")
EV = EV[EV['Month'] == 1]

jan = EV.drop(['rate'], axis = 1)

df1 = pd.melt(jan, id_vars=['Account Number', 'Conv_date'], var_name='Hour')

df = pd.read_csv("EV_Similarity_Matrix.csv")
df = np.asarray(df)


from sklearn.cluster import AgglomerativeClustering

clustering = AgglomerativeClustering(n_clusters = 3).fit(df)

a = set(df1['Account Number'])

dic1 = {}
dic2 = {}
dic3 = {}

for i, j in zip(a, clustering.labels_):
    if j == 0:
        dic1[i] = [0]
    if j == 1:
        dic2[i] = [0]
    if j == 2:
        dic3[i] = [0]

a = (list(dic1.keys()))

matrix1 = np.zeros((len(a),len(a)))

for i, x in zip(a,range(0,len(a))):
    for j, y in zip(a,range(0,len(a))):
        q = df1[df1['Account Number']==i].sort_values(['Account Number','Conv_date','Hour'],ascending = [1,1,1])['value']
        p = df1[df1['Account Number']==j].sort_values(['Account Number','Conv_date','Hour'],ascending = [1,1,1])['value']

        matrix1[x][y] = dtw(np.asarray(q[0:167]),np.asarray(p[0:167]))

cmin1 = np.sum(matrix1, axis = 1)
minimum1 = np.argmin(cmin1)
cluster1 = a[minimum1]

#max1 = np.argwhere(matrix1 == np.max(matrix1))
#print(max1[0])
#clustermax1 = a[max1[0][0]]
#clustermin1 = a[max1[0][1]]
#print(clustermax1,clustermin1)

np.savetxt("EV_Cluster1.csv", matrix1, delimiter=",")


a = (list(dic2.keys()))

matrix2 = np.zeros((len(a),len(a)))

for i, x in zip(a,range(0,len(a))):
    for j, y in zip(a,range(0,len(a))):
        q = df1[df1['Account Number']==i].sort_values(['Account Number','Conv_date','Hour'],ascending = [1,1,1])['value']
        p = df1[df1['Account Number']==j].sort_values(['Account Number','Conv_date','Hour'],ascending = [1,1,1])['value']

        matrix2[x][y] = dtw(np.asarray(q[0:167]),np.asarray(p[0:167]))

cmin2 = np.sum(matrix2, axis = 1)
minimum2 = np.argmin(cmin2)
cluster2 = a[minimum2]

#max2 = np.argwhere(matrix2 == np.max(matrix2))
#print(max2[0])
#clustermax2 = a[max2[0][0]]
#clustermin2 = a[max2[0][1]]
#print(clustermax2,clustermin2)

np.savetxt("EV_Cluster2.csv", matrix2, delimiter=",")

a = (list(dic3.keys()))

matrix3 = np.zeros((len(a),len(a)))

for i, x in zip(a,range(0,len(a))):
    for j, y in zip(a,range(0,len(a))):
        q = df1[df1['Account Number']==i].sort_values(['Account Number','Conv_date','Hour'],ascending = [1,1,1])['value']
        p = df1[df1['Account Number']==j].sort_values(['Account Number','Conv_date','Hour'],ascending = [1,1,1])['value']

        matrix3[x][y] = dtw(np.asarray(q[0:167]),np.asarray(p[0:167]))

cmin3 = np.sum(matrix3, axis = 1)
minimum3 = np.argmin(cmin3)
cluster3 = a[minimum3]

#max3 = np.argwhere(matrix3 == np.max(matrix3))
#print(max3[0])
#clustermax3 = a[max3[0][0]]
#clustermin3 = a[max3[0][1]]
#print(clustermax3,clustermin3)


print(cluster1)
print(cluster2)
print(cluster3)


np.savetxt("EV_Cluster3.csv", matrix3, delimiter=",")












