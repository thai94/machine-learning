import math
import numpy as np 
import matplotlib.pyplot as plt

X = np.linspace(-4,6,100)
Y = X**2 + 10 * np.sin(X)

plt.plot(X, Y, 'g')     # data 
plt.axis([-4, 6, -10, 50])

def grad(x):
    return 2*x + 10 * math.cos(x)
def cost(x):
    return x**2 + 10 * np.sin(x)

def myGD(eta, x0):
    x = [x0]
    for it in range(100):
        xNew = x[-1] - eta * grad(x[-1])
        if abs(grad(xNew)) < 1e-3:
            break
        x.append(xNew)
    return (x, it)

(x1, it1) = myGD(0.1, 5)

plt.plot(np.asarray(x1), cost(np.asarray(x1)), 'r.')     # data 

print('Solution x1 = %f, cost = %f, obtained after %d iterations'%(x1[-1], cost(x1[-1]), it1))

def has_converged(theta_new):
    return np.linalg.norm(grad(theta_new)) < 1e-3

def GD_momentum(theta_init, eta, gamma):
    theta = [theta_init]
    v_old = np.zeros_like(theta_init)
    for it in range(100):
        v_new = gamma*v_old + eta*grad(theta[-1])
        theta_new = theta[-1] - v_new
        if has_converged(theta_new):
            break 
        theta.append(theta_new)
        v_old = v_new
    return theta

def myGD_momentum(theta0, eta, v0, gama):
    thetas = [theta0]
    vOld = v0
    for it in range(100):
        vNew = gama * vOld + eta * grad(thetas[-1])
        thetaNew = thetas[-1] - vNew
        if has_converged(thetaNew):
            break
        thetas.append(thetaNew)
        vOld = vNew
    return thetas


# theta_F = GD_momentum(5, 0.1, 0.9)
theta_F = myGD_momentum(5, 0.1, 0, 0.9)
plt.plot(np.asarray(theta_F), cost(np.asarray(theta_F)), 'b.')     # data 

print('Solution x2 = %f'% theta_F[-1])

plt.show()