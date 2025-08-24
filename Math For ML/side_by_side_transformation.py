import numpy as np
import matplotlib.pyplot as plt

# Create a grid of vectors
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)
vectors = np.stack([X.ravel(), Y.ravel()])

# Define transformation matrices
rotation_angle = np.pi / 4  # 45 degrees
R = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
              [np.sin(rotation_angle),  np.cos(rotation_angle)]])

P = np.array([[1, 0],  # Projection onto x-axis
              [0, 0]])

S = np.array([[2, 0],  # Scaling: x2 in x, 1/2 in y
              [0, 0.5]])

# Apply transformations
rotated = R @ vectors
projected = P @ vectors
scaled = S @ vectors

# Plotting
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
titles = ['Rotation (45°)', 'Projection (onto x-axis)', 'Scaling (x2, y/2)']
transformed_sets = [rotated, projected, scaled]

for ax, title, transformed in zip(axes, titles, transformed_sets):
    ax.quiver(vectors[0], vectors[1], transformed[0], transformed[1],
              angles='xy', scale_units='xy', scale=1, color='blue', alpha=0.6)
    ax.set_title(title)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.grid(True)

plt.tight_layout()
plt.show()