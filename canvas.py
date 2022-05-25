import tkinter as tk


class Canvas(tk.Canvas):
    """
        Создает экземпляр класса холста на окне window в указанных координатах
    """
    def __init__(self, window, width, height):
        super().__init__(window, width = width, height = height)
        self.pack()

