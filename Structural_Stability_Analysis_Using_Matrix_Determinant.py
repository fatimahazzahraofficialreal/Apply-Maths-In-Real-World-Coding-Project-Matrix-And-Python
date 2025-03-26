import numpy as np

def calculate_determinant(matrix):
    """Calculate the determinant of a given matrix."""
    return np.linalg.det(matrix)

# Example: Stability analysis for a truss structure represented by a 3x3 matrix
truss_matrix = np.array([[4, 2, 1],
                         [2, 3, 1],
                         [1, 1, 2]])

determinant = calculate_determinant(truss_matrix)

if determinant == 0:
    print("The structure is unstable or degenerate (determinant = 0).")
else:
    print(f"The structure is stable. Determinant value: {determinant:.2f}")
