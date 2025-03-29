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
        self.stop_angle = int(np.degrees(np.arctan(pointP[1] / pointP[0])))

        # State variables
        self.state = {"is2dAnimationDone": False, "is3dAnimationDone": False}

        # Static plot elements
        self.ax.plot([0, pointP[0]], [0, 0], [0, 0], 'r--', label='x-trace')
        self.ax.plot([pointP[0], pointP[0]], [0, pointP[1]], [0, 0], 'b--', label='y-trace')

        # Initialize dynamic elements
        self.line_r, = self.ax.plot([], [], [], 'g', label='r')
        self.pointP_2d, = self.ax.plot([pointP[0]], [pointP[1]], [0], 'ro', label='Point P')  # Static 2D point
        self.pointP_3d, = self.ax.plot([], [], [], 'ro', label='Point P\'')  # Dynamic 3D point
        self.trace_line, = self.ax.plot([], [], [], color='blue', linestyle='--')  # Tracing line

    def update_2d(self, frame):
        theta = np.radians(frame)
        x_r = self.r * np.cos(theta)
        y_r = self.r * np.sin(theta)

        # Update the line segment dynamically
        self.line_r.set_data([0, x_r], [0, y_r])
        self.line_r.set_3d_properties([0, 0])

        # At the end of animation, finalize Point P
        if frame >= self.stop_angle:
            ani2d.event_source.stop()
            self.state["is2dAnimationDone"] = True

            # Draw the final state of r and Point P
            self.ax.plot([0, self.pointP[0]], [0, self.pointP[1]], [0, 0], color='green', label='Final r')
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

            # Transition to cylinder animation
            self.start_cylinder_animation(z_pos)

        return self.pointP_3d, self.trace_line

    def update_cylinder(self, frame, z_max):
        theta = np.linspace(0, 2 * np.pi, 100)
        z = np.linspace(0, frame / 100 * z_max, 50)

        # Create dynamic layers of the cylinder
        for zi in z:
            x = self.r * np.cos(theta)
            y = self.r * np.sin(theta)
            self.ax.plot(x, y, zi, color='cyan', alpha=0.5)

        if frame == 100:
            ani_cylinder.event_source.stop()

            # Preserve the final cylindrical surface
            Z = np.linspace(0, z_max, 50)  # Full cylinder height
            Theta = np.linspace(0, 2 * np.pi, 100)  # Full angular span
            X = self.r * np.cos(Theta)
            Y = self.r * np.sin(Theta)

            # Add permanent layers for the cylinder
            for z in Z:
                self.ax.plot(X, Y, z, color='cyan', alpha=0.5)

    def start_3d_animation(self):
        global ani3d
        ani3d = FuncAnimation(self.fig, self.update_3d, frames=101, interval=50)

    def start_cylinder_animation(self, z_max):
        global ani_cylinder
        ani_cylinder = FuncAnimation(
            self.fig, 
            self.update_cylinder, 
            frames=51,  # Faster cylinder animation
            fargs=(z_max,), 
            interval=30  # Shorter interval
        )

    def on_change(self, event):
        # Preserve final state during user interaction
        if self.state["is3dAnimationDone"]:
            Z = np.linspace(0, 5, 50)  # Full cylinder height
            Theta = np.linspace(0, 2 * np.pi, 100)
            X = self.r * np.cos(Theta)
            Y = self.r * np.sin(Theta)

            # Add permanent cylinder layers
            for z in Z:
                self.ax.plot(X, Y, z, color='cyan', alpha=0.5)

# Main logic
pointP = (4, 2, 0)  # Define the coordinates of Point P
animation = CylindricalCoordinates(pointP)

# Create 2D animation
ani2d = FuncAnimation(animation.fig, animation.update_2d, frames=np.arange(0, animation.stop_angle + 1))

# Enable interactive user control
animation.fig.canvas.mpl_connect('button_release_event', animation.on_change)

# Show plot
plt.legend()
plt.show()