import numpy as np

x = np.array([1, 2.0, 3, 4, 5], dtype=np.int64)
print(x)

y = np.zeros(10, dtype=np.int64)
print (y[0])

z = np.ones_like(y)
print (z)

t = np.arange( start= 0, stop = 1, step=0.1)
print(t)

a = np.arange(0, 10)
print(2 ** a)

b = 2 ** a
print ( b)
ids = [4, 6, 8]
print (b[ids])
print (b[2:])
b[ids] = 1
print (b)

c = np.array([1, 2, 3, 4, 5, 6, 7])
print (10 + c)
print (10 - c)
print (10 * c)
print (10 / c)

d = np.array([1, 2, 3, 4])
e = np.array([2, 3, 4, 8])
print (d / e)
print (np.log2(d))

x = np.array([1, 2, 3, 4])
print(np.sum(np.abs(x)))
ex = np.exp(x)
sumex = np.sum(ex)
y = ex / sumex
print (y) 

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 9])
print (x.dot(y))

print (np.sqrt(np.sum(x ** 2)))