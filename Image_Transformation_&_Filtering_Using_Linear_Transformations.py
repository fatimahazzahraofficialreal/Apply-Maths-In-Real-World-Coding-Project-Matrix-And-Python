import numpy as np
import matplotlib.pyplot as plt
import cv2  

# Load and convert image to grayscale
image = cv2.imread("your_image.jpg", cv2.IMREAD_GRAYSCALE)  # Replace with actual image path

# Define linear transformation matrices
def apply_transformation(image, matrix):
    rows, cols = image.shape
    transformed = cv2.warpAffine(image, matrix, (cols, rows))
    return transformed

# Scaling (resizing)
scale_matrix = np.float32([[1.5, 0, 0], [0, 1.5, 0]])

# Rotation (45 degrees)
angle = np.radians(45)
rotation_matrix = np.float32([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0]])

# Shearing
shear_matrix = np.float32([[1, 0.5, 0], [0.5, 1, 0]])

# Apply transformations
scaled_image = apply_transformation(image, scale_matrix)
rotated_image = apply_transformation(image, rotation_matrix)
sheared_image = apply_transformation(image, shear_matrix)

# Edge detection using Sobel filter (another linear transformation)
edges = cv2.Sobel(image, cv2.CV_64F, 1, 1, ksize=5)

# Plot results
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes[0, 0].imshow(image, cmap="gray")
axes[0, 0].set_title("Original Image")
axes[0, 1].imshow(scaled_image, cmap="gray")
axes[0, 1].set_title("Scaled Image")
axes[1, 0].imshow(rotated_image, cmap="gray")
axes[1, 0].set_title("Rotated Image")
axes[1, 1].imshow(sheared_image, cmap="gray")
axes[1, 1].set_title("Sheared Image")
plt.show()

# Display edge detection
plt.imshow(edges, cmap="gray")
plt.title("Edge Detection using Sobel Filter")
plt.show()
