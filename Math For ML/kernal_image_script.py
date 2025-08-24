import numpy as np
import matplotlib.pyplot as plt

# Define a linear transformation matrix
A = np.array([[2, 1],
              [0, 0]])  # This flattens all vectors onto the x-axis

# Create a grid of vectors in R^2
x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
X, Y = np.meshgrid(x, y)
vectors = np.stack([X.ravel(), Y.ravel()], axis=1)

# Apply the transformation
transformed = vectors @ A.T

# Plot original vectors
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.quiver(vectors[:, 0], vectors[:, 1], vectors[:, 0], vectors[:, 1], color='gray', alpha=0.5)
plt.title("Original Vectors in $V$")
plt.axis('equal')
plt.grid(True)

# Plot transformed vectors
plt.subplot(1, 2, 2)
plt.quiver(vectors[:, 0], vectors[:, 1], transformed[:, 0], transformed[:, 1], color='blue', alpha=0.7)
plt.title("Transformed Vectors in $W = \Phi(V)$")
plt.axis('equal')
plt.grid(True)

plt.suptitle("Linear Transformation: Image and Kernel")
plt.tight_layout()
plt.show()