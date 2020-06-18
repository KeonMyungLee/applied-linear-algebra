import numpy as np

# 행렬 A를 출력하는 함수 
def pprint(msg, A):
    print("---", msg, "---")
    (n,m) = A.shape
    for i in range(0, n):
        line = ""
        for j in range(0, m):
            line += "{0:.2f}".format(A[i,j]) + "\t"
        print(line)
    print("")

A = np.array([[1., 2.], [3., 4.]])
B = np.array([[2., 2.], [1., 3.]])
C = np.array([[4., 5., 6.], [7., 8., 9.]])
v = np.array([[10.], [20.]])
w = np.array([[4.], [8.]])

pprint("A+B", A+B)     # 행렬의 덧셈
pprint("A-B", A-B)     # 행렬의 뺄셈 

pprint("3*A ", 3*A)     # 행렬의 스칼라배 
pprint("2*v ", 2*v)      # 벡터의 스칼라배

pprint("matmul(A,B)", np.matmul(A,B))      # 행렬의 곱셈
pprint("matmul(A,C)", np.matmul(A,C))      # 행렬의 곱셈  
pprint("A*v", A*v)      # 행렬과 벡터의 곱셈

pprint("matrix_power(A, 2)", np.linalg.matrix_power(A, 2)) # 행렬의 거듭제곱
pprint("matrix_power(A, 3)", np.linalg.matrix_power(A, 3)) # 행렬의 거듭제곱

pprint("A*B", A*B)            # 행렬의 원소별 곱셈
pprint("A/B", A/B)             # 행렬의 원소별 나눗셈 
pprint("A**2 == A*A", A**2)  # 행렬의 원소별 거듭제곱

pprint("A.T", A.T)       # 행렬의 전치
pprint("v.T", v.T)        # 벡터의 전치   

C = np.diag([1, 2, 3])   # 대각행렬 생성
pprint("diag(1,2,3) =", C)

D11 = np.array([[1, 2], [3, 4]])
D12 = np.array([[5], [6]])
D21 = np.array([[7, 7]])
D22 = np.array([[8]])
D = np.block([[D11, D12], [D21, D22]])  # 블록행렬 생성 
pprint("block matrix", D) 
