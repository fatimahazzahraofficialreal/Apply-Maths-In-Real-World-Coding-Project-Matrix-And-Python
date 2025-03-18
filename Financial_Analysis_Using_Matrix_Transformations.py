import numpy as np

def swap_rows(matrix, i, j):
    """Swap row i and row j in a matrix"""
    matrix[[i, j]] = matrix[[j, i]]
    return matrix

def multiply_row(matrix, i, scalar):
    """Multiply row i by a scalar"""
    matrix[i] = matrix[i] * scalar
    return matrix

def add_multiple_of_row(matrix, i, j, scalar):
    """Add (scalar * row j) to row i"""
    matrix[i] = matrix[i] + scalar * matrix[j]
    return matrix

def swap_columns(matrix, i, j):
    """Swap column i and column j in a matrix"""
    matrix[:, [i, j]] = matrix[:, [j, i]]
    return matrix

def add_multiple_of_column(matrix, i, j, scalar):
    """Add (scalar * column j) to column i"""
    matrix[:, i] = matrix[:, i] + scalar * matrix[:, j]
    return matrix

# Example: Investment Portfolio Analysis
# Rows represent different investment types (e.g., stocks, bonds, real estate)
# Columns represent different time periods or financial metrics
financial_matrix = np.array([[5000, 7000, 9000],  # Investment in Stocks over time
                             [3000, 4000, 6000],  # Investment in Bonds
                             [2000, 3000, 5000]], dtype=float)  # Investment in Real Estate

print("Initial Financial Matrix:")
print(financial_matrix)

# Example Operations:

# Adjusting investment allocation by shifting investment rows (Swap row 1 and 2)
financial_matrix = swap_rows(financial_matrix, 0, 1)
print("\nAfter Swapping Stock and Bond Investment Rows:")
print(financial_matrix)

# Scaling investment in stocks by a factor of 1.1 (e.g., increase stock investments by 10%)
financial_matrix = multiply_row(financial_matrix, 0, 1.1)
print("\nAfter Increasing Stock Investments by 10%:")
print(financial_matrix)

# Redistributing a portion of real estate investment into stocks (Adding 50% of real estate to stocks)
financial_matrix = add_multiple_of_row(financial_matrix, 0, 2, 0.5)
print("\nAfter Redistributing 50% of Real Estate Investment to Stocks:")
print(financial_matrix)
