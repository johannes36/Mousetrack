# python -m pip --version
#-TKINTER STYLE CONSTANTS
import tkinter as tk

from model import Model
from viewer import MainView
from controller import Controller

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Mousetrack')

        model = Model()

        view = MainView(self)
        view.grid(row = 0, column=0, padx= 10, pady = 10)
        

        controller = Controller(model, view)

        view.set_controller(controller)



if __name__ == "__main__":
    app = App()
    app.mainloop()
