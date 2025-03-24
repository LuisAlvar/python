import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the primary vertical line (1, -1, z)
x_line = [1] * 100
y_line = [-1] * 100
z_line = np.linspace(-10, 10, 100)
ax.plot(x_line, y_line, z_line, label='Vertical Line (1, -1, z)', color='r')

# Add parallel lines
# Line parallel to X-axis
x_parallel_x = np.linspace(-10, 10, 100)
y_parallel_x = [-1] * 100
z_parallel_x = [0] * 100
ax.plot(x_parallel_x, y_parallel_x, z_parallel_x, label='Parallel to X-axis', color='b')

# Line parallel to Y-axis
x_parallel_y = [1] * 100
y_parallel_y = np.linspace(-10, 10, 100)
z_parallel_y = [0] * 100
ax.plot(x_parallel_y, y_parallel_y, z_parallel_y, label='Parallel to Y-axis', color='g')

# Line parallel to Z-axis
x_parallel_z = [0] * 100
y_parallel_z = [0] * 100
z_parallel_z = np.linspace(-10, 10, 100)
ax.plot(x_parallel_z, y_parallel_z, z_parallel_z, label='Parallel to Z-axis', color='purple')

# Label the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Add a title
ax.set_title('3D Plot: Vertical Line and Parallel Lines')

# Add legend
ax.legend()

# Display the plot
plt.show()