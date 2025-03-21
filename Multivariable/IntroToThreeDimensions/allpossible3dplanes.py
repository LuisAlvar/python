import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the ranges for the planes
range_vals = np.linspace(-10, 10, 100)

# Plane parallel to the XY-plane (Z = 0)
x_xy, y_xy = np.meshgrid(range_vals, range_vals)
z_xy = np.zeros_like(x_xy)
plane1 = ax.plot_surface(x_xy, y_xy, z_xy, alpha=0.5, color='red', label='Parallel to XY-plane')

# Plane parallel to the YZ-plane (X = 0)
y_yz, z_yz = np.meshgrid(range_vals, range_vals)
x_yz = np.zeros_like(y_yz)
plane2 = ax.plot_surface(x_yz, y_yz, z_yz, alpha=0.5, color='green', label='Parallel to YZ-plane')

# Plane parallel to the XZ-plane (Y = 0)
x_xz, z_xz = np.meshgrid(range_vals, range_vals)
y_xz = np.zeros_like(x_xz)
plane3 = ax.plot_surface(x_xz, y_xz, z_xz, alpha=0.5, color='blue', label='Parallel to XZ-plane')

# Label the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Add a title
ax.set_title('3D Planes Parallel to Axes')

# Create a custom legend
legend_labels = ['Parallel to XY-plane', 'Parallel to YZ-plane', 'Parallel to XZ-plane']
legend_colors = ['red', 'green', 'blue']
for label, color in zip(legend_labels, legend_colors):
    ax.scatter([], [], [], label=label, color=color)  # Invisible points for legend

ax.legend(loc='upper right')

# Display the plot
plt.show()