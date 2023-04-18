import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Set up the figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)

# Initialize the points
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

# Initialize the surface
surf = ax.plot_surface(X, Y, Z)

# Define the animation function
def animate(frame):
    # Update the surface heights with a new sine wave
    Z = np.sin(X + frame/10) + np.cos(Y + frame/10)
    surf.set_array(Z.ravel())
    return (surf,)

# Create the animation
anim = FuncAnimation(fig, animate, frames=100, interval=50)

# Show the animation
plt.show()
