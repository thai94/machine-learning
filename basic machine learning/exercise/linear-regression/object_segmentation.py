import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

img = mpimg.imread('girl3.jpg')


X = img.reshape((img.shape[0]*img.shape[1], img.shape[2]))

K = 500
kmeans = KMeans(n_clusters=K).fit(X)
label = kmeans.predict(X)

img4 = np.zeros_like(X)
for k in range(K):
    img4[label == k] = kmeans.cluster_centers_[k]

img5 = img4.reshape((img.shape[0], img.shape[1], img.shape[2]))

plt.imshow(img5)
imgplot = plt.imshow(img5)
plt.axis('off')
plt.show() 