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

# A의 열벡터에 대한 단위벡터로 구성된 직교기저를 구하는 그람-슈미트 과정
def gramSchmidt(A):
    basis = []
    for v in A.T:
        w = v - sum(np.dot(v,b)*b  for b in basis )
        if (np.abs(w) > 1e-10).any():  
            basis.append(w/np.linalg.norm(w))
    return np.array(basis).T

print("그람-슈미트 과정을 이용한 직교기저\n")
A = np.array([[3.0, 1.0], [2.0, 2.0]])
pprint("열벡터", A)
pprint("직교기저", gramSchmidt(A))

B = np.array([[1.0, 1.0, 0.0], [1.0, 3.0, 1.0], [2.0, -1.0, 1.0]])
pprint("열벡터", B)
pprint("직교기저", gramSchmidt(B))

C = np.array([[1, 1, 1], [2, 2, 0], [3, 0, 0], [0, 0, 1]])
pprint("열벡터", C)
pprint("직교기저", gramSchmidt(C))

# QR 분해
print("\nQR 분해\n")
C = np.array([[1, 1, 1], [2, 2, 0], [3, 0, 0], [0, 0, 1]])
Q, R = np.linalg.qr(C)

pprint("C", C)
pprint("Q", Q)
pprint("R", R)
pprint("Q*R", np.matmul(Q,R))
