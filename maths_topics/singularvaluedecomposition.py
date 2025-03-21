'''Singular Value Decomposition (SVD)

 1. What is Singular Value Decomposition (SVD)?

👉 Singular Value Decomposition (SVD) is a way to decompose (break down) a matrix into three simpler matrices:

A = U \cdot \Sigma \cdot V^T

where:
	•	A → Original matrix
	•	U → Left singular vectors (Orthogonal matrix)
	•	Σ (Sigma) → Diagonal matrix of singular values
	•	Vᵀ → Right singular vectors (Orthogonal matrix transpose)
    
   ---> Why is SVD Important?

👉 Machine Learning:
	•	Dimensionality reduction → PCA
	•	Noise reduction → Signal processing

👉 Natural Language Processing (NLP):
	•	Latent Semantic Analysis (LSA) → Document similarity

👉 Image Processing:
	•	Image compression → JPEG format'''

import numpy as np

# Define matrix A
A = np.array([[1, 2], [3, 4], [5, 6]])

# Perform SVD
U, S, VT = np.linalg.svd(A)

# Convert S into a diagonal matrix
S_diag = np.zeros((A.shape[0], A.shape[1]))
np.fill_diagonal(S_diag, S)

# Reconstruct matrix
A_reconstructed = U @ S_diag @ VT

# Print Results
print("Matrix U:\n", U)
print("Singular Values:\n", S)
print("Matrix V^T:\n", VT)
print("\nReconstructed Matrix:\n", A_reconstructed)