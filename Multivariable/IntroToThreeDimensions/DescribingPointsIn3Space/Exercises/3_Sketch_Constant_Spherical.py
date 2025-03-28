import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Sphere: rho = 2
phi = np.linspace(0, np.pi, 100)  # Polar angle
theta = np.linspace(0, 2 * np.pi, 100)  # Azimuthal angle
Phi, Theta = np.meshgrid(phi, theta)
X_sphere = 2 * np.sin(Phi) * np.cos(Theta)
Y_sphere = 2 * np.sin(Phi) * np.sin(Theta)
Z_sphere = 2 * np.cos(Phi)
ax.plot_surface(X_sphere, Y_sphere, Z_sphere, alpha=0.5, color='blue', label='Sphere: rho=2')

# Cone: phi = pi/3
phi_cone = np.pi / 3
theta_cone = np.linspace(0, 2 * np.pi, 100)
r_cone = np.linspace(0, 10, 100)  # Variable radius (extends outward)
R_cone, Theta_cone = np.meshgrid(r_cone, theta_cone)
X_cone = R_cone * np.sin(phi_cone) * np.cos(Theta_cone)
Y_cone = R_cone * np.sin(phi_cone) * np.sin(Theta_cone)
Z_cone = R_cone * np.cos(phi_cone)
ax.plot_surface(X_cone, Y_cone, Z_cone, alpha=0.5, color='red', label='Cone: phi=pi/3')

# Half-plane: theta = -3pi/4
theta_plane = -3 * np.pi / 4
r_plane = np.linspace(-10, 10, 100)  # Radial extent
z_plane = np.linspace(-10, 10, 100)  # Vertical extent
R_plane, Z_plane = np.meshgrid(r_plane, z_plane)
X_plane = R_plane * np.cos(theta_plane)
Y_plane = R_plane * np.sin(theta_plane)
ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.5, color='green', label='Half-plane: theta=-3pi/4')

# Add legend
ax.legend(loc='upper right')

# Customize axes and ticks
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])
ax.set_xticks(np.arange(-10, 12, 2))
ax.set_yticks(np.arange(-10, 12, 2))
ax.set_zticks(np.arange(-10, 12, 2))
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Plot of Sphere, Cone, and Half-plane')

# Show the plot
plt.show()