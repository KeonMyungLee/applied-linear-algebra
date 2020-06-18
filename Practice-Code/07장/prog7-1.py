import numpy as np
import matplotlib.pyplot as plt
import imageio as im 

def linear_transformation(src, a):   # 선형변환  수행 함수 
    M, N, _ = src.shape           #  M : y-축 방향 크기, N: x-축 방향 크기 
    corners = np.array([[0, 0, N-1, N-1], [0, M-1, 0, M-1]]) # 영상 코너 위치
    new_points = a.dot(corners).astype(int)  # 코너 위치의 선형 변환 결과 

    xcoord = new_points[0,:]   # x-축 좌표값 
    ycoord = new_points[1,:]   # y-축 좌표값 
    minx = np.amin(xcoord) 
    maxx = np.amax(xcoord) 
    miny = np.amin(ycoord) 
    maxy = np.amax(ycoord)

    newN = maxx-minx+1    # 선형변환 이후 x-축 방향 영상 크기 
    newM = maxy-miny+1    # 선형변환 이후 y-축 방향 영상 크기 
    dest = np.full((newM, newN, 3), 200)    # 출력 영상 생성  
    y = miny
    for i in range(newM):
        x = minx
        for j in range(newN):
            pts = np.array([[x],[y]])
           # 출력영상의 (x,y) 위치에 대응하는 원본영상의 위치 계산: 역행렬 사용 
            newpts = np.linalg.inv(a).dot(pts).round().astype(int) 
            if (newpts[0] >= 0 and newpts[0] < N and newpts[1] >= 0 
                and newpts[1] < M):
                dest[i,j,:] = src[newpts[1],newpts[0],:]
            x = x+1
        y = y+1
    return dest

def translate(src, d):        # d[0]: x-축 이동,  d[1]: y-축 이동
    M, N, _ = src.shape    # N : x-axis,  M : y-axis
    steps = np.absolute(d)

    newM = M + 2*steps[1]
    newN = N + 2*steps[0]
    dest = np.full((newM, newN, 3), 200)         # 출력영상 생성 
    for i in range(newM):
        for j in range(newN):
            yp = i-d[0]
            xp = j-d[1]
            if xp >= 0 and xp < N and yp >= 0 and yp < M:
                dest[i,j,:] = src[yp, xp, :]
    return dest 

src = im.imread('Cat.jpg')          # 영상 파일 읽어오기 
plt.subplot(3,2,1)                   # 3행 2열로 분할하여 첫 번째 위치 선택 
plt.title('original')                   # 제목 출력 
plt.imshow(src)                     # 영상 출력 

# x축으로 1.5배, y축으로 0.8배 확대 및 축소 
a = np.array([[1.5, 0],[0, 0.8]])
dst = linear_transformation(src, a)
plt.subplot(3,2,2)
plt.title('scaled by 1.5 and 0.8')
plt.imshow(dst)

# 반시계 방향으로 45∘ 회전 
alpha = np.pi/4
a = np.array([[np.cos(alpha), -np.sin(alpha)], [np.sin(alpha), np.cos(alpha)]])
dst = linear_transformation(src, a)
plt.subplot(3,2,3)
plt.title('Rotation by 45∘ clockwise')
plt.imshow(dst)

# x-축을 기준으로 반사 
a = np.array([[1, 0], [0, -1]])
dst = linear_transformation(src, a)
plt.subplot(3,2,4)
plt.title('Reflection about the x-axis')
plt.imshow(dst)

# x-축 방향으로 +y/2를 하면서 밀림 
a = np.array([[1, .5], [0, 1]])
dst = linear_transformation(src, a)
plt.subplot(3,2,5)
plt.title('shearing in the x-axis with +y/2')
plt.imshow(dst)

# x축 방향으로 30, y축 방향으로 이동 
dst = translate(src, [30, 20])
plt.subplot(3,2,6)
plt.title('translate by(30, 20)')
plt.imshow(dst)               
plt.show()                      # 화면에 보이기 
