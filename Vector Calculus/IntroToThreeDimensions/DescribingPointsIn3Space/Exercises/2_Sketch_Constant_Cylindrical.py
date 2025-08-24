import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define ranges and resolution
x_range = np.linspace(-10, 10, 100)
y_range = np.linspace(-10, 10, 100)
z_range = np.linspace(-10, 10, 100)

# Plane z = -2
X, Y = np.meshgrid(x_range, y_range)
Z_plane = -2 * np.ones_like(X)
ax.plot_surface(X, Y, Z_plane, alpha=0.5, color='blue', label='Plane: z = -2')

# Cylinder with radius 4 centered at (0,0)
theta = np.linspace(0, 2 * np.pi, 100)
z_cylinder = np.linspace(-10, 10, 100)  # Cylinder height
Theta, Z_cyl = np.meshgrid(theta, z_cylinder)
X_cylinder = 4 * np.cos(Theta)  # Parametric equation for cylinder X
Y_cylinder = 4 * np.sin(Theta)  # Parametric equation for cylinder Y
ax.plot_surface(X_cylinder, Y_cylinder, Z_cyl, alpha=0.5, color='red', label='Cylinder: radius=4')

# Ray from origin in direction -3pi/4
theta_ray = -3 * np.pi / 4
r_ray = np.linspace(0, 10, 100)  # Ray length (variable radius)
z_ray = np.linspace(0, 10, 100)  # Varying z-coordinate
x_ray = r_ray * np.cos(theta_ray)
y_ray = r_ray * np.sin(theta_ray)
ax.plot(x_ray, y_ray, z_ray, color='green', label='Ray: direction=-3π/4')

# Add legend
ax.legend(loc='upper right')

# Customize axes and ticks
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])
ax.set_xticks(np.arange(-10, 12, 2))  # Tick marks at intervals of 2
ax.set_yticks(np.arange(-10, 12, 2))  # Tick marks at intervals of 2
ax.set_zticks(np.arange(-10, 12, 2))  # Tick marks at intervals of 2
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Plot of Plane, Cylinder, and Ray')

# Show the plot
plt.show()