import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image, ImageDraw, ImageFont

# Define the figure and axes
fig, ax = plt.subplots()
fig.set_size_inches(8, 6)
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])

# Define the text to animate
text = 'Hello World!'
font_size = 60
font = ImageFont.truetype('arial.ttf', font_size)
text_width, text_height = font.getsize(text)

# Define the text artist
background = Image.new('RGBA', (800, 600), (255, 255, 255, 255))
draw = ImageDraw.Draw(background)
draw.text(((800 - text_width) / 2, (600 - text_height) / 2), text, font=font, fill=(0, 0, 0, 255))
background = np.array(background)
text_artist = ax.imshow(background, extent=[-5, 5, -5, 5], alpha=0.5)

# Define the animation function
def animate(frame):
    # Calculate the x and y positions based on the current frame
    x = np.sin(frame * np.pi / 50) * 2
    y = np.cos(frame * np.pi / 50) * 2

    # Update the background image with the new position
    background = Image.new('RGBA', (800, 600), (255, 255, 255, 255))
    draw = ImageDraw.Draw(background)
    draw.text(((800 - text_width) / 2 + x*30, (600 - text_height) / 2 + y*30), text, font=font, fill=(0, 0, 0, 255))
    background = np.array(background)

    # Update the text artist
    text_artist.set_data(background)

# Create the animation
animation = FuncAnimation(fig, animate, frames=200, interval=50)

# Show the animation
plt.show()
