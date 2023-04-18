import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.spatial.transform import Rotation

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate the x, y, and z arrays
N = 100
X, Y = np.meshgrid(np.linspace(-1, 1, N), np.linspace(-1, 1, N))
Z = np.sin(np.sqrt(X**2 + Y**2)) / (np.sqrt(X**2 + Y**2))

# Create the surface plot
surf = ax.plot_surface(X, Y, Z, cmap='magma', rstride=1, cstride=1)

def animate(frame):
    # Update the surface heights with a new function
    Z = np.sin(np.sqrt(X**2 + Y**2 + frame/10)) / (np.sqrt(X**2 + Y**2))
    surf.set_array(Z.ravel())
    
    # Rotate the surface around the y-axis
    points = np.column_stack([X.ravel(), Y.ravel(), Z.ravel()])
    rot_points = Rotation.from_euler('y', frame/5, degrees=True).apply(points)
    x_rot, y_rot, z_rot = rot_points[:, 0], rot_points[:, 1], rot_points[:, 2]
    surf._offsets3d = (x_rot, y_rot, z_rot)
    
    return (surf,)

# Create the animation
anim = FuncAnimation(fig, animate, frames=200, interval=20, blit=True)

# Show the animation
plt.show()
