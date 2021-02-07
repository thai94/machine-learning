from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt

N = 50
X = np.linspace(-50, 50, 200, endpoint=True)
y = X**4 + X**3 + X**2 - X - 1 + np.sin(X)

plt.plot(X, y, 'r')
plt.show()