import cv2
import numpy as np
import os

# Load images and convert to grayscale
image_dir = "faces"  # Folder containing face images (same size)
image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg") or f.endswith(".png")]
image_data = []

for file in image_files:
    img = cv2.imread(os.path.join(image_dir, file), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (100, 100))  # Resize all to same size
    image_data.append(img.flatten())

image_matrix = np.array(image_data).T  # Each column is an image vector

# Compute mean face
mean_face = np.mean(image_matrix, axis=1).reshape(-1, 1)
A = image_matrix - mean_face  # Subtract mean

# Compute covariance matrix using trick (A.T @ A) for speed
cov_matrix = A.T @ A

# Eigen decomposition
eigenvalues, eigenvectors_temp = np.linalg.eig(cov_matrix)
eigenvectors = A @ eigenvectors_temp  # Back-project to original space

# Normalize eigenvectors (eigenfaces)
eigenfaces = eigenvectors / np.linalg.norm(eigenvectors, axis=0)

# Project images onto eigenface space
projected_images = eigenfaces.T @ A

def recognize_face(test_image_path):
    test_img = cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE)
    test_img = cv2.resize(test_img, (100, 100)).flatten().reshape(-1, 1)
    test_img = test_img - mean_face
    
    projected_test = eigenfaces.T @ test_img

    # Find closest match
    distances = [np.linalg.norm(projected_test - p) for p in projected_images.T]
    match_index = np.argmin(distances)

    return image_files[match_index], distances[match_index]

# Example usage
# matched_name, match_score = recognize_face("test_face.jpg")
# print(f"Best match: {matched_name}, Distance: {match_score}")
