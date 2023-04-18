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
        self.dy = 5  # move text 5 pixels down each frame
        self.animate()

    def animate(self):
        self.canvas.move(self.text, self.dx, self.dy)
        coords = self.canvas.coords(self.text)
        if coords[0] < 0 or coords[1] > 400: # if text hits left or right wall, reverse x direction
            self.dx *= -1
        if coords[1] < 0 or coords[0] > 400: # if text hits top or bottom wall, reverse y direction
            self.dy *= -1
        self.canvas.after(20, self.animate)


if __name__ == '__main__':
    root = tk.Tk()
    app = TextAnimation(root)
    root.mainloop()
