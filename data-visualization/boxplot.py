import numpy as np
import matplotlib.pyplot as plt

mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
data = mu + sigma * np.random.randn(1000)

fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.boxplot(data)

plt.show()
