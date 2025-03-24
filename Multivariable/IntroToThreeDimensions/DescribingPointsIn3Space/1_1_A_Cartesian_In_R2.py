import numpy as np  # Import numpy library
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set axis limits
ax.set_xlim([-4, 4])  # X-axis depth
ax.set_ylim([-5, 5])  # Y-axis horizontal
ax.set_zlim([-2, 2])   # Z-axis vertical

# Plot the axes with colors
ax.quiver(0, 0, 0, 1, 0, 0, color='red', label='X-axis')   # X-axis (red)
ax.quiver(0, 0, 0, 0, 1, 0, color='green', label='Y-axis') # Y-axis (green)
ax.quiver(0, 0, 0, 0, 0, 1, color='blue', label='Z-axis')  # Z-axis (blue)

# Add a plane at Z=0
xx, yy = np.meshgrid(range(-4, 5), range(-5, 6))  # Mesh grid for X-Y plane
zz = np.zeros_like(xx)  # Z=0 for the plane
ax.plot_surface(xx, yy, zz, alpha=0.2, color='gray')  # Semi-transparent gray plane

# Add a 2D point in the X-Y plane
x_2d, y_2d, z_2d = 2, 3, 0  # Coordinates of the 2D point
ax.scatter(x_2d, y_2d, z_2d, color='purple', s=100, label='Point A (X, Y)')

# Add tracing lines to the point
# Line along X-axis from origin to the x-coordinate
ax.plot([0, x_2d], [0, 0], [0, 0], color='red', linestyle='--', label='X Trace')
# Line along Y-axis from the x-coordinate to the y-coordinate
ax.plot([x_2d, x_2d], [0, y_2d], [0, 0], color='green', linestyle='--', label='Y Trace')

# Add labels along the trace lines
ax.text(x_2d / 2, 0, 0, "+2 units", color='red', fontsize=10, ha='center')   # Halfway on X-axis
ax.text(x_2d, y_2d / 2, 0, "+3 units", color='green', fontsize=10, ha='center')  # Halfway on Y-axis

# Add a label for the point
ax.text(x_2d, y_2d+0.5, z_2d, f"Point A ({x_2d}, {y_2d})", color='black', fontsize=10, ha='center')

# Set axis labels
ax.set_xlabel('X Axis (Red)')
ax.set_ylabel('Y Axis (Green)')
ax.set_zlabel('Z Axis (Blue)')

# Add a title for the point being displayed
ax.set_title(f" Displaying Point at ({x_2d}, {y_2d}, {z_2d}) on the X-Y Plane")

# Add a legend for clarity
ax.legend(loc="lower left")

# Adjust the view angle
ax.view_init(elev=90, azim=-90)  # Slight tilt and rotation for better visualization

# Show the plot
plt.show()