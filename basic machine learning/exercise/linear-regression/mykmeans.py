import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
np.random.seed(11)

means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)
X = np.concatenate((X0, X1, X2), axis = 0)
K = 3

def initilizeCenters(X, k):
    return X[np.random.choice(X.shape[0], k, replace=False)]

def assignLabel(X, centers):
    D = cdist(X, centers)
    return np.argmin(D, axis=1)

def findNewCenter(X, label):
    centers = np.zeros((K, X.shape[1]))
    for k in range(K):
        xk = X[label == k]
        centers[k, :] = np.mean(xk, axis = 0)

    return centers

def hasConverged(centers, new_centers):
    return (set([tuple(a) for a in centers]) == 
        set([tuple(a) for a in new_centers]))

def kmeans(X, k):
    # initilize random center
    centers = [initilizeCenters(X, k)]

    label = []
    while True:
        label = assignLabel(X, centers[-1])
        newCenter = findNewCenter(X, label)
        if hasConverged(centers[-1], newCenter):
            break
        centers.append(newCenter)
    return (centers[-1], label)


(centers, label) = kmeans(X, K)

def kmeans_display(X, label):
    K = np.amax(label) + 1
    X0 = X[label == 0, :]
    X1 = X[label == 1, :]
    X2 = X[label == 2, :]
    
    plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize = 4, alpha = .8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize = 4, alpha = .8)
    plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize = 4, alpha = .8)

    plt.axis('equal')
    plt.plot()
    plt.show()

kmeans_display(X, label)