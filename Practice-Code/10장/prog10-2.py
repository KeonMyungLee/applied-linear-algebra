import numpy as np
from numpy.matlib import repmat
import matplotlib.pyplot as plt
from scipy import linalg

C1 = np.array([[2.,3.], [2.,4.], [3.,6.], [4.,1.], [4.,4.]])
C2 = np.array([[6.,8.], [8.,7.], [9.,5.], [9.,10.], [10.,8.]])

mu1 = np.mean(C1, axis=0)
mu2 = np.mean(C2, axis=0)

print("C1의 평균 벡터 =", mu1)
print("C2의 평균 벡터  =", mu2)

S1 = np.cov(C1.T)*(C1.shape[0]-1)
S2 = np.cov(C2.T)*(C2.shape[0]-1)
Sw = S1 + S2
print("C1의 산포 행렬 = ", S1)
print("C2의 산포 행렬 = ", S2)
print("부류 내의 산포 행렬 = ", Sw)

Sb = (mu1 - mu2).reshape(2,1).dot((mu1 - mu2).reshape(1,2))
print("부류 간의 산포 행렬 = ", Sb)

D, U = linalg.eig(linalg.inv(Sw).dot(Sb))
print("Sw^{-1}*Sb의 고윳값 = ", D)
wLDA = U[:,0]
print("LDA 정사영 벡터 = ", wLDA)

plt.figure(1)
plt.plot(C1[:,0], C1[:,1], 'bd')
plt.plot(C2[:,0], C2[:,1], 'ko')
plt.plot([0, wLDA[0]*15], [0,wLDA[1]*15], 'r')
plt.show()
