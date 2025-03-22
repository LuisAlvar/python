import matplotlib.pyplot as plt
import numpy as np

# Create the 2D plot
fig, ax = plt.subplots()

# Define the range for x and y axes
x = np.linspace(-5, 5, 100)  # Range of x for the horizontal line
y = np.linspace(-5, 5, 100)  # Range of y for the vertical line

# Plot x=2 (a vertical line)
ax.plot([2, 2], [-5, 5], color='red', linestyle='--', label='x = 2')

# Plot y=3 (a horizontal line)
ax.plot([-5, 5], [3, 3], color='blue', linestyle='--', label='y = 3')

# Customize the plot
ax.axhline(0, color='black', linewidth=0.5)  # X-axis
ax.axvline(0, color='black', linewidth=0.5)  # Y-axis
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('2D Plot of x=2 and y=3 as Lines')
ax.legend()

# Show the plot
plt.grid(True)
plt.show()