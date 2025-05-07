import numpy as np

A = np.array([[1, 2], [4, 5], [7, 8]])
B = np.diag([2, 2, 2])
C = np.array([[2, 1, 0], [0, 0, 2]])
D = np.array([[3, 2, 1], [0, 5, 6], [8, -1, 2]])

print("Ślad A:", np.trace(A))
print("Ślad B:", np.trace(B))
print("Ślad C:", np.trace(C))
print("Ślad D:", np.trace(D))