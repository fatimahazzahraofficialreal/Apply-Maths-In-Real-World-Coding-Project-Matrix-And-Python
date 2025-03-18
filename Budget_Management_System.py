import numpy as np

def add_budgets(budget1, budget2):
    return np.add(budget1, budget2)

# Example: Monthly budgets for two departments
dept1_budget = np.array([
    [5000, 2000, 1500],  # Rent, Salaries, Utilities
    [3000, 2500, 1200]   # Equipment, Marketing, Miscellaneous
])

dept2_budget = np.array([
    [4000, 2200, 1300],
    [3500, 2000, 1000]
])

total_budget = add_budgets(dept1_budget, dept2_budget)

print("Total Combined Budget:")
print(total_budget)
