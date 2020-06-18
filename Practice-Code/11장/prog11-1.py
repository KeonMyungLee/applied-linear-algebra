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

print("특잇값 분해\n")
A = np.array([
	[1,2,3,4,5,6,7,8,9,10],
	[11,12,13,14,15,16,17,18,19,20],
	[21,22,23,24,25,26,27,28,29,30]])
pprint("데이터", A)

U, s, VT = np.linalg.svd(A)  # 특잇값 분해 
pprint("U", U)
 
m, n = A.shape
Sigma = np.zeros((m, n))     # mxn 행렬
k = np.size(s)
Sigma[:k, :k] = np.diag(s)    # 특잇값  
pprint("Sigma", Sigma)
pprint("V^T", VT)            # nxn 행렬 

# 2개의 특잇값을 선택 
n_elements = 2
Sigma = Sigma[:, :n_elements]
VT = VT[:n_elements, :]

# 재구성한 데이터 
B = np.matmul(U, np.matmul(Sigma, VT))
pprint("재구성한 데이터", B)
