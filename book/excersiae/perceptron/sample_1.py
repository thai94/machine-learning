import numpy as np 
import matplotlib.pyplot as plt

means = [[-1, 0], [1, 0]]
cov = [[.3, .2], [.2, .3]]
N = 100

X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)



X = np.concatenate((X0, X1), axis = 0)
y = np.concatenate((np.ones(N), -1*np.ones(N)))

def predict(w, X):
    return np.sign(X.dot(w))

def perceptron(X, y, w_init):
    w = w_init
    it = 0
    while True:
        pred = predict(w, X)
        mis_idxs = np.where(np.equal(pred, y) == False)[0]
        num_mis = mis_idxs.shape[0]
        if num_mis <= 1:
            return w
        random_id = np.random.choice(mis_idxs, 1)[0]
        w = w + y[random_id]*X[random_id]
        it += 1
        print("Ie: ", it)

Xbar = X
w_init = np.random.randn(Xbar.shape[1])
w = perceptron(Xbar, y, w_init)

plt.plot(X[:, 0], X[:, 1], "b.")

x11 = -1.5
y11 = - w[0] * x11 / w[1]

x22 = 1.5
y22 = - w[0] * x22 / w[1]

plt.plot([x11, x22], [y11, y22], "r")
plt.show()

print(w)