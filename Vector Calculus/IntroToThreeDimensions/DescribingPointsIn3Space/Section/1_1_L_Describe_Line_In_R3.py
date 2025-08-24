import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertical line (x=1, y=-1, z=all)
x_line = [1] * 100
y_line = [-1] * 100
z_line = np.linspace(-10, 10, 100)

# Plot the vertical line
ax.plot(x_line, y_line, z_line, label='Vertical Line (1, -1, z)', color='r')

# Create data for the x=1 plane
y_plane, z_plane = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
x_plane = np.ones_like(y_plane)

# Plot the x=1 plane
ax.plot_surface(x_plane, y_plane, z_plane, alpha=0.5, color='blue', label='x=1 Plane')

# Create data for the y=-1 plane
x_plane, z_plane = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
y_plane = -np.ones_like(x_plane)

# Plot the y=-1 plane
ax.plot_surface(x_plane, y_plane, z_plane, alpha=0.5, color='green', label='y=-1 Plane')

# Label the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Add a title
ax.set_title('3D Plot: Vertical Line and Planes')

# Display the plot
plt.show()