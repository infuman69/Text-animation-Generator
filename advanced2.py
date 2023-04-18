import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the text to be animated
text = "Hello, world!"
n = len(text)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 3))
ax.set_xlim(0, n)
ax.set_ylim(0, 1)

# Create the text object
text_obj = ax.text(0, 0.5, "", fontsize=20)

# Define the animation function
def animate(frame):
    text_obj.set_text(text[:frame+1])
    return text_obj,

# Create the animation
anim = FuncAnimation(fig, animate, frames=n, interval=200)

# Show the animation
plt.show()
