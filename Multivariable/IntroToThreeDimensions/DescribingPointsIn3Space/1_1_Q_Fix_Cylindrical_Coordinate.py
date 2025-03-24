import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create the figure and 3D axes
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Parameters for the cylindrical coordinates
z_values = np.linspace(-5, 5, 100)
theta_values = np.linspace(0, 2 * np.pi, 100)
r_values = np.linspace(1, 3, 100)

# Fix z: Draw a circle in the XY plane
z_fixed = 1.0  # Fix z at this value
r_circle = 2.0  # Radius of the circle
theta_circle = np.linspace(0, 2 * np.pi, 100)
x_circle = r_circle * np.cos(theta_circle)
y_circle = r_circle * np.sin(theta_circle)
ax.plot(x_circle, y_circle, z_fixed, label='Fixed z (Circle)')

# Fix theta (delta): Draw a straight line in cylindrical coordinates
theta_fixed = np.pi / 4  # Fix theta at this value
x_line = r_values * np.cos(theta_fixed)
y_line = r_values * np.sin(theta_fixed)
ax.plot(x_line, y_line, z_values, label='Fixed θ (Line)')

# Fix r: Draw a vertical cylindrical surface
r_fixed = 2.0  # Fix r at this value
theta_grid, z_grid = np.meshgrid(theta_values, z_values)
x_cylinder = r_fixed * np.cos(theta_grid)
y_cylinder = r_fixed * np.sin(theta_grid)
ax.plot_surface(x_cylinder, y_cylinder, z_grid, alpha=0.3, cmap='viridis', label='Fixed r (Cylinder)')

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Set the title and show the plot
ax.set_title('Cylindrical Coordinates with Fixed z, θ, and r')
plt.show()