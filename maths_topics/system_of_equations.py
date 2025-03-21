import numpy as np

# Coefficient matrix
A = np.array([[2, 3], [3, 2]])

# Constant matrix
B = np.array([12, 10])

# 1️⃣ Substitution Method
def substitution_method():
    # From 2x + 3y = 12 → x = (12 - 3y) / 2
    y = (12 - 2 * ((10 - 2 * 12 / 3) / 3)) / 3
    x = (12 - 3 * y) / 2
    return x, y

# 2️⃣ Elimination Method
def elimination_method():
    # First equation: 2x + 3y = 12
    # Second equation: 3x + 2y = 10
    
    # Multiply first equation by 3 → 6x + 9y = 36
    # Multiply second equation by 2 → 6x + 4y = 20
    # Subtract → 5y = 16 → y = 16 / 5
    
    a1, b1, c1 = 2, 3, 12
    a2, b2, c2 = 3, 2, 10
    
    # Make coefficients of x equal by multiplying:
    a1 = a1 * 3
    b1 = b1 * 3
    c1 = c1 * 3
    
    a2 = a2 * 2
    b2 = b2 * 2
    c2 = c2 * 2
    
    # Subtract equations:
    y = (c1 - c2) / (b1 - b2)
    x = (12 - 3 * y) / 2
    
    return x, y

# 3️⃣ Matrix Method
def matrix_method():
    solution = np.linalg.solve(A, B)
    x, y = solution
    return x, y

# ✅ Test All Methods
x_sub, y_sub = substitution_method()
x_elim, y_elim = elimination_method()
x_mat, y_mat = matrix_method()

# ✅ Print Results
print("----- Substitution Method -----")
print(f"Number of days Machine A works: {x_sub:.2f}")
print(f"Number of days Machine B works: {y_sub:.2f}")

print("\n----- Elimination Method -----")
print(f"Number of days Machine A works: {x_elim:.2f}")
print(f"Number of days Machine B works: {y_elim:.2f}")

print("\n----- Matrix Method -----")
print(f"Number of days Machine A works: {x_mat:.2f}")
print(f"Number of days Machine B works: {y_mat:.2f}")