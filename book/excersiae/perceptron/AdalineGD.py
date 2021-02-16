import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class AdalineSGD(object):

    def __init__(self, eta=0.01, epochs=50):
        self.eta = eta
        self.epochs = epochs
    
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def activation(self, X):
        return self.net_input(X)

    def train(self, X, y):
       
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []

        for i in range(self.epochs):
            output = self.net_input(X)
            errors = (y - output)
            
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()

            cost = (errors**2).sum() / 2.0
            if cost <= 0.1:
                break
            self.cost_.append(cost)
        pass

    def predict(self, X):
        return np.where(self.activation(X) >= 0.0, 1, -1)

ppn = AdalineSGD(epochs=800, eta=0.0001)
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [0,2]].values


ppn.train(X, y)
print('Weights: %s' % ppn.w_)
print('cost: %s' % len(ppn.cost_), "-", ppn.cost_[-1])
x11 = 4
y11 = (-x11 * ppn.w_[1] - ppn.w_[0]) / ppn.w_[2]
x22 = 8
y22 = (-x22 * ppn.w_[1] - ppn.w_[0]) / ppn.w_[2]
plt.plot([x11, x22], [y11, y22], 'b')
plt.plot(X[:, 0][y==1], X[:, 1][y==1], 'r.')
plt.plot(X[:, 0][y==-1], X[:, 1][y==-1], 'b.')
plt.show()

