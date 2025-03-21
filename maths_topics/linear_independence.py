import numpy as np

# Define vectors as matrix
A = np.array([[1, 2], [3, 4]])

# Check for linear independence using determinant
det = np.linalg.det(A)
if det == 0:
    print("Vectors are linearly dependent")
else:
    print("Vectors are linearly independent")

# Define basis vectors
basis = np.array([[1, 0], [0, 1]])
print("\nBasis vectors:")
print(basis)

# Find rank of matrix
rank = np.linalg.matrix_rank(A)
print("\nRank of matrix A:", rank)