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

# 최소제곱해
print("\n행렬방정식의 최적근사해\n")
A = np.array([[1,1], [2,1], [3,1], [4,1]])
b = np.array([[3.5], [4.3], [7.2], [8.0]])
x = np.matmul(np.matmul(np.linalg.inv(np.matmul(A.T, A)), A.T), b)

pprint("Ax = b의 A", A)
pprint("Ax = b의 b", b)
pprint("Ax = b의 해(x))", x)

print("\nQR 분해를 이용한 선형방정식의 최적근사해\n")
C = np.array([[1,3,5], [1,1,0], [1,1,2], [1,3,3]])
d = np.array([[3], [5], [7], [-3]])
Q, R = np.linalg.qr(C)
x = np.matmul(np.matmul(np.linalg.inv(R), Q.T), d)

pprint("Cx = d의 C", C)
pprint("Cx = d의 d", d)
pprint("Cx = d의 해(x))", x)
