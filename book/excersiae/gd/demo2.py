import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as ptl

X = np.random.rand(1000)
y = 4 + 3 * X + .5*np.random.randn(1000) # noise added


one = np.ones((X.shape[0],1))
Xbar = np.concatenate((one, X.reshape(-1, 1)), axis = 1)

def grad(w):
    N = Xbar.shape[0]
    return 1/N * Xbar.T.dot(Xbar.dot(w) - y)

def cost(w):
    N = Xbar.shape[0]
    0.5 / N * np.linalg.norm(y - Xbar.dot(w)) ** 2

def GD(w_init, eta):
    w = [w_init]
    for it in range(1000):
        w_new = w[-1] - eta * grad(w[-1])
        if np.linalg.norm(grad(w_new)) < 1e-3:
            break
        w.append(w_new)

    return (w, it)

w_init = np.array([2, 1])

(w1, it1) = GD(w_init, 0.5)

print('Sol found by GD: w = ', w1[-1].T, ', after %d iterations.' %(it1+1))

ptl.plot(X, y, 'r.')
ptl.show()
