import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Given point (r, delta in radians, z)
r = 5
delta = np.pi / 4  # 45 degrees
z = 3

# Conversion to cylindrical coordinates
x = r * np.cos(delta)
y = r * np.sin(delta)

# Create figure and axes
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(121, polar=True)  # Polar plot
ax2 = fig.add_subplot(122, projection='3d')  # 3D plot

# Polar plot initial setup
polar_point, = ax1.plot([], [], 'ro', markersize=8, label="Selected Point")
polar_trace, = ax1.plot([], [], 'r-', alpha=0.7, label="Trace")  # Trace line
ax1.set_rlim(0, r + 2)
ax1.legend()

# 3D plot initial setup
point_3d, = ax2.plot([], [], [], 'bo', markersize=10, label="Selected Point in 3D")
trace_3d, = ax2.plot([], [], [], 'b-', alpha=0.7, label="Trace")  # Trace line
ax2.set_xlim(-r - 2, r + 2)
ax2.set_ylim(-r - 2, r + 2)
ax2.set_zlim(0, z + 2)
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")
ax2.legend()

# Lists to store trace data
polar_r_values = []
polar_delta_values = []
x_values = []
y_values = []
z_values = []

# Animation function
def update(frame):
    t = frame / 100.0  # t goes from 0 to 1

    # Current coordinates
    current_r = t * r
    current_delta = t * delta
    current_x = t * x
    current_y = t * y
    current_z = t * z

    # Update trace data
    polar_r_values.append(current_r)
    polar_delta_values.append(current_delta)
    x_values.append(current_x)
    y_values.append(current_y)
    z_values.append(current_z)

    # Polar animation updates
    polar_point.set_data([current_delta], [current_r])
    polar_trace.set_data(polar_delta_values, polar_r_values)

    # 3D animation updates
    point_3d.set_data([current_x], [current_y])
    point_3d.set_3d_properties([current_z])
    trace_3d.set_data(x_values, y_values)
    trace_3d.set_3d_properties(z_values)

    return polar_point, polar_trace, point_3d, trace_3d

# Animation setup
anim = FuncAnimation(fig, update, frames=101, interval=50, blit=True)

plt.tight_layout()
plt.show()