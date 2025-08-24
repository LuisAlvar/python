import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create the figure and 3D axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Define spherical coordinates
r = 3  # Radius
theta = np.pi / 4  # Azimuthal angle (45 degrees in XY-plane)
varphi = np.pi / 6  # Polar angle (30 degrees from Z-axis)

# Convert spherical to Cartesian coordinates
x = r * np.sin(varphi) * np.cos(theta)  # Projection in the X direction
y = r * np.sin(varphi) * np.sin(theta)  # Projection in the Y direction
z = r * np.cos(varphi)                  # Projection in the Z direction

# Plot radius (hypotenuse)
ax.plot([0, x], [0, y], [0, z], label='Radius (ρ)', color='blue')

# Show \(\theta\) angle in XY-plane
x_theta = r * np.sin(varphi)  # Length of the projection in the XY plane
ax.plot([0, x_theta], [0, 0], [0, 0], color='orange', linestyle='--', label='Projection of θ')
ax.text(x_theta / 2, 0, 0, r'$\theta$', color='orange', fontsize=12)

# Show \(\varphi\) angle from Z-axis
ax.plot([0, 0], [0, 0], [0, z], color='red', linestyle='--', label='Projection of ϕ')
ax.text(0, 0, z / 2, r'$\varphi$', color='red', fontsize=12)

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Visualizing θ and ϕ in Spherical Coordinates')
ax.legend()

# Show the plot
plt.show()