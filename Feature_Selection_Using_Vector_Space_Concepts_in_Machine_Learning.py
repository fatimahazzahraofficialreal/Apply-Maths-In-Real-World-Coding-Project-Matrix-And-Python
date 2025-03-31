import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load the dataset (Iris dataset as an example)
data = load_iris()
X = data.data  # Feature matrix

# Apply PCA to reduce dimensions from 4 to 2
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Explained variance ratio
explained_variance = pca.explained_variance_ratio_

# Plot the transformed data
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=data.target, cmap='viridis', edgecolors='k')
plt.xlabel(f'Principal Component 1 ({explained_variance[0]:.2%} variance)')
plt.ylabel(f'Principal Component 2 ({explained_variance[1]:.2%} variance)')
plt.title('Feature Reduction Using PCA (Vector Space Basis)')
plt.colorbar(label="Target Classes")
plt.show()
