import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Coordinates of the 3D point
x, y, z = 3, 3, 3

# Create a new figure for 3D plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D point
ax.scatter(x, y, z, color='red', label='Point (3, 3, 3)', s=100)

# Plot projections onto the XY-plane, XZ-plane, and YZ-plane
# XY-plane projection (z = 0)
ax.scatter(x, y, 0, color='blue', label='Projection onto XY-plane (3, 3, 0)', s=50)
# XZ-plane projection (y = 0)
ax.scatter(x, 0, z, color='green', label='Projection onto XZ-plane (3, 0, 3)', s=50)
# YZ-plane projection (x = 0)
ax.scatter(0, y, z, color='purple', label='Projection onto YZ-plane (0, 3, 3)', s=50)

# Add lines to connect the point to its projections for better visualization
ax.plot([x, x], [y, y], [z, 0], color='blue', linestyle='dashed')  # To XY-plane
ax.plot([x, x], [y, 0], [z, z], color='green', linestyle='dashed')  # To XZ-plane
ax.plot([x, 0], [y, y], [z, z], color='purple', linestyle='dashed')  # To YZ-plane

# Set axis labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Set the title
ax.set_title('3D Point and Projections onto 2D Planes')

# Add a legend
ax.legend()

# Show the plot
plt.show()
