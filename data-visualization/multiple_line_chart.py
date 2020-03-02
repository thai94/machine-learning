import matplotlib.pyplot as plt
import numpy as np

t1 = np.arange(0.0, 20.0, 1)
s1 = [1, 2, 2, 1, 6, 7, 9, 4, 5, 12, 8, 12, 17, 12, 11, 20, 17, 18, 8, 20]

t2 = 2 * np.arange(0.0, 20.0, 1)
s2 = (1, 2, 2, 1, 6, 7, 9, 4, 5, 12, 8, 12, 17, 12, 11, 20, 17, 18, 8, 20)

plt.plot(t1, s1, color='r')
plt.plot(t2, s2, color='b')
plt.xlabel('Item (s)')
plt.ylabel('Value')
plt.title('Python Line Chart: Plotting numbers')

plt.show()
