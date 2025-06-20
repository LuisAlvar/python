import numpy as np
import matplotlib.pyplot as plt

# Define time values for two cycles
T = 2 * np.pi / abs(3.09)  # Compute period
t = np.linspace(0, T, 1000)  # Limit time to two cycles

# Define the function x(t)
x = 25 * np.cos(3.09 * t - 0.295 * np.pi)

# Plot the function
plt.plot(t, x, label=r'$x(t) = 25 \cos(3.09t - 0.295\pi)$')

# Labels and title
plt.xlabel('Time (t)')
plt.ylabel('Position (x)')
plt.title('Position vs Time (One Cycles)')
plt.legend()
plt.grid()

# Show the plot
plt.show()