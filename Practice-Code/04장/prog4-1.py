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
pprint("A", A)

Ainv1 = np.linalg.matrix_power(A, -1)   # matrix_power( ) 사용한 역행렬 계산
pprint("linalg.matrix_power(A, -1) => Ainv1", Ainv1)

Ainv2 = np.linalg.inv(A)  # inv( ) 사용한 역행렬 계산 
pprint("np.linalg.inv(A) => Ainv2", Ainv2)

pprint("A*Ainv1", np.matmul(A, Ainv1))   # 행렬과 역행렬의 곱 
pprint("A*Ainv2", np.matmul(A, Ainv2))   # 행렬과 역행렬의 곱 

B = np.random.rand(3,3)                 # 난수를 이용한 행렬 초기화 
pprint("B =", B)
Binv = np.linalg.inv(B)                   # 역행렬 계산 
pprint("Binv =", Binv)
pprint("B*Binv =", np.matmul(B, Binv))   # 행렬과 역행렬의 곱 

# CX = D의 해 계산 
C = np.array([[5., 3., 2., 1], [6, 2, 4, 5], [7, 4, 1, 3], [4, 3, 5, 2]])
D = np.array([[4.], [2.], [5.], [1.]])
x = np.matmul(np.linalg.inv(C), D)
pprint("x", x)                            # 해 X 출력 
pprint("C*x", np.matmul(C, X))           # C*X의 결과가 D와 같은지 확인 
