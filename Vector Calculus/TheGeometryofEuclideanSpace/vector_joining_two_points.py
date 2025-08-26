import matplotlib.pyplot as plt

# Define points
P = (-2, -1)
Q = (-3, -3)
R = (-1, -4)

# Define free vectors
v = (Q[0] - P[0], Q[1] - P[1])  # Q - P
w = (R[0] - Q[0], R[1] - Q[1])  # R - Q
u = (P[0] - R[0], P[1] - R[1])  # P - R

# === First Plot: Bounded Vectors from Origin ===
fig, ax1 = plt.subplots()
ax1.set_xlim(-5, 1)
ax1.set_ylim(-5, 1)
ax1.set_aspect('equal')
ax1.grid(True)

# Plot bounded vectors
for label, (x, y) in {'P': P, 'Q': Q, 'R': R}.items():
    ax1.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='blue')
    ax1.plot(x, y, 'o', color='black', markersize=6)
    ax1.text(x, y - 0.3, f'{label} ({x},{y})', fontsize=11, color='darkred')

ax1.plot(0, 0, 'ko')
ax1.set_title('Bounded Vectors P, Q, R from Origin')

# === Second Plot: Free Vectors + Bounded Vectors (Dashed) ===
fig, ax2 = plt.subplots()
ax2.set_xlim(-5, 1)
ax2.set_ylim(-5, 1)
ax2.set_aspect('equal')
ax2.grid(True)

# Draw points
for label, (x, y) in {'P': P, 'Q': Q, 'R': R}.items():
    ax2.plot(x, y, 'o', color='black', markersize=6)
    ax2.text(x, y - 0.3, f'{label} ({x},{y})', fontsize=11, color='darkgreen')

# Draw free vectors
ax2.quiver(*P, *v, angles='xy', scale_units='xy', scale=1, color='purple', label='v: P→Q')
ax2.quiver(*Q, *w, angles='xy', scale_units='xy', scale=1, color='orange', label='w: Q→R')
ax2.quiver(*R, *u, angles='xy', scale_units='xy', scale=1, color='teal', label='u: R→P')

# Draw original bounded vectors with dashed, semi-transparent style
for label, (x, y) in {'P': P, 'Q': Q, 'R': R}.items():
    ax2.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1,
               color='gray', alpha=0.5, linestyle='dashed')

ax2.set_title('Free Vectors v, w, u + Bounded Vectors (Dashed)')
ax2.legend()


# === Third Plot: Bounded Vectors v, w, u from Origin ===
fig, ax3 = plt.subplots()
ax3.set_xlim(-5, 5)
ax3.set_ylim(-5, 5)
ax3.set_aspect('equal')
ax3.grid(True)

# Plot bounded vectors from origin
for label, (x, y), color in zip(['v', 'w', 'u'], [v, w, u], ['purple', 'orange', 'teal']):
    ax3.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color=color)
    ax3.plot(x, y, 'o', color='black', markersize=6)
    ax3.text(x + 0.5, y - 0.3, f'{label} ({x},{y})', fontsize=11, color=color)

# Origin marker
ax3.plot(0, 0, 'ko')
ax3.set_title('Bounded Vectors v, w, u from Origin')
ax3.set_xlabel('X-axis')
ax3.set_ylabel('Y-axis')


plt.show()