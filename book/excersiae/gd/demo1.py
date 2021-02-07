import numpy as np
import matplotlib.pyplot as ptl

x = np.arange(-10, 10, step= 0.1)
y = x**2 + 5 * np.sin(x)

ptl.plot(x, y, 'r')


def grad(x0):
    return 2 * x0 + 5 * np.cos(x0)
def cost(x0):
    return x0**2 + 5 * np.sin(x0)
def GD(x_init, eta):
    x = [x_init]
    for it in range(100):
        x_new = x[-1] - eta * grad(x[-1])
        if abs(grad(x_new)) <= 1e-3:
            break
        x.append(x_new)
    return (x, it)

(x1, it1) = GD(10, 0.1)
print('Solution x1 = %f, cost = %f, after %d iterations'%(x1[-1], cost(x1[-1]), it1))

ptl.plot(np.array(x1), cost(np.array(x1)), 'b.')

ptl.show()