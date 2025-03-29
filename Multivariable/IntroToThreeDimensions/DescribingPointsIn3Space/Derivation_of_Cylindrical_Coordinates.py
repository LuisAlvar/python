import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class CylindricalCoordinates:
    def __init__(self, pointP):
        # Initialize figure and axes
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_xlim(0, 5)
        self.ax.set_ylim(0, 5)
        self.ax.set_zlim(0, 5)
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.set_zlabel('Z-axis')

        # Point and radius
        self.pointP = pointP
        self.r = np.sqrt(pointP[0]**2 + pointP[1]**2)
        self.stop_angle = int(np.degrees(np.arctan(pointP[1] / pointP[0])))

        # State variables
        self.state = {"is2dAnimationDone": False}

        # Static elements
        self.ax.plot([0, pointP[0]], [0, 0], [0, 0], 'r--', label='x-trace')
        self.ax.plot([pointP[0], pointP[0]], [0, pointP[1]], [0, 0], 'b--', label='y-trace')

        # Initialize dynamic elements
        self.line_r, = self.ax.plot([], [], [], 'g', label='r')
        self.pointP_2d, = self.ax.plot([pointP[0]], [pointP[1]], [0], 'ro', label='Point P')  # 2D point
        self.pointP_3d, = self.ax.plot([], [], [], 'ro', label='Point P\'')  # 3D point
        self.trace_line, = self.ax.plot([], [], [], color='blue', linestyle='--')

    def update_2d(self, frame):
        theta = np.radians(frame)
        x_r = self.r * np.cos(theta)
        y_r = self.r * np.sin(theta)

        # Update the line segment
        self.line_r.set_data([0, x_r], [0, y_r])
        self.line_r.set_3d_properties([0, 0])

        if frame >= self.stop_angle:
            ani2d.event_source.stop()  # Stop the 2D animation
            self.state["is2dAnimationDone"] = True

            # Preserve final 2D state and label Point P
            self.ax.plot([0, self.pointP[0]], [0, self.pointP[1]], [0, 0], color='green', label='Final r')
            self.ax.scatter(self.pointP[0], self.pointP[1], self.pointP[2], color='red', label='Point P', s=50)
            self.ax.text(self.pointP[0], self.pointP[1], 0, 'Point P', fontsize=10, color='red')  # Display label at the end

            # Start the 3D animation
            self.start_3d_animation()

        return self.line_r

    def update_3d(self, frame):
        z_pos = frame / 100 * 5  # Linearly interpolate Z

        # Update point and tracing line
        self.pointP_3d.set_data([self.pointP[0]], [self.pointP[1]])
        self.pointP_3d.set_3d_properties([z_pos])

        self.trace_line.set_data([self.pointP[0], self.pointP[0]], [self.pointP[1], self.pointP[1]])
        self.trace_line.set_3d_properties([0, z_pos])

        if frame == 100:
            ani3d.event_source.stop()  # Stop the 3D animation

            # Draw the final line segment from origin to Point P prime
            self.ax.plot([0, self.pointP[0]], [0, self.pointP[1]], [0, z_pos], color='purple', label='Line to P\'')
            self.ax.text(self.pointP[0], self.pointP[1], z_pos, 'Point P\'', fontsize=10, color='purple')  # Display label at the end

        return self.pointP_3d, self.trace_line

    def start_3d_animation(self):
        # Define the 3D animation here
        global ani3d
        ani3d = FuncAnimation(self.fig, self.update_3d, frames=101, interval=50)

# Main logic
pointP = (4, 2, 0)  # Define the point
animation = CylindricalCoordinates(pointP)

# Create 2D animation
ani2d = FuncAnimation(animation.fig, animation.update_2d, frames=np.arange(0, animation.stop_angle + 1))

# Display the plot
plt.legend()
plt.show()