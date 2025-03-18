import numpy as np

def gauss_jordan_inverse(matrix):
    n = len(matrix)
    augmented = np.hstack((matrix, np.identity(n)))
    
    for i in range(n):
        if augmented[i][i] == 0:
            for j in range(i+1, n):
                if augmented[j][i] != 0:
                    augmented[[i, j]] = augmented[[j, i]]
                    break
        
        augmented[i] = augmented[i] / augmented[i][i]
        
        for j in range(n):
            if i != j:
                augmented[j] = augmented[j] - augmented[j][i] * augmented[i]
    
    return augmented[:, n:]

def optimize_production(A, demand):
    A_inv = gauss_jordan_inverse(A)
    materials_needed = np.dot(A_inv, demand)
    return materials_needed

# Example case:
# Each row in A represents the amount of raw materials needed for one unit of a product.
A = np.array([[2, 1],  # Product 1 requires 2 units of material A and 1 unit of material B
              [1, 3]]) # Product 2 requires 1 unit of material A and 3 units of material B

demand = np.array([100, 150])  # Production target: 100 units of product 1 and 150 units of product 2

materials = optimize_production(A, demand)
print("Amount of raw materials needed:")
print(materials)
