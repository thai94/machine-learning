import numpy as np
import matplotlib.pyplot as ptl
#  cung dau : du doan dung
#  cang thich thi cang phat it
x = np.arange(-0.1, -0.9, -0.1)
y = np.log2(1 + np.exp(-x))

ptl.plot(x, y)
ptl.show()