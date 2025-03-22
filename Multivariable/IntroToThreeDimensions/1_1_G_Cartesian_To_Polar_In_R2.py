import matplotlib.pyplot as plt
import numpy as np

# Define a Cartesian point
x, y = 3, 3  # Example Cartesian coordinates

# Convert to polar coordinates
r = np.sqrt(x**2 + y**2)  # Radius
theta = np.arctan2(y, x)  # Angle in radians (arctan2 handles all quadrants)

# Create the 2D plot
fig, ax = plt.subplots()
ax.set_aspect('equal')  # Equal scaling for proper visualization

# Plot the Cartesian point
ax.plot(x, y, 'bo', label=f'Cartesian Point ({x}, {y})')

# Plot the polar coordinate (show radius visually)
ax.plot([0, x], [0, y], 'purple', linestyle='--', label=f'r = {r:.2f} (Radius)')

# Draw an arc to represent the angle
arc_theta = np.linspace(0, theta, 100)  # Create angle points from 0 to theta
arc_x = 0.5 * np.cos(arc_theta)  # Arc radius (small constant value for visibility)
arc_y = 0.5 * np.sin(arc_theta)  # Arc radius
ax.plot(arc_x, arc_y, color='red', label=f'θ = {np.degrees(theta):.2f}° (Angle)')

# Add labels for clarity
ax.text(x + 0.3, y + 0.3, f"({x}, {y})", color='blue', fontsize=10)  # Cartesian coordinates
ax.text(0.5 * np.cos(theta / 2), 0.5 * np.sin(theta / 2), f'{np.degrees(theta):.2f}°',
        color='red', fontsize=10, ha='center')  # Angle label inside the arc

# Add axes for reference
ax.axhline(0, color='black', linewidth=0.5)  # X-axis
ax.axvline(0, color='black', linewidth=0.5)  # Y-axis

# Add labels and title
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('Conversion from Cartesian to Polar Coordinates (with Angle Arc)')
ax.legend()

# Set plot limits and grid
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
plt.grid(True)

# Show the plot
plt.show()