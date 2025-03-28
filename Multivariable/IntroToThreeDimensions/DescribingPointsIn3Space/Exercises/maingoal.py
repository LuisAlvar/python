import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parameters
R = 3  # Radius of the main sphere
r = 0.5  # Radius of the smaller sphere
a = 5  # Twist parameter for curve path
frames = 360  # Number of frames in the animation

# Function to create sphere
def create_sphere(radius):
    u, v = np.linspace(0, 2 * np.pi, 100), np.linspace(0, np.pi, 100)
    x = radius * np.outer(np.sin(v), np.cos(u))
    y = radius * np.outer(np.sin(v), np.sin(u))
    z = radius * np.outer(np.cos(v), np.ones_like(u))
    return x, y, z

# Function for curve path
def curve_path(t):
    x = (R - r) * np.sin(t) * np.cos(a * t)
    y = (R - r) * np.sin(t) * np.sin(a * t)
    z = (R - r) * np.cos(t)
    return x, y, z

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-R - r, R + r])
ax.set_ylim([-R - r, R + r])
ax.set_zlim([-R - r, R + r])
ax.set_box_aspect([1, 1, 1])

# Plot the main sphere
sphere_x, sphere_y, sphere_z = create_sphere(R)
ax.plot_surface(sphere_x, sphere_y, sphere_z, color='blue', alpha=0.5)

# Animation function
smaller_sphere, = ax.plot([], [], [], 'ro')
curve_t = np.linspace(0, 2 * np.pi, frames)
curve_x, curve_y, curve_z = curve_path(curve_t)
ax.plot(curve_x, curve_y, curve_z, 'k', linestyle='--')  # Plot the curve path

def update(frame):
    t = frame * (2 * np.pi / frames)  # Time parameter
    x, y, z = curve_path(t)
    smaller_sphere.set_data([x], [y])
    smaller_sphere.set_3d_properties([z])
    return smaller_sphere,

# Animate the smaller sphere
ani = FuncAnimation(fig, update, frames=frames, interval=50)
plt.show()