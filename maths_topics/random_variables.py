import numpy as np

# Define the outcomes and their probabilities
outcomes = [1, 2, 3, 4, 5, 6]
probabilities = [1/6] * 6

# Expected Value Calculation
expected_value = sum(outcomes[i] * probabilities[i] for i in range(len(outcomes)))

# Variance Calculation
variance = sum(outcomes[i]**2 * probabilities[i] for i in range(len(outcomes))) - expected_value**2

# Standard Deviation Calculation
std_deviation = np.sqrt(variance)

# Print Results
print(f"Expected Value of Dice Roll: {expected_value:.2f}")
print(f"Variance of Dice Roll: {variance:.2f}")
print(f"Standard Deviation of Dice Roll: {std_deviation:.2f}")