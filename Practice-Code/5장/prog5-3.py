import numpy as np

def solveByCrammer(A, B): # 크래머 공식을 이용한 연립선형방정식 AX=B의 해
    X = np.zeros(len(B))
    C = np.copy(A)
    for i in range(0, len(B)):
        for j in range(0, len(B)):
            C[j,i] = B[j]
            if i>0:
                C[j,i-1] = A[j,i-1]
        X[i] = np.linalg.det(C)/np.linalg.det(A)
    return X

# AX = B의 해
A = np.array([[2,-1,5,1], [3,2,2,-6], [1,3,3,-1], [5,-2,-3,3]])
B = np.array([[-3], [-32], [-47], [49]])
X = solveByCrammer(A, B)
print("A = ", A)
print("B = ", B)
print("X = ", X)
