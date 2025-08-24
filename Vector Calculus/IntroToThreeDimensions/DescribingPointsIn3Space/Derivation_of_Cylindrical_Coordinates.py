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
        # Define point and radius
        self.pointP = pointP
        self.r = np.sqrt(pointP[0]**2 + pointP[1]**2)
        # State variables
        self.state = {"is2dAnimationDone": False, "is3dAnimationDone": False}
        # Static plot elements
        self.ax.plot([0, pointP[0]], [0, 0], [0, 0], 'r--', label='x-trace')
        self.ax.plot([pointP[0], pointP[0]], [0, pointP[1]], [0, 0], 'b--', label='y-trace')
        self.ax.text(pointP[0]/2, 0.25, 0, 'x', fontsize=10, color='red')
        self.ax.text(pointP[0] + 0.25, pointP[1]/2, 0, 'y', fontsize=10, color='blue')
        # Initialize dynamic elements
        self.line_r, = self.ax.plot([], [], [], 'g', label='r')
        self.pointP_2d, = self.ax.plot([pointP[0]], [pointP[1]], [0], 'ro', label='Point P')  # Static 2D point
        self.pointP_3d, = self.ax.plot([], [], [], 'ro', label='Point P\'')  # Dynamic 3D point
        self.trace_line, = self.ax.plot([], [], [], color='blue', linestyle='--')  # Tracing line

    def update_2d(self, frame):
        # recalculating the length of the vector based on incrementation of y from 0 to pointP[1] based on the number of frames 
        total_frames = int(np.degrees(np.arctan(pointP[1] / pointP[0]))) + 1
        delta_y = (pointP[1] / float(total_frames)) * frame
        self.r = np.sqrt(pointP[0]**2 + delta_y**2) 
        # Calculate the new x_r and y_r
        theta = np.radians(frame)
        x_r = self.r * np.cos(theta)
        y_r = self.r * np.sin(theta)
        # Update the line segment dynamically
        self.line_r.set_data([0, x_r], [0, y_r])
        self.line_r.set_3d_properties([0, 0])
        # At the end of animation, finalize Point P
        if frame >= self.stop_angle:
            ani2d.event_source.stop()
            # Tracing the current stage as done
            self.state["is2dAnimationDone"] = True
            # Draw the final state of r and Point P
            self.ax.plot([0, self.pointP[0]], [0, self.pointP[1]], [0, 0], color='green', label='Final r')
            self.ax.text(self.pointP[0]/2, (self.pointP[0]/2) * np.tan(np.degrees(self.stop_angle)), 0, 'r', fontsize=10, color='green')
            self.ax.scatter(self.pointP[0], self.pointP[1], 0, color='red', label='Point P', s=50)
            self.ax.text(self.pointP[0], self.pointP[1], 0, 'Point P', fontsize=10, color='red')
            # Transition to 3D animation
            self.start_3d_animation()
        return self.line_r

    def update_3d(self, frame):
        z_pos = frame / 100 * 5  # Linearly interpolate z-coordinate
        # Update Point P' and its tracing line
        self.pointP_3d.set_data([self.pointP[0]], [self.pointP[1]])
        self.pointP_3d.set_3d_properties([z_pos])
        self.trace_line.set_data([self.pointP[0], self.pointP[0]], [self.pointP[1], self.pointP[1]])
        self.trace_line.set_3d_properties([0, z_pos])
        # At the end of animation, finalize Point P' and draw line to origin
        if frame == 100:
            ani3d.event_source.stop()
            self.state["is3dAnimationDone"] = True
            # Draw final line segment from origin to Point P'
            self.ax.plot([0, self.pointP[0]], [0, self.pointP[1]], [0, z_pos], color='green', label='Line to P\'')
            self.ax.text(self.pointP[0], self.pointP[1], z_pos, 'Point P\'', fontsize=10, color='purple')
            # Immediately display the cylinder
            self.display_cylinder(z_max=z_pos)
        return self.pointP_3d, self.trace_line

    def display_cylinder(self, z_max):
        # Generate coordinates for the cylinder
        theta = np.linspace(0, 2 * np.pi, 100)
        z = np.linspace(0, z_max, 50)
        theta_grid, z_grid = np.meshgrid(theta, z)

        x = self.r * np.cos(theta_grid)
        y = self.r * np.sin(theta_grid)
        z = z_grid

        # Plot the transparent blue cylinder
        self.ax.plot_surface(
            x, y, z, rstride=1, cstride=1, alpha=0.3, color='blue', edgecolor='none'
        )

    def start_3d_animation(self):
        global ani3d
        ani3d = FuncAnimation(self.fig, self.update_3d, frames=101, interval=50)

# Main logic
pointP = (4, 2, 0)  # Define the coordinates of Point P
animation = CylindricalCoordinates(pointP)

# Create 2D animation
animation.stop_angle = int(np.degrees(np.arctan(pointP[1] / pointP[0])))
ani2d = FuncAnimation(animation.fig, animation.update_2d, frames=np.arange(0, animation.stop_angle + 1))

# Show plot
plt.legend(loc="upper right")
plt.show()