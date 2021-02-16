import numpy as np
import matplotlib.pyplot as ptl

x = np.arange(0.1, 10, 0.1)
y = np.exp(-x)

ptl.plot(x, y)
ptl.show()