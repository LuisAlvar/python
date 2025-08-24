# To plot the planes (z=-2), (x=4), and (y=-5) on the same 3D graph in Python, we
# can use Matplotlib's Axes3D module. Here's an approach to get it done: 
# 
# Steps to Plot
# 1. Set up the figure adn axis for 3D plotting.
# 2. Define the ranges for each axes.
# 3. Create the surfaces for each plane.
# 4. Plot the planes and customize the graph.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define axis limits
x_range = np.linspace(-10, 10, 100)
y_range = np.linspace(-10, 10, 100)
z_range = np.linspace(-10, 10, 100)

# Generate meshgrid for x and y planes
X, Y = np.meshgrid(x_range, y_range)

# Plane z = -2
Z_plane = -2 * np.ones_like(X)
ax.plot_surface(X, Y, Z_plane, alpha=0.5, color='blue', label='Plane: z = -2')

# Plane x = 4
Y_plane, Z_plane = np.meshgrid(y_range, z_range)
X_plane = 4 * np.ones_like(Y_plane)
ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.5, color='red', label='Plane: x = 4')

# Plane y = -5
X_plane, Z_plane = np.meshgrid(x_range, z_range)
Y_plane = -5 * np.ones_like(X_plane)
ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.5, color='green', label='Plane: y = -5')

# Add text labels to the planes
ax.text(0, 0, -2, 'z = -2', color='black', fontsize=10)
ax.text(4, 0, 0, 'x = 4', color='black', fontsize=10)
ax.text(0, -5, 0, 'y = -5', color='black', fontsize=10)

# Add legend
ax.legend(loc='upper right')

# Customize axes and view
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

ax.set_xticks(np.arange(-10, 12, 2))  # Fewer tick values for X-axis
ax.set_yticks(np.arange(-10, 12, 2))  # Fewer tick values for Y-axis
ax.set_zticks(np.arange(-10, 12, 2))  # Fewer tick values for Z-axis

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Plot of Planes with Labels and Legend')

# Show the plot
plt.show()

# Explanation:
# 1. meshgrid generates a grid over which the planes are plotted
# 2. Color and Transparency (alpha) help differentiate the planes visually
# 3. The axis limites are set to ensure all planes are fully visible

