import matplotlib.pyplot as plt
import numpy as np

# Define the polar equation r = 2 (a circle)
theta_circle = np.linspace(0, 2 * np.pi, 500)  # Angle values from 0 to 2π
r_circle = 2
x_circle = r_circle * np.cos(theta_circle)
y_circle = r_circle * np.sin(theta_circle)

# Define the polar equation δ = 3π/4 (a straight line)
delta_line = 3 * np.pi / 4
r_line = np.linspace(0, 4, 500)  # Radius values from 0 to 4
x_line = r_line * np.cos(delta_line)
y_line = r_line * np.sin(delta_line)

# Create the 2D Cartesian plot
plt.figure()
plt.plot(x_circle, y_circle, label=r'Polar Equation: r = 2', color='blue')  # Circle
plt.plot(x_line, y_line, label=r'Polar Equation: δ = 3π/4', color='red', linestyle='--')  # Line

# Customize the plot
plt.axhline(0, color='black', linewidth=0.5)  # X-axis
plt.axvline(0, color='black', linewidth=0.5)  # Y-axis
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('2D Cartesian Plot of Polar Equations: r = 2 and δ = 3π/4')
plt.legend()
plt.grid(True)
plt.axis('equal')  # Equal scaling for proper visualization

# Show the plot
plt.show()