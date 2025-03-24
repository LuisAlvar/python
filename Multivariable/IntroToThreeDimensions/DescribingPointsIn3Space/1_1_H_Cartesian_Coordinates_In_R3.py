import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set axis limits
ax.set_xlim([-4, 4])  # X-axis depth
ax.set_ylim([-5, 5])  # Y-axis horizontal
ax.set_zlim([-2, 6])  # Z-axis vertical

# Plot the axes with colors
ax.quiver(0, 0, 0, 1, 0, 0, color='red', label='X-axis')   # X-axis (red)
ax.quiver(0, 0, 0, 0, 1, 0, color='green', label='Y-axis') # Y-axis (green)
ax.quiver(0, 0, 0, 0, 0, 1, color='blue', label='Z-axis')  # Z-axis (blue)

# Add a plane at Z=0
xx, yy = np.meshgrid(range(-4, 5), range(-5, 6))  # Mesh grid for X-Y plane
zz = np.zeros_like(xx)  # Z=0 for the plane
ax.plot_surface(xx, yy, zz, alpha=0.2, color='gray')  # Semi-transparent gray plane

# Add tracing lines to the point
# Line along X-axis from origin to the x-coordinate
ax.plot([0, 2], [0, 0], [0, 0], color='red', linestyle='--', label='X Trace')
# Line along Y-axis from the x-coordinate to the y-coordinate
ax.plot([2, 2], [0, 3], [0, 0], color='green', linestyle='--', label='Y Trace')

# Add labels along the trace lines
ax.text(2 / 2, 0, 0, "+2 units", color='red', fontsize=10, ha='center')   # Halfway on X-axis
ax.text(2, 3 / 2, 0, "+3 units", color='green', fontsize=10, ha='center')  # Halfway on Y-axis

# Add the point as a scatter plot
point, = ax.plot([2], [3], [0], 'o', color='purple', markersize=10, label='Point A (X, Y, Z)')

# Add the tracing line
trace_line, = ax.plot([2, 2], [3, 3], [0, 0], color='blue', linestyle='-', label='Tracing Line')

# Add legend and labels
ax.set_xlabel('X Axis (Red)')
ax.set_ylabel('Y Axis (Green)')
ax.set_zlabel('Z Axis (Blue)')
ax.set_title('Animating Point Movement with Tracing Line')
ax.legend(loc="lower left")

# Animation function
def update(frame):
    # Calculate the Z position at the current frame
    z_pos = frame / frames * 5  # Linearly interpolate Z from 0 to 5

    # Update the point's position
    point.set_data([2], [3])  # X and Y remain constant
    point.set_3d_properties([z_pos])  # Update Z position

    # Update the tracing line to match the point's movement
    trace_line.set_data([2, 2], [3, 3])  # X and Y remain constant
    trace_line.set_3d_properties([0, z_pos])  # Extend the Z trace up to the current Z position

    # Stop updating when Z reaches 5
    if frame == frames:
        print("Animation complete. Point and tracing line fixed at (2, 3, 5).")

    return point, trace_line

# Create the animation
frames = 100  # Number of frames for the animation
ani = FuncAnimation(fig, update, frames=frames + 1, interval=50, blit=True)  # +1 ensures we include the final frame

# Show the animation
plt.show()