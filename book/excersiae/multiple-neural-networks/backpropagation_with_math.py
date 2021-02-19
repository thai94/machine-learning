import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return np.divide(1, (1 + np.exp(-x)))

def feedForward(x, w, b):
    zh1 = x[0]*w[0] + x[1]*w[2] + x[2]*w[4] + b[0]
    zh2 = x[0]*w[1] + x[1]*w[3] + x[2]*w[5] + b[1]
    h1 = sigmoid(zh1)
    h2 = sigmoid(zh2)

    z01 = h1*w[6] + h2*w[8] + b[1]
    z02 = h1*w[7] + h2**w[9] + b[1]
    o1 = sigmoid(z01)
    o2 = sigmoid(z02)

    h = [h1, h2]
    o = [o1, o2]
    return (h, o)

def error(o, t):
    return 0.5 * ( np.power(o[0] - t[0], 2) + np.power(o[1] - t[1], 2))


def backpropagation(h, o, t, x, w, b):
     
    dE_dO1 = o[0] - t[0]
    dO1_dZo1 = o[0] * (1 - o[0])
    
    dZo1_dw7 = h[0]
    dE_dw7 = dE_dO1 * dO1_dZo1 * dZo1_dw7
    
    dE_dO2 = o[1] - t[1]
    dO2_dZo2 = o[1] * (1 - o[1])
    
    dZo2_dw8 = h[0]
    dE_dw8 = dE_dO2 * dO2_dZo2 * dZo2_dw8

    dZo1_dw9 = h[1]
    dE_dw9 = dE_dO1 * dO1_dZo1 * dZo1_dw9

    dZo2_dw10 = h[1]
    dE_dw10 = dE_dO2 * dO2_dZo2 * dZo2_dw10

    dZo1_db2 = b[0]
    dZo2_db2 = b[0]
    dE_db2 =  dE_dO1 * dO1_dZo1 * dZo1_db2 + dE_dO2 * dO2_dZo2 * dZo2_db2

    dZo1_dh1 = w[6]
    dZo2_dh1 = w[7]
    dE_dh1 = dE_dO1 * dO1_dZo1 * dZo1_dh1 + dE_dO2 * dO2_dZo2 * dZo2_dh1

    dh1_dZh1 = h[0] * (1 - h[0])
    dZh1_dw1 = x[0]
    dE_dw1 = dE_dh1 * dh1_dZh1 * dZh1_dw1

    dZo1_dh2 = w[8]
    dZo2_dh2 = w[9]
    dE_dh2 = dE_dO1 * dO1_dZo1 * dZo1_dh2 + dE_dO2 * dO2_dZo2 * dZo2_dh2

    dh2_dZh2 = h[1] * (1 - h[1])
    dZh2_dw2 = x[0]
    dE_dw2 = dE_dh2 * dh2_dZh2 * dZh2_dw2

    dZh1_dw3 = x[1]
    dE_dw3 = dE_dh1 * dh1_dZh1 * dZh1_dw3

    dZh2_dw4 = x[1]
    dE_dw4 = dE_dh2 * dh2_dZh2 * dZh2_dw4

    dZh1_dw5 = x[2]
    dE_dw5 = dE_dh1 * dh1_dZh1 * dZh1_dw5

    dZh2_dw6 = x[2]
    dE_dw6 = dE_dh2 * dh2_dZh2 * dZh2_dw6

    dZh1_db1 = b[1]
    dZh2_db1 = b[1]

    dE_db1 = dE_dh1 * dh1_dZh1 * dZh1_db1 + dE_dh2 * dh2_dZh2 * dZh2_db1

    dE_dw = [dE_dw1, dE_dw2, dE_dw3, dE_dw4, dE_dw5, dE_dw6, dE_dw7, dE_dw8, dE_dw9, dE_dw10]
    dE_db = [dE_db1, dE_db2] 

    return (dE_dw, dE_db)

def train(numEpoch, x, b, w, t, anpha):

    e = []
    for _ in range(numEpoch):
        # feed forward
        h, o = feedForward(x, w, b)

        # calc error
        ei = error(o, t)
        e.append(ei)

        # back propagation
        dE_dw, dE_db = backpropagation(h, o, t, x, w, b)

        # udpate weight & bias
        w1 = w[0] - anpha * dE_dw[0]
        w2 = w[1] - anpha * dE_dw[1]
        w3 = w[2] - anpha * dE_dw[2]
        w4 = w[3] - anpha * dE_dw[3]
        w5 = w[4] - anpha * dE_dw[4]
        w6 = w[5] - anpha * dE_dw[5]
        w7 = w[6] - anpha * dE_dw[6]
        w8 = w[7] - anpha * dE_dw[7]
        w9 = w[8] - anpha * dE_dw[8]
        w10 = w[9] - anpha * dE_dw[9]

        b1 = b[0] - anpha * dE_db[0]
        b2 = b[1] - anpha * dE_db[1]

        w = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10]
        b = [b1, b2]

    return (w, b, e)

def main():
    numEpoch = 10000

    # initialize variables
    w1 = 0.1
    w2 = 0.2
    w3 = 0.3
    w4 = 0.4
    w5 = 0.5
    w6 = 0.6
    w7 = 0.7
    w8 = 0.8
    w9 = 0.9
    w10 = 0.1
    w = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10]

    b1 = 0.5
    b2 = 0.5
    b = [b1, b2]

    # input & target values
    x1 = 1
    x2 = 4
    x3 = 5
    x = [x1, x2, x3]

    t1 = 0.1
    t2 = 0.05
    t = [t1, t2]

    anpha = 0.01

    w, b, e = train(numEpoch, x, b, w, t, anpha)
    print("w: ", w)
    print("b", b)

    plt.plot(range(numEpoch), e)
    plt.show()

main()