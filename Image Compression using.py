import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def compress_image_svd(image_path, k):
    # Load image and convert to grayscale
    img = Image.open(image_path).convert('L')
    img_matrix = np.array(img)

    # Apply SVD
    U, S, Vt = np.linalg.svd(img_matrix, full_matrices=False)

    # Keep only top-k singular values
    S_reduced = np.diag(S[:k])
    U_reduced = U[:, :k]
    Vt_reduced = Vt[:k, :]

    # Reconstruct the image
    compressed_img = np.dot(U_reduced, np.dot(S_reduced, Vt_reduced))

    # Show original vs compressed
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(img_matrix, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title(f"Compressed (k={k})")
    plt.imshow(compressed_img, cmap='gray')
    plt.axis('off')

    plt.show()

# Example usage
compress_image_svd("your_image.jpg", k=50)
