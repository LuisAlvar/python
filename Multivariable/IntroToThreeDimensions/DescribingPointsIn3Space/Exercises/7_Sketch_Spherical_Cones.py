import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Cone: ϕ = π/6
phi_cone = np.pi/6
theta_cone = np.linspace(0, 2 * np.pi, 100)
r_cone = np.linspace(0, 10, 100) # variable radius (extends outward)
R_cone, Theta_cone = np.meshgrid(r_cone, theta_cone)
X_cone = R_cone * np.sin(phi_cone) * np.cos(Theta_cone) 
Y_cone = R_cone * np.sin(phi_cone) * np.sin(Theta_cone) 
Z_cone = R_cone * np.cos(phi_cone)
ax.plot_surface(X_cone, Y_cone, Z_cone, alpha=0.5, color="red", label="Cone: ϕ = π/6")

# Cone: ϕ = π/2
phi_cone = np.pi/2
theta_cone = np.linspace(0, 2 * np.pi, 100)
r_cone = np.linspace(0, 10, 100) # variable radius (extends outward)
R_cone, Theta_cone = np.meshgrid(r_cone, theta_cone)
X_cone = R_cone * np.sin(phi_cone) * np.cos(Theta_cone) 
Y_cone = R_cone * np.sin(phi_cone) * np.sin(Theta_cone) 
Z_cone = R_cone * np.cos(phi_cone)
ax.plot_surface(X_cone, Y_cone, Z_cone, alpha=0.5, color="grey", label="Cone: ϕ = π/2")

# Cone: ϕ = 3π/4
phi_cone = 3*np.pi/4
theta_cone = np.linspace(0, 2 * np.pi, 100)
r_cone = np.linspace(0, 10, 100) # variable radius (extends outward)
R_cone, Theta_cone = np.meshgrid(r_cone, theta_cone)
X_cone = R_cone * np.sin(phi_cone) * np.cos(Theta_cone) 
Y_cone = R_cone * np.sin(phi_cone) * np.sin(Theta_cone) 
Z_cone = R_cone * np.cos(phi_cone)
ax.plot_surface(X_cone, Y_cone, Z_cone, alpha=0.5, color="blue", label="Cone: ϕ = 3π/4")


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
ax.set_title('3D Plot of Cones')

# Show the plot
plt.show()