import numpy as np

A = np.array([[2, 3], [3, -6]])
w1, V1 = np.linalg.eig(A)

print("A의 고윳값 = ", w1)
print("A의 고유벡터 = ", V1)

B = np.array([[2, -3, 5], [-1, 4, -5], [-3, 3, -4]])
w2, V2 = np.linalg.eig(B)

print("\nB의 고윳값 = ", w2)
print("B의 고유벡터 = ", V2)
