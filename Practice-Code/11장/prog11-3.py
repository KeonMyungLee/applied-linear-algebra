import cv2
import numpy as np
import matplotlib.pyplot as plt

# corners1의 좌표를 corners2의 좌표로 변환하는 호모그래피 행렬 xform 구하기
def compute_xform(corners1, corners2):
  A = [ ]
  for i in range(4):
    x1, y1 = corners1[i]
    x2, y2 = corners2[i]
    A.append([x1, y1, 1, 0, 0, 0, -x2*x1, -x2*y1, -x2])
    A.append([0, 0, 0, x1, y1, 1, -y2*x1, -y2*y1, -y2])
  
  A = np.asarray(A)
  U, S, V = np.linalg.svd(A)
  xform = V[-1, :]
  xform = np.reshape(xform, (3, 3))

  return xform

def transform_image(xform, image1, corners1, corners2):
  # 호모그래피 행렬 xform을 통한 영상 image1의 변환 
  warped = cv2.warpPerspective(image1, xform, (500, 500))

  h1, w1 = image1.shape[:2]    # 원본 영상의 높이와 폭 
  h2, w2 = warped.shape[:2]    # 변환된 영상의 높이와 폭  

  out_image = np.zeros((max(h1, h2), w1+w2, 3), dtype=np.uint8)
  out_image[:h1, :w1, :3] = image1
  out_image[:h2, w1:w1+w2, :3] = warped

  for i in range(4):   # 대응 위치 표시 
    c1 = corners1[i]
    c2 = (corners2[i][0] + w1, corners2[i][1])
    cv2.circle(out_image, c1, radius = 2, color = (0, 255, 0), thickness = 2)
    cv2.circle(out_image, c2, radius = 2, color = (30, 255, 255), thickness = 2)
    cv2.line(out_image, c1, c2, color = (0, 0, 255), thickness = 1)
  
  cv2.imshow('original and transformed images', out_image)   # 
  cv2.waitKey(0)

def main():
  img_path1 = 'cameraman1.png'    # 입력 영상 파일명 
  img1 = cv2.imread(img_path1, cv2.IMREAD_COLOR)
  corners1 = [(122, 51), (26, 300), (454, 131), (330, 414)]  # 원본 영상의 꼭짓점 위치
  corners2 = [(50, 50), (50, 450), (450, 50), (450, 450)]    # 변환 영상의 대응 위치 
  xform = compute_xform(corners1, corners2)         # 변환 행렬 계산 
  print(xform)                                        # 호모그래피 행렬 출력
  transform_image(xform, img1, corners1, corners2)    # 영상 변환 

if __name__ == '__main__':
  main()
