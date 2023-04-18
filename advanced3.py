import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image, ImageDraw, ImageFont

# Define the figure and axes
fig, ax = plt.subplots()
fig.set_size_inches(8, 6)
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

# Define the background image
background = Image.new('RGBA', (800, 600), (255, 255, 255, 255))
draw = ImageDraw.Draw(background)
font = ImageFont.truetype('arial.ttf', 40)
draw.text((400, 300), 'Hello World', font=font, fill=(0, 0, 0, 255))
background = np.array(background)

# Define the text artist
text_artist = ax.imshow(background, extent=[0, 1, 0, 1], alpha=0.5)

# Define the animation function
def animate(frame):
    # Move the text artist
    x, y = np.random.rand(2)
    text_artist.set_extent([x, x + 1, y, y + 1])

    # Update the background image
    background = Image.new('RGBA', (800, 600), (255, 255, 255, 255))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('arial.ttf', 40)
    draw.text((400, 300), 'Hello World', font=font, fill=(0, 0, 0, 255))
    background = np.array(background)

    # Update the text artist
    text_artist.set_data(background)

# Create the animation
animation = FuncAnimation(fig, animate, frames=100, interval=50)

# Show the animation
plt.show()
