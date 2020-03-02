import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 20.0, 1)
s = [1, 2, 2, 1, 6, 7, 9, 4, 5, 12, 8, 12, 17, 12, 11, 20, 17, 18, 8, 20]

plt.plot(t, s, color='r')
plt.xlabel('Item (s)')
plt.ylabel('Value')
plt.title('Python Line Chart: Plotting numbers')


plt.show()
