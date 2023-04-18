import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)

# Initialize the line
line, = ax.plot([], [])

# Define the animation function
def animate(frame):
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x + frame/10)
    line.set_data(x, y)
    return (line,)

# Create the animation
anim = FuncAnimation(fig, animate, frames=100, interval=50)

# Show the animation
plt.show()
