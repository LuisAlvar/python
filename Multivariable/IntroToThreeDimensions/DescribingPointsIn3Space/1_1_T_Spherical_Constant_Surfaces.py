import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create the figure and 3D axes
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Define the grid for theta (azimuthal angle) and phi (polar angle)
theta = np.linspace(0, 2 * np.pi, 100)  # Azimuthal angle (0 to 2pi)
phi = np.linspace(0, np.pi, 100)       # Polar angle (0 to pi)

# Sphere surface: rho = 1 (constant)
rho_sphere = 1
Theta_sphere, Phi_sphere = np.meshgrid(theta, phi)
X_sphere = rho_sphere * np.sin(Phi_sphere) * np.cos(Theta_sphere)
Y_sphere = rho_sphere * np.sin(Phi_sphere) * np.sin(Theta_sphere)
Z_sphere = rho_sphere * np.cos(Phi_sphere)

# Plot the sphere
ax.plot_surface(X_sphere, Y_sphere, Z_sphere, alpha=0.6, color='blue', label='Sphere')

# Add label for the sphere
ax.text(0, 0, 1.2, 'Sphere (ρ = 1)', color='black', fontsize=12)

# Cone surface: phi = 3pi/4 (constant polar angle)
phi_cone = 3 * np.pi / 4  # Fixed polar angle
rho_cone = np.linspace(0, 2, 50)  # Radial range extended beyond the sphere
Theta_cone, Rho_cone = np.meshgrid(theta, rho_cone)
X_cone = Rho_cone * np.sin(phi_cone) * np.cos(Theta_cone)
Y_cone = Rho_cone * np.sin(phi_cone) * np.sin(Theta_cone)
Z_cone = Rho_cone * np.cos(phi_cone)

# Plot the cone
ax.plot_surface(X_cone, Y_cone, Z_cone, alpha=0.6, color='red', label='Cone')

# Add label for the cone
ax.text(0.5, 0.5, -0.5, 'Cone (φ = 3π/4)', color='black', fontsize=12)

# Add axes labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Sphere and Cone in Spherical Coordinates')

# Show the plot
plt.show()