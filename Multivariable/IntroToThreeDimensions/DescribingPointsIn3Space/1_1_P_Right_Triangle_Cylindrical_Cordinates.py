import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given point (r, delta in radians, z)
r = 5
delta = np.pi / 4  # 45 degrees
z = 3

# Conversion to cylindrical coordinates
x = r * np.cos(delta)
y = r * np.sin(delta)

# Calculate distances
distance_origin = np.sqrt(x**2 + y**2 + z**2)

# Create figure and 3D axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the cylindrical point
ax.scatter(x, y, z, color='red', label=f"Point ({x:.2f}, {y:.2f}, {z:.2f})")

# Plot the projection on the xy-plane
ax.scatter(x, y, 0, color='blue', label=f"Projection ({x:.2f}, {y:.2f}, 0)")

# Plot the right triangle edges
ax.plot([0, x], [0, y], [0, 0], color='green', linestyle='--', label="Base (xy-plane)")
ax.plot([x, x], [y, y], [0, z], color='orange', linestyle='--', label="Height (z-axis)")
ax.plot([0, x], [0, y], [0, z], color='purple', label=f"Hypotenuse = {distance_origin:.2f}")

# Customize the plot
ax.set_xlim(0, r + 2)
ax.set_ylim(0, r + 2)
ax.set_zlim(0, z + 2)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Right Triangle from Cylindrical Point to Origin")
ax.legend()

plt.tight_layout()
plt.show()