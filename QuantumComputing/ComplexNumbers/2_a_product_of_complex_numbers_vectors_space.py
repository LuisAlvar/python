import matplotlib.pyplot as plt

# Define complex numbers
C1 = complex(-2, -1)
C2 = complex(-1, -2)
C_product = C1 * C2  # Expected: 0 + 5i

# First plot: C1 and C2 only
fig1, ax1 = plt.subplots()
ax1.set_title('Complex Vectors: C₁ and C₂')
ax1.set_xlabel('Real')
ax1.set_ylabel('Imaginary')
ax1.quiver(0, 0, C1.real, C1.imag, angles='xy', scale_units='xy', scale=1, color='blue', label='C₁ = -2 - i')
ax1.quiver(0, 0, C2.real, C2.imag, angles='xy', scale_units='xy', scale=1, color='green', label='C₂ = -1 - 2i')
ax1.set_xlim(-3, 1)
ax1.set_ylim(-3, 1)
ax1.grid(True)
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.legend()
ax1.set_aspect('equal')

# Second plot: C1, C2, and the product
fig2, ax2 = plt.subplots()
ax2.set_title('Complex Vectors: C₁, C₂, and Their Product')
ax2.set_xlabel('Real')
ax2.set_ylabel('Imaginary')
ax2.quiver(0, 0, C1.real, C1.imag, angles='xy', scale_units='xy', scale=1, color='blue', label='C₁ = -2 - i')
ax2.quiver(0, 0, C2.real, C2.imag, angles='xy', scale_units='xy', scale=1, color='green', label='C₂ = -1 - 2i')
ax2.quiver(0, 0, C_product.real, C_product.imag, angles='xy', scale_units='xy', scale=1, color='red', label='C₁ × C₂ = 5i')
ax2.set_xlim(-3, 1)
ax2.set_ylim(-3, 6)
ax2.grid(True)
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.legend()
ax2.set_aspect('equal')

# Show plots
plt.show()