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

# Ray from origin in direction 0
theta_ray = 0
r_ray = np.linspace(0, 10, 100)  # Ray length (variable radius)
z_ray = np.linspace(0, 10, 100)  # Varying z-coordinate
x_ray = r_ray * np.cos(theta_ray)
y_ray = r_ray * np.sin(theta_ray)
ax.plot(x_ray, y_ray, z_ray, color='green', label='Ray: direction=0')

# Add text labels for direction 0
ax.text(0, 0, 0, 'Θ = 0', color='green', fontsize=10)

# Ray from origin in direction pi/4
theta_ray = np.pi / 4
r_ray = np.linspace(0, 10, 100)  # Ray length (variable radius)
z_ray = np.linspace(0, 10, 100)  # Varying z-coordinate
x_ray = r_ray * np.cos(theta_ray)
y_ray = r_ray * np.sin(theta_ray)
ax.plot(x_ray, y_ray, z_ray, color='blue', label='Ray: direction=π/4')

# Add text labels for pi/4
ax.text(5, 5, 0, 'Θ = π/4', color='blue', fontsize=10)

# Ray from origin in direction 3pi/4
theta_ray = (3*np.pi) / 4
r_ray = np.linspace(0, 10, 100)  # Ray length (variable radius)
z_ray = np.linspace(0, 10, 100)  # Varying z-coordinate
x_ray = r_ray * np.cos(theta_ray)
y_ray = r_ray * np.sin(theta_ray)
ax.plot(x_ray, y_ray, z_ray, color='red', label='Ray: direction=3π/4')

# Add text labels for pi/4
ax.text(-3, -3, 0, 'Θ = 3π/4', color='red', fontsize=10)

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
ax.set_title('3D Plot of Ray')

# Show the plot
plt.show()