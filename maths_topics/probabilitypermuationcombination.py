import math

# Probability Calculation
def probability(event_outcomes, sample_space):
    return event_outcomes / sample_space

# Permutation
def permutation(n, r):
    return math.factorial(n) // math.factorial(n - r)

# Combination
def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Real-world Example - Tesla Defective Parts Prediction
total_parts = 1000
defective_parts = 150

# Probability that a part is defective
prob_defective = probability(defective_parts, total_parts)
print(f"Probability of selecting a defective part: {prob_defective:.2f}")

# Probability that 3 randomly selected parts are all defective
# P(A ∩ B ∩ C) = P(A) * P(B|A) * P(C|A ∩ B)
prob_all_defective = (
    (defective_parts / total_parts) *
    ((defective_parts - 1) / (total_parts - 1)) *
    ((defective_parts - 2) / (total_parts - 2))
)
print(f"Probability of selecting 3 defective parts in a row: {prob_all_defective:.5f}")

# Permutation Example - Arranging 3 defective parts out of 5
perm = permutation(5, 3)
print(f"Permutation of 5 defective parts taken 3 at a time: {perm}")

# Combination Example - Choosing 3 defective parts from 5
comb = combination(5, 3)
print(f"Combination of 5 defective parts taken 3 at a time: {comb}")
