import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Function to plot a sphere
def plot_sphere(center, radius):
    a, b, c = center  # Unpack the center coordinates
    
    # Create a grid of points for the sphere
    u = np.linspace(0, 2 * np.pi, 100)  # Angular coordinates for longitude
    v = np.linspace(0, np.pi, 100)      # Angular coordinates for latitude

    # Compute the x, y, z coordinates of the sphere surface
    x = a + radius * np.outer(np.cos(u), np.sin(v))
    y = b + radius * np.outer(np.sin(u), np.sin(v))
    z = c + radius * np.outer(np.ones_like(u), np.cos(v))

    # Create a 3D figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the sphere surface
    ax.plot_surface(x, y, z, color='blue', alpha=0.6, label='Sphere Surface')

    # Plot the center point
    ax.scatter(a, b, c, color='red', label=f'Center ({a}, {b}, {c})', s=100)

    # Label the axes
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    # Add a title
    ax.set_title(f"Sphere at ({a}, {b}, {c}) with radius {radius}")

    # Set limits for the axes
    ax.set_xlim([a - radius - 1, a + radius + 1])
    ax.set_ylim([b - radius - 1, b + radius + 1])
    ax.set_zlim([c - radius - 1, c + radius + 1])

    # Add legend
    ax.legend()

    # Show the plot
    plt.show()

# Parameters
center = (2, 3, 5)  # Center of the sphere (a, b, c)
radius = 4          # Radius of the sphere

# Call the function to plot the sphere
plot_sphere(center, radius)