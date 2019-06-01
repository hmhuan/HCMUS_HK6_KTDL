import numpy as np

a = np.array([[1, 2, 3]])
b = np.array([[2, 8, 2]])

print(np.linalg.norm(a - b))
print(np.sum(np.power(a - b, 2)))