import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create the 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate grid points for x and y
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
x, y = np.meshgrid(x, y)

# Set z = 3 (plane at z=3)
z = np.full_like(x, 3)

# Plot the surface
ax.plot_surface(x, y, z, alpha=0.7, rstride=100, cstride=100, color='skyblue', edgecolor='gray')

# Add labels and a title
ax.set_title("3D Plot of the Plane z = 3")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Show the plot
plt.show()
