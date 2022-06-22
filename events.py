from window import Window
window = Window("События", 300 ,300)

def up(event):
    x = event.x
    y = event.y
    print("Клавиша стрелка вверх нажата")
    print(event)
    print(f"Координата X {event.x}, координата Y {event.y}")

def double_B1(event):
    x = event.x
    y = event.y
    print("Левая кнопка мыши нажата дважды")
    print(event)
    print(f"Координата X {event.x}, координата Y {event.y}")

        



window.bind("<Up>", up)
window.bind("<Double-Button-1>", double_B1)
window.mainloop()
