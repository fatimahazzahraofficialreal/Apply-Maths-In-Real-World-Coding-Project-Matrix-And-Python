import numpy as np
import matplotlib.pyplot as plt

# Define transformation matrices
def scaling_matrix(sx, sy):
    return np.array([[sx, 0], [0, sy]])

def rotation_matrix(theta):
    rad = np.radians(theta)
    return np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])

def reflection_matrix(axis):
    if axis == 'x':
        return np.array([[1, 0], [0, -1]])
    elif axis == 'y':
        return np.array([[-1, 0], [0, 1]])

def shearing_matrix(shx, shy):
    return np.array([[1, shx], [shy, 1]])

# Apply transformation
def transform(points, matrix):
    return np.dot(points, matrix.T)

# Original shape (square)
square = np.array([[1, 1], [1, -1], [-1, -1], [-1, 1], [1, 1]])  # Closed shape

# Choose transformation
transformation = scaling_matrix(2, 1.5)  # Example: Scaling by 2x in x-direction and 1.5x in y-direction
transformed_square = transform(square, transformation)

# Plot original and transformed shapes
plt.figure(figsize=(6,6))
plt.plot(square[:,0], square[:,1], 'bo-', label="Original")
plt.plot(transformed_square[:,0], transformed_square[:,1], 'ro-', label="Transformed")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()
plt.title("2D Linear Transformation")
plt.show()
