from mnist import MNIST
mndata = MNIST('./MNIST/')
images, labels = mndata.load_testing()
from display_network import *
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors

X = np.asarray(images)
K = 10
kmeans = KMeans(n_clusters=K).fit(X)

# print('Centers found by scikit-learn:')
# print(kmeans.cluster_centers_)
pred_label = kmeans.predict(X)


# NearestNeighbors
# fig=plt.figure(figsize=(28, 28))
X0 = np.asarray(X)[:10000,:]
N0 = 100
k = 5
Xk = X0[pred_label == k, :]
center_k = [kmeans.cluster_centers_[k]]
neigh = NearestNeighbors(N0)
neigh.fit(Xk)
nears = Xk[neigh.kneighbors(center_k, N0)[1][0]]

fig=plt.figure(figsize=(28, 28))
columns = 40
rows = 50
it = 1
for idx in range(nears.shape[0]):
    first_image = np.array(nears[idx], dtype='float')
    img = first_image.reshape((28, 28))
    fig.add_subplot(rows, columns, it)
    f1 = plt.imshow(img, interpolation='nearest', cmap = "jet")
    f1.axes.get_xaxis().set_visible(False)
    f1.axes.get_yaxis().set_visible(False)

    it = it + 1

plt.show()


# First 100 images

# fig=plt.figure(figsize=(28, 28))
# columns = 40
# rows = 50
# it = 1
# for idx, lable in enumerate(pred_label):
#     if lable == 1:
#         first_image = np.array(X[idx], dtype='float')
#         img = first_image.reshape((28, 28))

#         fig.add_subplot(rows, columns, it)
#         f1 = plt.imshow(img, interpolation='nearest', cmap = "jet")
#         f1.axes.get_xaxis().set_visible(False)
#         f1.axes.get_yaxis().set_visible(False)
        
#         it = it + 1

#         if it == 100:
#             break

# plt.show()