import numpy as np
import matplotlib.pyplot as plt

# Define two linearly independent basis vectors in R²
v1 = np.array([1, 2])
v2 = np.array([2, 1])
origin = np.array([0, 0])

# Grid of scalar values for linear combinations
scalars = np.linspace(-2, 2, 10)
points = []

# Create span (all linear combinations)
for a in scalars:
    for b in scalars:
        point = a * v1 + b * v2
        points.append(point)

points = np.array(points)

# Plot the basis vectors
plt.figure(figsize=(8, 8))
plt.quiver(*origin, *v1, angles='xy', scale_units='xy', scale=1, color='red', label='v1 = [1, 2]')
plt.quiver(*origin, *v2, angles='xy', scale_units='xy', scale=1, color='blue', label='v2 = [2, 1]')

# Plot the span
plt.scatter(points[:, 0], points[:, 1], alpha=0.3, label='Span of v1 & v2')

# Example: show a unique combination
target = np.array([3, 5])
A = np.column_stack((v1, v2))
coeffs = np.linalg.solve(A, target)
reconstructed = coeffs[0] * v1 + coeffs[1] * v2

plt.plot(target[0], target[1], 'go', label='Target Vector [3, 5]')
plt.text(target[0]+0.2, target[1], f'{coeffs[0]:.2f}·v1 + {coeffs[1]:.2f}·v2')

# Formatting
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.axhline(0, color='grey', lw=1)
plt.axvline(0, color='grey', lw=1)
plt.grid(True)
plt.gca().set_aspect('equal')
plt.legend()
plt.title("Visualizing Basis, Span, and Unique Linear Combination")
plt.show()