import matplotlib.pyplot as plt
import numpy as np

# Polar coordinate
r = 2
delta = 3 * np.pi / 4  # Angle in radians

# Convert to Cartesian coordinates
x = r * np.cos(delta)
y = r * np.sin(delta)

# Create the 2D plot
fig, ax = plt.subplots()
ax.set_aspect('equal')  # Equal aspect ratio

# Plot the point
ax.plot(x, y, 'bo', label=f'Point (r=2, δ=3π/4) → ({x:.2f}, {y:.2f})')

# Draw a line from the origin to the point to represent radius
ax.plot([0, x], [0, y], 'purple', linestyle='--', label='Radius (r=2)')

# Add labels for the point
ax.text(x + 0.2, y + 0.2, f"({x:.2f}, {y:.2f})", color='blue', fontsize=10)

# Customize the plot
ax.axhline(0, color='black', linewidth=0.5)  # X-axis
ax.axvline(0, color='black', linewidth=0.5)  # Y-axis
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title("Polar to Cartesian: r=2, δ=3π/4")
ax.legend()

# Show grid and the plot
plt.grid(True)
plt.show()