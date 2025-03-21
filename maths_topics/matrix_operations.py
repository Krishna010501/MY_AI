import numpy as np

# Define two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Addition
print("Addition:\n", A + B)

# Subtraction
print("Subtraction:\n", A - B)

# Multiplication
print("Multiplication:\n", np.matmul(A, B))

# Transpose
print("Transpose:\n", A.T)

# Inverse
print("Inverse:\n", np.linalg.inv(A))

# Determinant
print("Determinant:\n", np.linalg.det(A))