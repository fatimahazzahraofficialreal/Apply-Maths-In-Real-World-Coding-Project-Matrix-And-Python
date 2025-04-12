import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def is_orthogonal(matrix):
    return np.allclose(np.dot(matrix.T, matrix), np.identity(matrix.shape[0]))

def rotate_points(points, rotation_matrix):
    return np.dot(rotation_matrix, points)

# Define 3D object (a simple cube)
cube = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
]).T  # Shape: (3, 8)

# Rotation matrix around Z-axis by 90 degrees
theta = np.radians(90)
rotation_z = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta),  np.cos(theta), 0],
    [0, 0, 1]
])

# Check if rotation matrix is orthogonal
print("Is the rotation matrix orthogonal?", is_orthogonal(rotation_z))

# Apply rotation
rotated_cube = rotate_points(cube, rotation_z)

# Plot original and rotated cube
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(*cube, c='blue', label='Original')
ax.scatter(*rotated_cube, c='red', label='Rotated')
ax.legend()
ax.set_title("3D Cube Rotation with Orthogonal Matrix")
plt.show()
