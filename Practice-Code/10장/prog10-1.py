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

print("고윳값 분해\n")
A = np.array([[3.0, 1.0], [2.0, 2.0]])
w, S = np.linalg.eig(A)
L = np.diag(w)
pprint("행렬 A", A)
pprint("고윳값 행렬 L", L)
pprint("고유벡터 행렬 S", S)
pprint("S*L*S^{-1}", np.matmul(np.matmul(S,L), np.linalg.inv(S)))

B = np.array([[1.0, 1.0, 0.0], [1.0, 3.0, 1.0], [2.0, -1.0, 1.0]])
w, S = np.linalg.eig(B)
L = np.diag(w)
pprint("행렬 B", B)
pprint("고윳값 행렬 L", L)
pprint("고유벡터 행렬 S", S)
pprint("S*L*S^{-1}", np.matmul(np.matmul(S,L), np.linalg.inv(S)))
