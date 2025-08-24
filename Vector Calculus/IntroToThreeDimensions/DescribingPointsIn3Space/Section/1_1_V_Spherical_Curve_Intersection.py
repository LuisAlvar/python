import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create the figure and 3D axes
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Define the parameters for the curve
rho = 1  # Fixed radial distance (sphere)
phi = 3 * np.pi / 4  # Fixed polar angle (cone)
theta = np.linspace(0, 2 * np.pi, 200)  # Azimuthal angle (full circle)

# Calculate the Cartesian coordinates for the intersection curve
x = rho * np.sin(phi) * np.cos(theta)
y = rho * np.sin(phi) * np.sin(theta)
z = rho * np.cos(phi)

# Plot the intersection curve
ax.plot(x, y, z, label='Intersection Curve', color='purple')

# Plot the sphere (optional for context)
phi_sphere = np.linspace(0, np.pi, 100)
theta_sphere = np.linspace(0, 2 * np.pi, 100)
Theta_sphere, Phi_sphere = np.meshgrid(theta_sphere, phi_sphere)
X_sphere = rho * np.sin(Phi_sphere) * np.cos(Theta_sphere)
Y_sphere = rho * np.sin(Phi_sphere) * np.sin(Theta_sphere)
Z_sphere = rho * np.cos(Phi_sphere)
ax.plot_surface(X_sphere, Y_sphere, Z_sphere, alpha=0.3, color='blue', label='Sphere (ρ=1)')

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Intersection of Sphere (ρ=1) and Cone (φ=3π/4)')
ax.legend()

# Show the plot
plt.show()