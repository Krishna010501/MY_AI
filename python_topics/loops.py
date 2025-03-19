# Multiplication table from 1 to 5

# Outer loop for row numbers
for i in range(1, 6):
    # Inner loop for column numbers
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()  # Moves to the next row after completing a row

# Pattern printing using nested loops

n = 5
for i in range(1, n + 1):
    for j in range(i):
        print('*', end=' ')
    print()

