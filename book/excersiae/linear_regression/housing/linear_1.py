import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./housing.csv")
x = df[0:500].median_income
y = df[0:500].median_house_value

x = np.array(x)
y = np.array(y)

one = np.ones((x.shape[0], 1))
X = x.reshape(((x.shape[0], 1)))
Xbar = np.concatenate((one, X), axis = 1)

A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
print(w)

w_0, w_1 = w[0], w[1]
y1 = w_1*x[0] + w_0
y2 = w_1*x[-1] + w_0

plt.scatter(x, y)
plt.plot(x, x.dot(w[1]) + w[0])

plt.show()