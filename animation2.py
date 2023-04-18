import time
import tkinter as tk


class TextAnimation:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg='white')
        self.canvas.pack()
        self.text = self.canvas.create_text(
            200, 200, text='Hello, World!', font=('Arial', 30))
        self.dx = 5  # move text 5 pixels to the right each frame
        self.animate()

    def animate(self):
        self.canvas.move(self.text, self.dx, 0)
        coords = self.canvas.coords(self.text)

        if coords[0] < 0 or coords[1] > 400:  # if text goes off screen, reverse direction
            self.dx *= -1
        color = '#' + format(int((time.time() * 1000) % 1536),'03x')  # calculate color based on time
        self.canvas.itemconfig(self.text, fill=color)  # set text color
        self.canvas.after(20, self.animate)


if __name__ == '__main__':
    root = tk.Tk()
    app = TextAnimation(root)
    root.mainloop()
