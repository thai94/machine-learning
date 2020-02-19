import numpy as np
import matplotlib.pyplot as plt

# random data
N = 80

# group 1
g1 = (0.3*np.random.rand(N), 0.3*np.random.rand(N))

# group 2
g2 = (0.4 + 0.3*np.random.rand(N), 0.3*np.random.rand(N))

# group 3
g3 = (0.7 + 0.3*np.random.rand(N), 0.8*np.random.rand(N))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x1, y1 = g1
ax.scatter(x1, y1, c="red", s=5, alpha=0.8, label='coffee')

x2, y2 = g2
ax.scatter(x2, y2, c="green", s=5, alpha=0.8, label='tea')

x3, y3 = g3
ax.scatter(x3, y3, c="blue", s=5, alpha=0.8, label='water')

plt.legend(loc=2)


plt.show()
