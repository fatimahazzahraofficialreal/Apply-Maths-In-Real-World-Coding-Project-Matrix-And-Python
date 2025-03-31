import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Sample stock data: Features (Moving Avg, Trading Volume, Price Change)
X = np.array([
    [50, 10000, 1.5],
    [52, 12000, 1.7],
    [48, 9500, 1.4],
    [55, 13000, 1.8],
    [49, 10500, 1.6]
])  # Predictor variables (potentially dependent features)

y = np.array([101, 105, 98, 110, 100])  # Stock closing prices

# Check for linear dependence using rank (if rank < number of features, they are dependent)
rank = np.linalg.matrix_rank(X)
print(f"Rank of feature matrix: {rank}, Number of features: {X.shape[1]}")
if rank < X.shape[1]:
    print("Some features are linearly dependent!")

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train a linear regression model
model = LinearRegression()
model.fit(X_scaled, y)

# Predict next day's price based on new data
new_data = np.array([[53, 11500, 1.65]])  # New day's features
new_data_scaled = scaler.transform(new_data)
predicted_price = model.predict(new_data_scaled)

print(f"Predicted stock price: {predicted_price[0]:.2f}")

# Plot feature relationships
plt.scatter(X[:, 0], y, label="Moving Avg vs Price")
plt.scatter(X[:, 1], y, label="Volume vs Price", marker="x")
plt.scatter(X[:, 2], y, label="Price Change vs Price", marker="s")
plt.xlabel("Feature Values")
plt.ylabel("Stock Price")
plt.legend()
plt.title("Stock Features vs Closing Price")
plt.show()
