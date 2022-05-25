import tkinter as tk

from window import Window
from canvas import Canvas
from new_image import NewImg


from constants import WIDTH
from constants import HEIGHT

state = "menu"

window = Window("Найди предметы", WIDTH, HEIGHT)

canvas = Canvas(window, WIDTH, HEIGHT)

  

menu_buttons = []
background = NewImg(canvas, "images/background.png", 0, 0)



window.mainloop()