import matplotlib.pyplot as plt
import numpy as np

# Cartesian point
x, y = 2, 3  # Example Cartesian coordinates

# Convert to polar coordinates
r = np.sqrt(x**2 + y**2)  # Radius
theta = np.arctan2(y, x)  # Angle in radians (arctan2 handles all quadrants)

# Create the 2D plot
fig, ax = plt.subplots()
ax.set_aspect('equal')  # Equal aspect ratio for proper scaling

# Plot the Cartesian point
ax.plot(x, y, 'bo', label=f'Cartesian Point ({x}, {y})')

# Add a line from the origin to the point (to represent the radius)
ax.plot([0, x], [0, y], 'purple', linestyle='--', label=f'r = {r:.2f}')

# Add labels for the Cartesian and Polar values
ax.text(x / 2, y / 2, f'r = {r:.2f}', color='purple', fontsize=10)  # Label for the radius
ax.text(x + 0.3, y + 0.3, f'({x}, {y})', color='blue', fontsize=10)  # Label for Cartesian coordinates
ax.text(r / 2 * np.cos(theta / 2), r / 2 * np.sin(theta / 2), f'θ = {np.degrees(theta):.2f}°', color='red', fontsize=10)

# Add the axes
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Set the labels and title
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title(f"Converting Cartesian ({x}, {y}) to Polar (r={r:.2f}, θ={np.degrees(theta):.2f}°)")
ax.legend()

# Set the limits for better visualization
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

# Show grid and the plot
plt.grid(True)
plt.show()