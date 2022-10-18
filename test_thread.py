import tkinter as tk
from tkinter import ttk

from pynput import mouse as mouse


def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))


def startApp():
    global listener
    listener = mouse.Listener(on_move=on_move, on_click=on_click)
    listener.start()

def stopApp():
    listener.stop()
    print("Stopped")
    


root = tk.Tk()

buttonStart = tk.Button(root, text="Starte Listener & Thread", command=startApp).grid(row=0, column=0)
buttonStopp = tk.Button(root, text="Stoppe Listener & Thread", command=stopApp).grid(row=0, column=1)

root.mainloop()