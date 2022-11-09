import tkinter as tk
from tkinter import ttk

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ttk.Label(self, text = "Seite xy")
        self.label.grid(row=0, column=0)

        self.Button = ttk.Button(self, text="Starte", command= self.first_ButtonClicked)
        self.Button.grid(row=1, column=0)

        self.Button2 = ttk.Button(self, text="Stoppe", command= self.second_ButtonClicked)
        self.Button2.grid(row=2, column=0)
 
        
        self.controller = None


    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller


    def first_ButtonClicked(self):
        if self.controller:
            self.controller.start_Tracking()

    def second_ButtonClicked(self):
        if self.controller:
            self.controller.stop_Tracking()