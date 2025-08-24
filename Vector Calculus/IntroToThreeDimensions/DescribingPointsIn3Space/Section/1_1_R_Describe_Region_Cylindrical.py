import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create the figure and 3D axes
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Parameters for the inequalities
r = np.linspace(0, 2, 50)  # Radius range
theta = np.linspace(0, np.pi / 3, 50)  # Angular range (0 to π/3)
z = np.linspace(0, 5, 50)  # Height range

# Create the meshgrid for the cylindrical coordinates
R, Theta, Z = np.meshgrid(r, theta, z)

# Convert cylindrical to Cartesian coordinates for plotting
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

# Plot the filled region (volume)
ax.scatter(X, Y, Z, alpha=0.1, color='#B3C8CF', label='Filled Region')

# Add labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Filled Region in Cylindrical Coordinates')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([0, 5])
ax.legend()

# Show the plot
plt.show()