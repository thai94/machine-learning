
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Perceptron(object):
    def __init__(self, eta=0.01, epochs=50):
        self.eta = eta
        self.epochs = epochs
    def train(self, X, y):

        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.epochs):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] +=  update * xi
                self.w_[0] +=  update
                errors += int(update != 0.0)
            if errors == 0:
                break
            self.errors_.append(errors)
        pass

    def predict(self, x):
        sum = np.dot(x, self.w_[1:]) + self.w_[0]
        return np.where(sum >= 0.0, 1, -1)

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [0,2]].values

ppn = Perceptron(epochs=10, eta=0.1)
ppn.train(X, y)
print('Weights: %s' % ppn.w_)
print('errors: ', ppn.errors_)
x11 = 3
y11 = (-x11 * ppn.w_[1] - ppn.w_[0]) / ppn.w_[2]
x22 = 8
y22 = (-x22 * ppn.w_[1] - ppn.w_[0]) / ppn.w_[2]
plt.plot([x11, x22], [y11, y22], 'b')
plt.plot(X[:, 0][y==1], X[:, 1][y==1], 'r.')
plt.plot(X[:, 0][y==-1], X[:, 1][y==-1], 'b.')
plt.show()

