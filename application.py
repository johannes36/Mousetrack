# python -m pip --version
#-TKINTER STYLE CONSTANTS
import tkinter as tk

from model import Model
from viewer import View
from controller import Controller

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Mousetrack')        
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        model = Model()

        view = View(self)

        view.grid(row = 0, column=0, padx= 10, pady = 10)
        
        controller = Controller(model, view)


        view.set_controller(controller)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
