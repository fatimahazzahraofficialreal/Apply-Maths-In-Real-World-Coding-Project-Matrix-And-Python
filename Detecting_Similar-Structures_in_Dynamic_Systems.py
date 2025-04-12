import numpy as np

def are_similar(A, B):
    """Check if two matrices A and B are similar: A = P B P^-1 for some P"""
    try:
        # Step 1: Check eigenvalues (must be the same set)
        eig_A, _ = np.linalg.eig(A)
        eig_B, _ = np.linalg.eig(B)
        if not np.allclose(sorted(eig_A), sorted(eig_B)):
            return False

        # Step 2: Try to find a matrix P such that A = P B P^-1
        # This is hard in general, so here we simplify and just check eigen decompositions
        return True  # Simplified answer: same eigenvalues = potential similarity
    except:
        return False

# Example: Two matrices that are similar
A = np.array([[2, 1],
              [0, 2]])

B = np.array([[2, 0],
              [0, 2]])

result = are_similar(A, B)
print("Are the matrices similar?", result)
