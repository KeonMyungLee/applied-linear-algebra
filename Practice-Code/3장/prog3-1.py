import numpy as np

print("벡터의 결합에 의한 행렬 생성")
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])

A = np.vstack([v1, v2, v3])       # v1, v2, v3를 각각 행으로 하는 행렬 생성 
print("A =", A)

B = np.column_stack([v1, v2, v3]) # v1, v2, v3를 각각 열로 하여 행렬 생성 
print("B =", B)

C = np.array([[1, 2], [3, 4], [5, 6]])
print("C =", C)

D = np.column_stack([C, v3])    # C행렬에 v3를 열로 추가하여 행렬 생성 
print("D =", D)

print("행렬의 원소 접근") 
E = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print("E[0,3] =", E[0,3])           # 1행 4열의 원소 
print("E[1,2] =", E[1,2])	       # 2행 3열의 원소 

print("E[0:2, 2] =", E[0:2, 2])     # 1행, 2행의 3열 1차원 행렬   
print("E[0:2, 2:3] =", E[0:2, 2:3]) # 1행, 2행의 3열, 4열의 2차원 행렬
print("E[2, :] =", E[2, :])         # 3행의 1차원 행렬 

print("원소의 변경")
print("E =", E)

print("E[0,0] = ", E[0, 0])        
E[0, 0] = -1                    # 1행 1열의 원소 변경 
print(E)
print("E[0,0] = ", E[0, 0])
