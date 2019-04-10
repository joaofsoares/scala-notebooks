import numpy as np


a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

A = np.array(a)

print(A)

print(A.shape)

print(A[1, 2])

print(A[0, 0:2])

print(A * 2)
