import numpy as np
import matplotlib.pyplot as plt

# Transformation matrix A
A = np.array([[2, 1],
              [0, 3]])

# New basis vectors
v1_bar = np.array([1, 1])
v2_bar = np.array([-1, 1])
S = np.column_stack((v1_bar, v2_bar))

# Transformed matrix in new basis
T = S
T_inv = np.linalg.inv(T)
A_bar = T_inv @ A @ S

# Standard basis
e1 = np.array([1, 0])
e2 = np.array([0, 1])

# Transformed standard basis
Ae1 = A @ e1
Ae2 = A @ e2

# Transformed new basis
Ab1 = A @ v1_bar
Ab2 = A @ v2_bar

# Plot setup
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title('Visualizing Theorem 2.20: Basis Change and Transformation')

# Helper function to draw vectors
def draw_vector(v, color, label):
    ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)

# Plot original basis
draw_vector(e1, 'blue', 'e1 (standard)')
draw_vector(e2, 'blue', 'e2 (standard)')

# Plot transformed standard basis
draw_vector(Ae1, 'red', 'A @ e1')
draw_vector(Ae2, 'red', 'A @ e2')

# Plot new basis
draw_vector(v1_bar, 'green', 'b1 (new basis)')
draw_vector(v2_bar, 'green', 'b2 (new basis)')

# Plot transformed new basis
draw_vector(Ab1, 'purple', 'A @ b1')
draw_vector(Ab2, 'purple', 'A @ b2')

# Add legend
ax.legend(loc='upper left')
plt.show()