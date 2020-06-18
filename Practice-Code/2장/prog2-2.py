import numpy as np

# 행렬 A를 출력하는 함수 
def pprint(msg, A):
    print("---", msg, "---")
    (n,m) = A.shape
    for i in range(0, n):
        line = ""
        for j in range(0, m):
            line += "{0:.2f}".format(A[i,j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")


# 가우스-조단 소거법을 수행하는 함수 
def gauss(A):
    (n,m) = A.shape

    for i in range(0, n):
        # i번째 열에서 최대값을 갖는 행 선택 
        maxEl = abs(A[i,i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k,i]) > maxEl:
                maxEl = abs(A[k,i])
                maxRow = k

        # 현재 i번째 행과 최대값을 갖는 행 maxRow의 교환
        for k in range(i, m):
            tmp = A[maxRow,k]
            A[maxRow,k] = A[i,k]
            A[i,k] = tmp

        # 피봇 값을 1로 만들기 
        piv = A[i,i]
        for k in range(i, m):
            A[i,k] = A[i,k]/piv
            
        # 현재 i번째 열의 i번째 행을 제외한 모두 원소를 0으로 만들기
        for k in range(0, n):
            if k != i:
                c = A[k,i]/A[i,i]
                for j in range(i, m):
                    if i == j:
                        A[k,j] = 0
                    else:
                        A[k,j] = A[k,j] - c * A[i,j]
 
        pprint(str(i+1)+"번째 반복", A)  # 중간 과정 출력 

    # Ax=b의 해 반환
    x = np.zeros(n)
    for i in range(0,n):
        x[i] = A[i,n] 
    return x


# 주어진 문제 

# 
# 
# 

# 주어진 문제에 대한 첨가 행렬 
A = np.array([[2., 2., 4., 18.], [1., 3., 2., 13.], [3., 1., 3., 14.]])

pprint("주어진 문제", A)     # 첨가 행렬 출력 
x = gauss(A)               # 가우스-조단 소거법 적용

# 출력 생성
(n,m) = A.shape
line = "해:\t"
for i in range(0, n):
    line += "{0:.2f}".format(x[i]) + "\t"
print(line)
