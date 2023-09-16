# -*- coding: utf-8 -*-
"""DM1.4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t-RTtXJ3SkMV6T_fgLja8toDfSOJQRdh
"""



import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
import scipy.io
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn import metrics
def purity_score(y_true, y_pred):
    contingency_matrix = metrics.cluster.contingency_matrix(y_true, y_pred)
    return np.sum(np.amax(contingency_matrix, axis=0)) / np.sum(contingency_matrix)

mat = scipy.io.loadmat('cstr.mat')
fea=pd.DataFrame(mat['fea'])
gnd=pd.DataFrame(mat['gnd'])
gmm=GaussianMixture(n_components=3, random_state=0).fit(fea)
labels = gmm.predict(fea)
plt.scatter(np.array(fea.iloc[:,1]),np.array(fea.iloc[:,2]),c=labels, s=40, cmap='viridis')
plt.title('CSTR')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
acc=accuracy_score(gnd,labels)
print("CSTR: accuracy for GMM :",acc)
purity=purity_score(gnd,labels)
print("CSTR: purity for GMM :",purity)



mat1 = scipy.io.loadmat('COIL20.mat')
fea1=pd.DataFrame(mat1['fea'])
gnd1=pd.DataFrame(mat1['gnd'])
gmm=GaussianMixture(n_components=3, random_state=0).fit(fea1)
labels1= gmm.predict(fea1)
plt.scatter(np.array(fea1.iloc[:,1]),np.array(fea1.iloc[:,2]),c=labels1, s=40, cmap='viridis')
plt.title('COIL20')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
acc1=accuracy_score(gnd1,labels1)
print("COIL20: accuracy for GMM :",acc1)
purity1=purity_score(gnd1,labels1)
print("COIL20: purity for GMM :",purity1)



mat2 = scipy.io.loadmat('k1b.mat')
X=pd.DataFrame(mat2['X'])
Y=pd.DataFrame(mat2['Y'])
y=pd.DataFrame(mat2['y'])
gmm=GaussianMixture(n_components=10, random_state=0).fit(X)
labels2= gmm.predict(X)
plt.scatter(np.array(X.iloc[:,1]),np.array(X.iloc[:,2]),c=labels2, s=40, cmap='viridis')
plt.title('k1b')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
acc2=accuracy_score(y,labels2)
print("k1b: accuracy for GMM :",acc2)
purity2=purity_score(y,labels2)
print("k1b: purity for GMM :",purity2)


mat3 = scipy.io.loadmat('re0.mat')
X1=pd.DataFrame(mat3['X'])
Y1=pd.DataFrame(mat3['Y'])
y1=pd.DataFrame(mat3['y'])
gmm=GaussianMixture(n_components=3, random_state=0).fit(X1)
labels3= gmm.predict(X1)
plt.scatter(np.array(X1.iloc[:,1]),np.array(X1.iloc[:,2]),c=labels3, s=40, cmap='viridis')
plt.title('re0')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
acc3=accuracy_score(y1,labels3)
print("re0: accuracy for GMM :",acc3)
purity3=purity_score(y1,labels3)
print("re0: purity for GMM :",purity3)