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
from window import Window

window = Window("События", 300, 300)

def right(event):

    print("Клавиша стрелка вправо нажата")

    print(event)

    print(f"Координата X {event.x}, Координата Y {event.y}")



window.bind("<Right>", right)



def motion(event):

    print("Перемещение мыши")

    print(event)

    print(f"Координата X {event.x}, Координата Y {event.y}")



window.bind("<Motion>", motion)

window.mainloop() 


window.mainloop()