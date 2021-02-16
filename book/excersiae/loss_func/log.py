import numpy as np
import matplotlib.pyplot as ptl

x = np.arange(0.1, 100, 0.1)
y = np.log2(x)
ptl.plot(x, y)
ptl.show()
