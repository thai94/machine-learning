from __future__ import print_function
import numpy as np
from time import time # for comparing runing time
d, N = 1000, 10000 # dimension, number of training points 
X = np.random.randn(N, d) # N d-dimensional points
z = np.random.randn(d)

def dist_pp(z, x):
    d = z - x
    return np.sum(d * d)

def dist_ps_naive(z, X):
    N = X.shape[0]
    res = np.zeros((1, N))
    for i in range(N):
        res[0][i] = dist_pp(z, X[i])
    return res

t1 = time()
D1 = dist_ps_naive(z, X)
print('naive point2set, running time:', time() - t1, 's')
print("D1: ", D1)