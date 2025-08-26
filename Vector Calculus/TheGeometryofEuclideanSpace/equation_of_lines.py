import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define vectors
a = np.array([1, 2])
v = np.array([2, 1])

# Setup plot
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title("Visualizing l(t) = a + t·v")

# Draw static vectors a and v
ax.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='blue', label='a')
ax.quiver(a[0], a[1], v[0], v[1], angles='xy', scale_units='xy', scale=1, color='green', label='v')

# Initialize animated elements
tv_arrow = ax.quiver(a[0], a[1], 0, 0, angles='xy', scale_units='xy', scale=1, color='orange', label='t·v')
lt_point, = ax.plot([], [], 'ro', label='l(t)')
trace, = ax.plot([], [], 'r--', linewidth=1)

# Labels
a_label = ax.text(a[0]/2, a[1]/2, 'a', color='blue')
v_label = ax.text(a[0] + v[0]/2, a[1] + v[1]/2, 'v', color='green')
tv_label = ax.text(0, 0, '', color='orange')
lt_label = ax.text(0, 0, '', color='red')

trace_x, trace_y = [], []

def init():
    lt_point.set_data([], [])
    trace.set_data([], [])
    tv_arrow.set_UVC(0, 0)
    tv_label.set_text('')
    lt_label.set_text('')
    return tv_arrow, lt_point, trace, tv_label, lt_label

def update(frame):
    t = frame / 10.0 - 5
    tv = t * v
    lt = a + tv

    # Update t·v arrow
    tv_arrow.set_UVC(tv[0], tv[1])
    tv_label.set_position((a[0] + tv[0]/2, a[1] + tv[1]/2))
    tv_label.set_text(f't·v (t={t:.1f})')

    # Update l(t) point
    lt_point.set_data([lt[0]], [lt[1]])
    lt_label.set_position((lt[0] + 0.3, lt[1]))
    lt_label.set_text('l(t)')

    # Update trace
    trace_x.append(lt[0])
    trace_y.append(lt[1])
    trace.set_data(trace_x, trace_y)

    return tv_arrow, lt_point, trace, tv_label, lt_label

ani = animation.FuncAnimation(fig, update, frames=100, init_func=init,
                              blit=True, interval=100, repeat=False)

ax.legend()
plt.show()