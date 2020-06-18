import numpy as np

def DFT(x):  # 이산 푸리에 변환 
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

def IDFT(x): # 역 이산 푸리에 변환 
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(2j * np.pi * k * n / N)/N
    return np.dot(M, x)
    
d = np.array([1, 0, 2, 1])
F = DFT(d)
print('이산 푸리에 변환 결과 : ', F)
D = IDFT(F)
print('역 이산 푸리에 변환 결과: ', D)
