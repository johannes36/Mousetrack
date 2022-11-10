import tkinter as tk
from tkinter import ttk

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ttk.Label(self, text = "Seite xy")
        self.label.grid(row=0, column=0)

        self.Button = ttk.Button(self, text="Starte", command= self.start_ButtonClicked)
        self.Button.grid(row=1, column=0)

        self.Button2 = ttk.Button(self, text="Stoppe", command= self.stop_ButtonClicked)
        self.Button2.grid(row=2, column=0)

        self.label = ttk.Label(self, text="Name Datensatz:")
        self.label.grid(row = 3, column=0)

        self.nameDataset_var = tk.StringVar()
        self.Entry = ttk.Entry(self, textvariable=self.nameDataset_var, width=30)
        self.Entry.grid(row=3, column=1)

        self.save_Button = ttk.Button(self, text="Save", command=self.save_button_clicked)
        self.save_Button.grid(row=4, column=0)
 
        
        self.controller = None





    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller


    def save_button_clicked(self):
            """
            Handle button click event
            :return:
            """
            if self.controller:
                self.controller.save_DataToCSV(self.nameDataset_var.get())

    def start_ButtonClicked(self):
        if self.controller:
            self.controller.start_Tracking()

    def stop_ButtonClicked(self):
        if self.controller:
            self.controller.stop_Tracking()