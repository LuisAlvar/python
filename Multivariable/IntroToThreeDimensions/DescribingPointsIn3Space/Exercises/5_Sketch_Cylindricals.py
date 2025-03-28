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

# Setup for cylindrical 
theta = np.linspace(0, 2 * np.pi, 100)        # provide a circle area of 2pi
z_clinder = np.linspace(-10, 10, 100)         # cylinder height up and down
Theta, Z_cyl = np.meshgrid(theta, z_clinder)  # makes a cylindrical grid

# Cylinder with radius 1 centered at (0,0)
X_cylinder = 1 * np.cos(Theta)                # Parametric equation for cylinder X = rcos
Y_cylinder = 1 * np.sin(Theta)                # Parametric equation for clinder Y = rsin
ax.plot_surface(X_cylinder, Y_cylinder, Z_cyl, alpha=0.5, color='blue', label='Cylinder: radius=1')

# Add text labels for r = 1
ax.text(2, 0, 0, 'r = 1', color='blue', fontsize=10)

# Cylinder with radius 3 centered at (0,0)
X_cylinder = 3 * np.cos(Theta)                # Parametric equation for cylinder X = rcos
Y_cylinder = 3 * np.sin(Theta)                # Parametric equation for clinder Y = rsin
ax.plot_surface(X_cylinder, Y_cylinder, Z_cyl, alpha=0.5, color='red', label='Cylinder: radius=3')

# Add text labels for r = 1
ax.text(5, -5, 0, 'r = 3', color='red', fontsize=10)

# Cylinder with radius 5 centered at (0,0)
X_cylinder = 5 * np.cos(Theta)                # Parametric equation for cylinder X = rcos
Y_cylinder = 5 * np.sin(Theta)                # Parametric equation for clinder Y = rsin
ax.plot_surface(X_cylinder, Y_cylinder, Z_cyl, alpha=0.5, color='grey', label='Cylinder: radius=5')

# Add text labels for r = 1
ax.text(10, -10, 0, 'r = 5', color='grey', fontsize=10)

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
ax.set_title('3D Plot of Cylinders')

# Show the plot
plt.show()