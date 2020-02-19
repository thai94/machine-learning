# https://pythonspot.com/matplotlib/
import matplotlib.pyplot as plt
import numpy as np

# Create data
N = 500
x = np.random.rand(N)
y = np.random.rand(N)
colors = (0, 0.5, 0.5)
area = np.pi*3


# Plot
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Scatter plot example')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
