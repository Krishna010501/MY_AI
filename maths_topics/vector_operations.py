import numpy as np

# Create vectors
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Addition
print("Addition:", v1 + v2)

# Subtraction
print("Subtraction:", v1 - v2)

# Scalar Multiplication
print("Scalar Multiplication:", 2 * v1)

# Dot Product
print("Dot Product:", np.dot(v1, v2))

# Cross Product
print("Cross Product:", np.cross(v1, v2))

# Magnitude
print("Magnitude of v1:", np.linalg.norm(v1))

# Projection
projection = (np.dot(v1, v2) / np.dot(v2, v2)) * v2
print("Projection of v1 onto v2:", projection)