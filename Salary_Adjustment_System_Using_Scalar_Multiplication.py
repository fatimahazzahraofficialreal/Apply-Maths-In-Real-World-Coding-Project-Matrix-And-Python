import numpy as np

def adjust_salaries(salary_matrix, multiplier):
    """Multiplies the salary matrix by a scalar value to adjust salaries."""
    return salary_matrix * multiplier

# Example: Employee salaries in different departments (in $)
salaries = np.array([[4000, 3500, 5000],  # Department A salaries
                      [4500, 3800, 5200],  # Department B salaries
                      [4700, 3900, 5400]]) # Department C salaries

increase_percentage = 1.10  # 10% salary increase
new_salaries = adjust_salaries(salaries, increase_percentage)

print("Updated salaries after 10% increase:\n", new_salaries)
