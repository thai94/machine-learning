import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./housing.csv")
X = df[0:100][['total_rooms', 'total_bedrooms', 'population', 'median_income']]
y = df[0:100].median_house_value


X = np.array(X)
y = np.array(y)

one = np.ones((X.shape[0], 1))
Xbar = np.c_[X, one]

A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
print(w)

o = Xbar[0].dot(w)
print(o)