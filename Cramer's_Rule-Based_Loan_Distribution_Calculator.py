import numpy as np

def cramer_rule(coeff_matrix, constants):
    det_main = np.linalg.det(coeff_matrix)
    
    if det_main == 0:
        raise ValueError("The system has no unique solution (determinant is 0).")
    
    solutions = []
    n = coeff_matrix.shape[0]
    
    for i in range(n):
        temp_matrix = coeff_matrix.copy()
        temp_matrix[:, i] = constants
        det_temp = np.linalg.det(temp_matrix)
        solution = det_temp / det_main
        solutions.append(solution)
    
    return solutions

# Example Use Case: Loan Distribution
# Suppose the bank must distribute loans in a way that satisfies certain constraints.
# x = amount for Sector A, y = amount for Sector B, z = amount for Sector C
coeff_matrix = np.array([[3, 2, 1],   # Constraints from capital availability
                         [1, 2, 3],   # Constraints from market demand
                         [2, 1, 2]])  # Constraints from investment limits

constants = np.array([100, 120, 110])  # Total loan limits for each constraint

try:
    loan_distribution = cramer_rule(coeff_matrix, constants)
    print("Optimal loan distribution (in million dollars):")
    print(f"Sector A: ${loan_distribution[0]:.2f}M")
    print(f"Sector B: ${loan_distribution[1]:.2f}M")
    print(f"Sector C: ${loan_distribution[2]:.2f}M")
except ValueError as e:
    print(e)
