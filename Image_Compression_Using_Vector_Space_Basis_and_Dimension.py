import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from skimage.color import rgb2gray
from skimage import io

# Load and convert image to grayscale
image = io.imread("your_image.jpg")  # Replace with actual image path
gray_image = rgb2gray(image)

# Convert image to matrix
image_matrix = np.array(gray_image)

# Apply PCA to reduce dimensions while preserving key basis vectors
num_components = 50  # Adjust for different compression levels
pca = PCA(n_components=num_components)
transformed = pca.fit_transform(image_matrix)
compressed = pca.inverse_transform(transformed)

# Plot original and compressed images
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image_matrix, cmap="gray")
axes[0].set_title("Original Image")
axes[1].imshow(compressed, cmap="gray")
axes[1].set_title(f"Compressed Image ({num_components} components)")
plt.show()
