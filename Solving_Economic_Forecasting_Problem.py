import numpy as np

def gauss_jordan_elimination(matrix, results):
    n = len(matrix)
    augmented_matrix = np.hstack((matrix, results.reshape(-1, 1)))
    
    # Applying Gauss-Jordan Elimination to get RREF (Reduced Row Echelon Form)
    for i in range(n):
        # Pivoting to make sure the diagonal element is non-zero
        if augmented_matrix[i][i] == 0:
            for j in range(i+1, n):
                if augmented_matrix[j][i] != 0:
                    augmented_matrix[[i, j]] = augmented_matrix[[j, i]]
                    break
        
        # Normalize the pivot row
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i][i]
        
        # Eliminate other rows
        for j in range(n):
            if i != j:
                factor = augmented_matrix[j][i]
                augmented_matrix[j] -= factor * augmented_matrix[i]
    
    # Extracting solutions from the augmented matrix
    solution = augmented_matrix[:, -1]
    return solution

# Example Scenario: Economic Sectors Interdependency
# A is the matrix representing inter-industry dependencies
A = np.array([[0.4, 0.3, 0.3],  # Sector 1 depends on 40% of itself, 30% on sector 2, and 30% on sector 3
              [0.2, 0.6, 0.2],  # Sector 2 depends on 20% of sector 1, 60% on itself, and 20% on sector 3
              [0.3, 0.3, 0.4]]) # Sector 3 depends on 30% of sector 1, 30% on sector 2, and 40% on itself

# Target production levels (total economic demand)
total_demand = np.array([100, 200, 150])  # Total demand in each sector

# Solving the system to get the required production levels
required_production = gauss_jordan_elimination(A, total_demand)
print("Required production levels in each sector to meet the total economic demand:")
print(required_production)
