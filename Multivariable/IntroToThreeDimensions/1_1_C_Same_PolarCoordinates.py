import matplotlib.pyplot as plt
import numpy as np

# Define the polar coordinates
r1, theta1 = 3, 2 * np.pi / 3  # (3, 2π/3)
r2, theta2 = -3, 5 * np.pi / 3  # (-3, 5π/3)

# Create a polar plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Plot the first point
ax.plot(theta1, r1, 'ro', label=f'(3, 2π/3) → θ = {np.degrees(theta1):.1f}°, r = 3')

# Plot the second point
ax.plot(theta2, r2, 'bo', label=f'(-3, 5π/3) → θ = {np.degrees(theta2):.1f}°, r = -3')

# Highlight the equivalence with a line to the same physical point
ax.plot([theta1, theta2], [r1, abs(r1)], 'k--', label='Equivalent Points')

# Add grid, labels, and title
ax.grid(True)
ax.set_title('Visualization of Equivalent Polar Coordinates', va='bottom')
ax.legend(loc='upper right')

# Show the plot
plt.show()
