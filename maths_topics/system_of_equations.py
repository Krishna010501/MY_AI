import numpy as np

# Coefficient matrix
A = np.array([[2, 3], [3, 2]])

# Constant matrix
B = np.array([12, 10])

# Solve the system of equations
solution = np.linalg.solve(A, B)

# Extract the values
x, y = solution

# Print results
print(f"Number of days Machine A works: {x:.2f}")
print(f"Number of days Machine B works: {y:.2f}")