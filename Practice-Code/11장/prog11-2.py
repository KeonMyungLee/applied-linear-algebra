import numpy as np
import matplotlib.pyplot as plt
import imageio as im 

src = im.imread('flower3.jpg')
A = src[:,:,0]

# n_elements 개수만큼의 계수에 해당하는 요소를 사용하는 재구성 
def reconstruct(U, Sigma, VT, n_elements):
    Sigma = Sigma[:, :n_elements]
    VT = VT[:n_elements, :]
    B = np.matmul(U, np.matmul(Sigma, VT)) 
    return B 

plt.rcParams.update({'xtick.major.width': 0,
                     'xtick.labelsize': 0,
                     'ytick.major.width': 0,
                     'ytick.labelsize': 0,
                     'axes.linewidth': 0})

U, s, VT = np.linalg.svd(A)  # 특잇값 분해 
m, n = A.shape
Sigma = np.zeros((m, n))     # m x n 행렬
k = np.size(s)
Sigma[:k, :k] = np.diag(s)   # 특잇값  

plt.subplot(3,3,1)
plt.title('original')
plt.imshow(A, cmap='gray')

plt.subplot(3,3,2)
plt.title('rank 1')
B = reconstruct(U, Sigma, VT, 1)
plt.imshow(B, cmap='gray')

plt.subplot(3,3,3)
plt.title('upto rank 5')
B = reconstruct(U, Sigma, VT, 5)
plt.imshow(B, cmap='gray')

plt.subplot(3,3,4)
plt.title('upto rank 20')
B = reconstruct(U, Sigma, VT, 20)
plt.imshow(B, cmap='gray')

plt.subplot(3,3,5)
plt.title('upto rank 30')
B = reconstruct(U, Sigma, VT, 30)
plt.imshow(B, cmap='gray')

plt.subplot(3,3,6)
plt.title('upto rank 50')
B = reconstruct(U, Sigma, VT, 50)
plt.imshow(B, cmap='gray')

plt.subplot(3,3,7)
plt.title('upto rank 100')
B = reconstruct(U, Sigma, VT, 100)
plt.imshow(B, cmap='gray')

plt.subplot(3,3,8)
plt.title('upto rank 150')
B = reconstruct(U, Sigma, VT, 150)
plt.imshow(B, cmap='gray')

plt.subplot(3,3,9)
plt.title('upto rank 200')
B = reconstruct(U, Sigma, VT, 200)
plt.imshow(B, cmap='gray')
plt.show()
