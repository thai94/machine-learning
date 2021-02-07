import numpy as np

_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A = np.array(_A)

print ('Matrix A: ', A)

_B = [1, 2, 3]
B = np.array(_B)
print('Vector B: ', B)

print('A[0][1]: ', A[0, :])
print('B[0]: ', B[0])

print("-----") 

_C = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
_D = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
C = np.array(_C)
D = np.array(_D)

E = C + D
print('E: ', E)
F = C - D
print('F', F)

print('E/2:', E /2)
print('E*2:', E * 2)

G = A.dot(B)
print('G: ', G)

print('-----')
_I = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
_J = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
I = np.array(_I)
J = np.array(_J)

print ('I * J: ', I.dot(J))

print('-----')
a = np.eye(5)
print('I: ', a)

_G = [[1, 2], [3, 4]]
_H = [[5, 6], [7, 8]]
G = np.array(_G)
H = np.array(_H)
print ('G*H: ', G * H)

print('a== 1', a == 1)

print('A-1: ', np.linalg.pinv(G))
print('A-1: ', G.dot(np.linalg.pinv(G)))
print('transpose: ', np.transpose(G))
print('Size G:', np.size(G))

print('Sum: ', np.sum(G))
print('Max: ', np.max(G))
print('Min: ', np.min(G))

print('DET G: ', np.linalg.det(G))