import numpy as np


u = np.array([1, 0])

v = np.array([0, 1])

z = u + v

print(z)

r = z * 4

print(r)

print(np.dot(u, v))
