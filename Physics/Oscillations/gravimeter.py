import numpy as np
import matplotlib.pyplot as plt
import mplcursors

# Original dataset
time = np.array([141.7, 200.6, 245.8, 283.5])
length = np.array([0.500, 1.00, 1.500, 2.00])

# Modified dataset (dividing by 100)
time_scaled = pow(time / 100, 2)
length_scaled = length

# Calculate linear regression for the scaled dataset
slope, intercept = np.polyfit(time_scaled, length_scaled, 1)
regression_line = slope * time_scaled + intercept

# Create figure with two plots
fig, axs = plt.subplots(2, 1, figsize=(8, 10))  # Two separate plots stacked vertically

# First plot: Original dataset without regression
axs[0].plot(time, length, marker='o', linestyle='-', color='b', label="Original Data")
axs[0].set_xlabel("Time (seconds)")
axs[0].set_ylabel("Length (meters)")
axs[0].set_title("Original Dataset")
axs[0].legend()
axs[0].grid(True)

# Add static labels for original dataset
for t, l in zip(time, length):
    axs[0].annotate(f"{l:.3f}m", (t, l), textcoords="offset points", xytext=(5,5), ha='center', fontsize=10, color='darkred')

# Second plot: Scaled dataset with linear regression
axs[1].plot(time_scaled, length_scaled, marker='o', linestyle='-', color='g', label="Scaled Data")
axs[1].plot(time_scaled, regression_line, linestyle="--", color="red", label=f"Linear Fit: y = {slope:.4f}x + {intercept:.4f}")
axs[1].set_xlabel("Time (scaled) s^2 (T^2)")
axs[1].set_ylabel("Length (scaled)")
axs[1].set_title("Scaled Dataset with Linear Regression")
axs[1].legend()
axs[1].grid(True)

# Add static labels for scaled dataset
for t, l in zip(time_scaled, length_scaled):
    axs[1].annotate(f"{l:.3f}", (t, l), textcoords="offset points", xytext=(5,5), ha='center', fontsize=10, color='darkred')

# Enable interactive tooltips for both plots
cursor = mplcursors.cursor(hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(f"Time: {sel.target[0]:.3f}\nLength: {sel.target[1]:.3f}"))

# Show the plots
plt.tight_layout()
plt.show()

# Print the linear equation for the scaled dataset
print(f"The linear equation for the scaled dataset is: y = {slope:.4f}x + {intercept:.4f}")