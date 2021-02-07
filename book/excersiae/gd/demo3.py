import numpy as np
import matplotlib.pyplot as ptl

x = np.arange(-7, 7, 0.1)
y = x ** 2 + 10 * np.sin(x)

def grad(x0):
    return 2 * x0 + 10 * np.cos(x0)

def cost(x0):
    return x0 ** 2 + 10 * np.sin(x0)

def GD(x_init, eta):
    x = [x_init]
    for it in range(100):
        x_new = x[-1] - eta * grad(x[-1])
        if abs(grad(x_new)) <= 1e-3:
            break
        x.append(x_new)
    return (x, it)

(x1, it1) = GD(6, 0.1)
print('Solution x1 = %f, cost = %f, after %d iterations'%(x1[-1], cost(x1[-1]), it1))

ptl.plot(np.array(x1), cost(np.array(x1)), 'r.')


def GD_momentum(x_init, eta, gama):
    x = [x_init]
    preV = 0
    for it in range(100):
        v_new = gama * preV + eta * grad(x[-1])
        x_new = x[-1] - v_new
        if abs(grad(x_new)) <= 1e-3:
            break
        x.append(x_new)
        preV = v_new
    
    return (x, it)

(x2, it2) = GD_momentum(6, 0.1, 0.9)
print('Solution momentum x1 = %f, cost = %f, after %d iterations'%(x2[-1], cost(x2[-1]), it2))

ptl.plot(np.array(x1), cost(np.array(x1)), 'r.')

ptl.plot(x, y, 'b')
ptl.show()