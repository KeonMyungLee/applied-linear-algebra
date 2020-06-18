import numpy as np

A = np.array([[1, 2, 3],  # 3x3 행렬 생성 
              [4, 5, 6],
              [7, 8, 9]])  

v = np.array([[1],       # 3x1 행렬 생성
              [2],
              [3]]) 
print("A =", A)
print("v =", v)

print("A.shape =", A.shape)  # 행렬 A의 크기 (3,3)
print("v.shape =", v.shape)   # 행렬 v의 크기 (3,1)

B = np.array([1, 2, 3])
print("B =", B)
print("B.ndim =", B.ndim)    # 행렬 B의 차원 1
print("B.shape =", B.shape)  # 행렬 B의 크기 (3,)
print("v.ndim =", v.ndim)    # 행렬 v의 차원 2 

C = np.array([[1, 2, 3], [4, 5, 6]])
print("C = ", C)
print("C.ndim =", C.ndim)    # 행렬 C의 차원 2
print("C.shape =", C.shape)  # 행렬 C의 크기 (2,3)
