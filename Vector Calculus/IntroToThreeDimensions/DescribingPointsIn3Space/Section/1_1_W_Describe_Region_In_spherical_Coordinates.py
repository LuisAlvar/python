import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the spherical coordinate ranges
phi = np.linspace(0, np.pi/2, 50)  # Polar angle (ϕ)
theta = np.linspace(0, 3*np.pi/2, 50)  # Azimuthal angle (θ)
phi, theta = np.meshgrid(phi, theta)

# Cartesian coordinates for inner and outer surfaces
x_inner = 2 * np.sin(phi) * np.cos(theta)
y_inner = 2 * np.sin(phi) * np.sin(theta)
z_inner = 2 * np.cos(phi)

x_outer = 3 * np.sin(phi) * np.cos(theta)
y_outer = 3 * np.sin(phi) * np.sin(theta)
z_outer = 3 * np.cos(phi)

# Prepare vertices for the shell boundaries
vertices = []
for i in range(len(phi) - 1):
    for j in range(len(theta) - 1):
        # Inner surface vertices
        v1 = [x_inner[i, j], y_inner[i, j], z_inner[i, j]]
        v2 = [x_inner[i+1, j], y_inner[i+1, j], z_inner[i+1, j]]
        v3 = [x_inner[i+1, j+1], y_inner[i+1, j+1], z_inner[i+1, j+1]]
        v4 = [x_inner[i, j+1], y_inner[i, j+1], z_inner[i, j+1]]

        # Outer surface vertices
        v5 = [x_outer[i, j], y_outer[i, j], z_outer[i, j]]
        v6 = [x_outer[i+1, j], y_outer[i+1, j], z_outer[i+1, j]]
        v7 = [x_outer[i+1, j+1], y_outer[i+1, j+1], z_outer[i+1, j+1]]
        v8 = [x_outer[i, j+1], y_outer[i, j+1], z_outer[i, j+1]]

        # Faces connecting inner and outer surfaces
        vertices.extend([[v1, v2, v6, v5], [v2, v3, v7, v6], [v3, v4, v8, v7], [v4, v1, v5, v8]])

# Create the 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Add the filled shell
shell = Poly3DCollection(vertices, alpha=0.3, facecolors='cyan', edgecolors='k')
ax.add_collection3d(shell)

# Labels and aspect ratio
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Filled Solid Shell')
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio

plt.tight_layout()
plt.show()