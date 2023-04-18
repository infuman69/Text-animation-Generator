import tkinter as tk

class App:
    def __init__(self, master, text):
        self.master = master
        self.text = text
        self.canvas = tk.Canvas(master, width=400, height=200)
        self.canvas.pack()
        self.draw_text()

    def draw_text(self):
        x = 0
        y = 50
        for i, char in enumerate(self.text):
            self.canvas.create_text(x, y, text=char, font=("Arial", 24), fill="black", tags="text")
            x += 20
            if i % 20 == 19:
                y += 40
                x = 0
            self.canvas.update()
            self.canvas.after(50)

root = tk.Tk()
app = App(root, "Hello, World!")
root.mainloop()
