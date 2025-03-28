import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure and axis 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Defin axis limits 
x_range = np.linspace(-10, 10, 100)
y_range = np.linspace(-10, 10, 100)
z_range = np.linspace(-10, 10, 100)

# Generate meshgrid for x and y planes
X, Y = np.meshgrid(x_range, y_range)

# Plane x = -1
Y_plane, Z_plane = np.meshgrid(y_range, z_range)
X_plane = -1 * np.ones_like(Y_plane)
ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.5, color='blue', label="Plane: x = -1")

# Plane x = 0
Y_plane, Z_plane = np.meshgrid(y_range, z_range)
X_plane = 0 * np.ones_like(Y_plane)
ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.5, color='red', label="Plane: x = 0")

# Plane x = 3
Y_plane, Z_plane = np.meshgrid(y_range, z_range)
X_plane = 3 * np.ones_like(Y_plane)
ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.5, color='grey', label="Plane: x = 3")

# Add text labels to the planes
ax.text(-5, 5, 0, 'x = -1', color='blue', fontsize=10)
ax.text(1, 1, 0, 'x = 0', color='black', fontsize=10)
ax.text(3, 3, 0, 'x = 3', color='grey', fontsize=10)

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