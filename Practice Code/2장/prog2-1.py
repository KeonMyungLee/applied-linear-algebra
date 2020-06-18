import numpy as np

a = np.zeros((2, 3))    # 2×3 영행렬 
print("a =", a)

b = np.ones((2, 2))     # 1값을 갖는 2×2 행렬 
print("b =", b)

c = np.full((3, 2), 3)   # 3을 성분로 갖는 3×2 행렬
print("c =", c)

d = np.eye(2)           # 2×2 크기의 단위행렬 
print("d =", d)
