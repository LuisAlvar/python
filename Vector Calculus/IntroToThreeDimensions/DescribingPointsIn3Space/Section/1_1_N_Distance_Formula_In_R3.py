import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Function to calculate the distance and print the derivation
def derive_distance_formula(point1, point2):
    print("### Derivation of the Distance Formula in R^3 ###")
    print("The distance formula: d = sqrt((Δx)^2 + (Δy)^2 + (Δz)^2)")

    # Extract coordinates
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    # Calculate differences
    delta_x = x2 - x1
    delta_y = y2 - y1
    delta_z = z2 - z1

    # Calculate the squared differences and final distance
    distance = math.sqrt(delta_x**2 + delta_y**2 + delta_z**2)
    print(f"The distance between points {point1} and {point2} is: {distance:.2f}")
    return distance, delta_x, delta_y, delta_z

# Points in 3D space
point1 = (2, -1, 5)
point2 = (-3, 4, 8)

# Calculate the distance and differences
distance, delta_x, delta_y, delta_z = derive_distance_formula(point1, point2)

# Plotting in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract coordinates
x_coords = [point1[0], point2[0]]
y_coords = [point1[1], point2[1]]
z_coords = [point1[2], point2[2]]

# Plot the two points
ax.scatter(point1[0], point1[1], point1[2], color='red', label='Point 1 (2, -1, 5)', s=50)
ax.scatter(point2[0], point2[1], point2[2], color='blue', label='Point 2 (-3, 4, 8)', s=50)

# Plot the line connecting the two points
ax.plot(x_coords, y_coords, z_coords, color='green', label=f'Line (Distance = {distance:.2f})')

# Shaded triangle to represent differences and distance
triangle_vertices = [
    [point1[0], point1[1], point1[2]],
    [point2[0], point1[1], point1[2]],
    [point2[0], point2[1], point1[2]]
]

# Add the shaded triangle
ax.add_collection3d(Poly3DCollection([triangle_vertices], alpha=0.3, color='cyan', label='Shaded Triangle'))

# Plot edges to illustrate deltas
# Δx edge
ax.plot([point1[0], point2[0]], [point1[1], point1[1]], [point1[2], point1[2]], color='orange', label='Δx')
ax.text((point1[0] + point2[0]) / 2, point1[1], point1[2], f'Δx = {delta_x}', color='orange')

# Δy edge
ax.plot([point2[0], point2[0]], [point1[1], point2[1]], [point1[2], point1[2]], color='purple', label='Δy')
ax.text(point2[0], (point1[1] + point2[1]) / 2, point1[2], f'Δy = {delta_y}', color='purple')

# Δz edge
ax.plot([point2[0], point2[0]], [point2[1], point2[1]], [point1[2], point2[2]], color='brown', label='Δz')
ax.text(point2[0], point2[1], (point1[2] + point2[2]) / 2, f'Δz = {delta_z}', color='brown')

# Label the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Add a title
ax.set_title('3D Visualization of Distance with Shading and Delta Values')

# Add legend
ax.legend()

# Show the plot
plt.show()