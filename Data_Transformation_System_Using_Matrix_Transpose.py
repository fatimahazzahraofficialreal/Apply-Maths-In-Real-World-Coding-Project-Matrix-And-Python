import numpy as np

def transpose_matrix(matrix):
    """Transpose the given matrix (rows become columns and vice versa)."""
    return np.transpose(matrix)

# Example: Dataset of students' test scores in different subjects
scores_matrix = np.array([[85, 78, 92],   # Student 1 scores in Math, Science, English
                          [88, 76, 94],   # Student 2 scores in Math, Science, English
                          [90, 82, 88]])  # Student 3 scores in Math, Science, English

# Transpose the matrix to change perspective: subjects become rows, students become columns
transposed_scores = transpose_matrix(scores_matrix)
print("Transposed Matrix (Subjects vs Students):\n", transposed_scores)
