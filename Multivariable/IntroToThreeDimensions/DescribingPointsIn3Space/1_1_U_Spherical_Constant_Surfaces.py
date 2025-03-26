import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create the figure and 3D axes
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Define grid for rho (radial) and phi (polar angle)
rho = np.linspace(0, 2, 100)  # Radial distance
phi = np.linspace(0, np.pi, 100)  # Polar angle
Theta, Rho = np.meshgrid(phi, rho)  # Meshgrid for spherical coordinates

# Fix theta = 3pi/4 (Half-plane)
theta_fixed = 3 * np.pi / 4
X_plane = Rho * np.sin(Theta) * np.cos(theta_fixed)
Y_plane = Rho * np.sin(Theta) * np.sin(theta_fixed)
Z_plane = Rho * np.cos(Theta)

# Plot the half-plane
ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.6, color='green', label='Half-Plane (θ = 3π/4)')

# Add label for the half-plane
ax.text(0.5, 0.5, 1, 'Half-Plane (θ = 3π/4)', color='black', fontsize=12)

# Fix varphi = 3pi/4 (Cone)
varphi_fixed = 3 * np.pi / 4  # Fixed polar angle
Theta_cone, Rho_cone = np.meshgrid(np.linspace(0, 2 * np.pi, 100), rho)
X_cone = Rho_cone * np.sin(varphi_fixed) * np.cos(Theta_cone)
Y_cone = Rho_cone * np.sin(varphi_fixed) * np.sin(Theta_cone)
Z_cone = Rho_cone * np.cos(varphi_fixed)

# Plot the cone
ax.plot_surface(X_cone, Y_cone, Z_cone, alpha=0.6, color='red', label='Cone (φ = 3π/4)')

# Add label for the cone
ax.text(0.5, 0.5, -0.5, 'Cone (φ = 3π/4)', color='black', fontsize=12)

# Add axes labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Half-Plane (θ = 3π/4) and Cone (φ = 3π/4) in Spherical Coordinates')

# Show the plot
plt.show()