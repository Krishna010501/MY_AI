import numpy as np
from scipy import stats

# Data - Tesla daily output
data = [120, 140, 150, 130, 160, 140, 150]

# Mean
mean = np.mean(data)

# Median
median = np.median(data)

# Mode
mode = stats.mode(data).mode[0]

# Range
data_range = max(data) - min(data)

# Variance
variance = np.var(data)

# Standard Deviation
std_dev = np.std(data)

# Quartiles
q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)  # Median
q3 = np.percentile(data, 75)

# Results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Range: {data_range}")
print(f"Variance: {variance:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"Q1: {q1}, Q2: {q2}, Q3: {q3}")