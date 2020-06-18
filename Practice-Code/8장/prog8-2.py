import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA 
import pandas as pd
from sklearn.preprocessing import StandardScaler

# iris 데이터의 위치 URL 
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# Pandas DataFrame으로 읽어들이기 
df = pd.read_csv(url, names=['sepal length','sepal width','petal length','petal width','target'])

nrow, ncol = df.shape
print("Iris data set :", nrow, "records with", ncol, "attributes\n")
print("First 5 records in iris data\n", df.head(5))
features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = df.loc[:, features].values          # 데이터의 속성값  
y = df.loc[:,['target']].values          # 데이터의 부류 
x = StandardScaler().fit_transform(x)  # 평균 0, 분산 1인 데이터로 변환 

pca = PCA(n_components=2)               # PCA를 적용하여 2개의 주성분만 추출 
principalComponents = pca.fit_transform(x)  # 주성분 축 2개를 이용한  2차원 데이터로 변환   
print("\nFirst principal axis:", pca.components_[0])
print("Second principal axis:", pca.components_[1])

principalDf = pd.DataFrame(data = principalComponents,
              columns = ['principal component 1', 'principal component 2'])
finalDf = pd.concat([principalDf, df[['target']]], axis = 1)

print("\nFirst 5 Transformed records\n", finalDf.head(5)) 
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('principal component 1', fontsize = 12)
ax.set_ylabel('principal component 2', fontsize = 12)
ax.set_title('PCA with 2 components', fontsize = 15)

targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']  # iris 데이터의 부류 이름 
colors = ['r', 'g', 'b']   # 부류별로 지정된 색상  
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['target'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2'], c = color, s = 40)
ax.legend(targets)
ax.grid()
fig.show()
