import numpy as np

def compare_expenses(expense1, expense2):
    """Subtracts two expense matrices to analyze financial changes."""
    difference = np.array(expense2) - np.array(expense1)
    return difference

# Example: Monthly expenses (rows: Rent, Salaries, Utilities)
jan_expenses = np.array([[5000, 2000, 1500],  # Rent, Salaries, Utilities (January)
                         [3000, 2500, 1800]])

feb_expenses = np.array([[5200, 2100, 1600],  # Rent, Salaries, Utilities (February)
                         [2900, 2700, 1750]])

expense_difference = compare_expenses(jan_expenses, feb_expenses)
print("Expense changes from January to February:\n", expense_difference)
