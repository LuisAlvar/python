import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the cuboid (box)
vertices = [
    [0, 0, 0], [2, 0, 0], [2, 3, 0], [0, 3, 0],  # Bottom face
    [0, 0, 5], [2, 0, 5], [2, 3, 5], [0, 3, 5]   # Top face
]

# Define the edges connecting the vertices to form the cuboid
edges = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],  # Bottom face
    [vertices[4], vertices[5], vertices[6], vertices[7]],  # Top face
    [vertices[0], vertices[1], vertices[5], vertices[4]],  # Side face 1
    [vertices[2], vertices[3], vertices[7], vertices[6]],  # Side face 2
    [vertices[1], vertices[2], vertices[6], vertices[5]],  # Side face 3
    [vertices[4], vertices[7], vertices[3], vertices[0]]   # Side face 4
]

# Create a 3D polygon collection to plot the cuboid
ax.add_collection3d(Poly3DCollection(edges, facecolors='cyan', alpha=0.3, edgecolors='black'))

# Set the limits of the axes
ax.set_xlim([0, 2])
ax.set_ylim([0, 3])
ax.set_zlim([0, 5])

# Label the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Add a title
ax.set_title('3D Region Defined by Inequalities')

# Display the plot
plt.show()