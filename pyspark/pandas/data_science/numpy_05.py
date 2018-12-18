import numpy as np


A = np.array([[0, 1, 1], [1, 0, 1]])

B = np.array([[1, 1], [1, 1], [-1, 1]])

C = np.dot(A, B)

print(C)
