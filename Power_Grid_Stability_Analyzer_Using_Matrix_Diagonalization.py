import numpy as np

# Sample symmetric matrix representing connections in a power grid
# This could represent how strongly each node (e.g., substation) is connected
A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 3]])

# Diagonalize the matrix: A = P * D * P_inv
eig_vals, eig_vecs = np.linalg.eig(A)

# Create the diagonal matrix from eigenvalues
D = np.diag(eig_vals)

# Compute the inverse of eigenvectors matrix
P_inv = np.linalg.inv(eig_vecs)

# Verify diagonalization
A_reconstructed = eig_vecs @ D @ P_inv

print("Original matrix A:")
print(A)
print("\nEigenvalues (D):")
print(D)
print("\nEigenvectors (P):")
print(eig_vecs)
print("\nReconstructed A from diagonalization (should match original A):")
print(A_reconstructed)
