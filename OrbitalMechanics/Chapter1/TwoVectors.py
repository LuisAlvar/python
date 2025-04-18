import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the vectors
a = np.array([1, 6, 18])
b = np.array([42, -69, 98])

# Define the origin
origin = np.array([0, 0, 0])

# Calculate the plane (shaded area) spanned by a and b
plane_points = np.array([
    origin,      # (0, 0, 0)
    a,           # Vector a
    b,           # Vector b
    a + b        # Endpoint of the parallelogram spanned by a and b
])

# Plotting the 3D coordinate system
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vectors
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', label='Vector a')
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='g', label='Vector b')

# Add annotations for the vectors with their values
ax.text(a[0], a[1], a[2], f'a {tuple(a)}', color='r', fontsize=10)
ax.text(b[0], b[1], b[2], f'b {tuple(b)}', color='g', fontsize=10)

# Shade the area between the vectors (plane)
verts = [plane_points[[0, 1, 3, 2]]]  # Define the vertices of the parallelogram
ax.add_collection3d(Poly3DCollection(verts, alpha=0.3, color='purple'))

# Set axes labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Set aspect ratio for better visualization
ax.set_box_aspect([1, 1, 1])

# Add legend
ax.legend()

plt.show()
