import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Sphere: rho = 1
rho = 1
phi = np.linspace(0, np.pi, 100)  # Polar angle
theta = np.linspace(0, 2 * np.pi, 100)  # Azimuthal angle
Phi, Theta = np.meshgrid(phi, theta)
X_sphere = rho * np.sin(Phi) * np.cos(Theta)
Y_sphere = rho * np.sin(Phi) * np.sin(Theta)
Z_sphere = rho * np.cos(Phi)
ax.plot_surface(X_sphere, Y_sphere, Z_sphere, alpha=0.5, color='blue', label='Sphere: rho=1')

# Sphere: rho = 2
rho = 2
phi = np.linspace(0, np.pi, 100)  # Polar angle
theta = np.linspace(0, 2 * np.pi, 100)  # Azimuthal angle
Phi, Theta = np.meshgrid(phi, theta)
X_sphere = rho * np.sin(Phi) * np.cos(Theta)
Y_sphere = rho * np.sin(Phi) * np.sin(Theta)
Z_sphere = rho * np.cos(Phi)
ax.plot_surface(X_sphere, Y_sphere, Z_sphere, alpha=0.5, color='grey', label='Sphere: rho=2')

# Sphere: rho = 5
rho = 5
phi = np.linspace(0, np.pi, 100)  # Polar angle
theta = np.linspace(0, 2 * np.pi, 100)  # Azimuthal angle
Phi, Theta = np.meshgrid(phi, theta)
X_sphere = rho * np.sin(Phi) * np.cos(Theta)
Y_sphere = rho * np.sin(Phi) * np.sin(Theta)
Z_sphere = rho * np.cos(Phi)
ax.plot_surface(X_sphere, Y_sphere, Z_sphere, alpha=0.5, color='green', label='Sphere: rho=5')

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