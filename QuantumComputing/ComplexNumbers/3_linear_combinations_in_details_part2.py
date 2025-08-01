import numpy as np
import matplotlib.pyplot as plt

# Basis vectors
v1 = np.array([1, 2])
v2 = np.array([2, 1])
origin = np.array([0, 0])

# Target vector to reach
target = np.array([3, 5])

# Solve for unique coefficients a and b such that a*v1 + b*v2 = target
A = np.column_stack((v1, v2))
coeffs = np.linalg.solve(A, target)
a, b = coeffs

# Scaled vectors
scaled_v1 = a * v1
scaled_v2 = b * v2

# Intermediate point after adding scaled_v1
intermediate = scaled_v1

# Final reconstruction
reconstructed = scaled_v1 + scaled_v2

# Plot setup
plt.figure(figsize=(8, 8))

# Basis vectors
plt.quiver(*origin, *v1, color='red', angles='xy', scale_units='xy', scale=1, label='v1 = [1, 2]')
plt.quiver(*origin, *v2, color='blue', angles='xy', scale_units='xy', scale=1, label='v2 = [2, 1]')

# Show scaling
plt.quiver(*origin, *scaled_v1, color='orange', angles='xy', scale_units='xy', scale=1, label=f'{a:.2f}·v1')
plt.quiver(*intermediate, *scaled_v2, color='green', angles='xy', scale_units='xy', scale=1, label=f'{b:.2f}·v2')

# Target vector
plt.plot(target[0], target[1], 'go', label='Target = [3, 5]')
plt.text(target[0]+0.2, target[1]+0.2, 'Target Vector')

# Visual tweaks
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.axhline(0, color='gray', lw=1)
plt.axvline(0, color='gray', lw=1)
plt.grid(True)
plt.gca().set_aspect('equal')
plt.title("Linear Combination: Stretching v1 and v2 to Reach Target")
plt.legend()
plt.show()