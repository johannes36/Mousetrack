import tkinter as tk
from tkinter import ttk

from pageone import PageOne
from pagetwo import PageTwo

class MainView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.controller = None

        container = ttk.Frame(self, borderwidth=10, relief="sunken")
        container.grid(sticky="nsew", pady=20, padx=20)
        # container.pack(fill="both")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (PageOne, PageTwo):

            frame = F(parent=container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            # frame.pack(fill="both")
        self.showFrame_ButtonClicked(PageOne)



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
                print("save Funktion not yet implemented")
                #self.controller.save_DataToCSV(self.nameDataset_var.get())

    def start_ButtonClicked(self):
        if self.controller:
            self.controller.start_Tracking()

    def stop_ButtonClicked(self):
        if self.controller:
            self.controller.stop_Tracking()



    def showFrame_ButtonClicked(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  

    def nextPage_ButtonClicked(self):
        pass