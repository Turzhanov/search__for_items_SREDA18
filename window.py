import tkinter as tk

class Window(tk.Tk):
    def __init__(self, title, width, height):
        self.tit = title
        self.width = width
        self.height = height
        super().__init__()
        self.geometry(f"{self.width}x{self.height}")
        self.title(self.tit)
        self.resizable(False, False)
