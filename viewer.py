import tkinter as tk
from tkinter import ttk

from pageone import PageOne
from pagetwo import PageTwo

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # self.parent = parent

        self.controller = None

        self._frame = None

        self.page1 = PageOne(parent)
        
        self.page2 = PageTwo(parent)
        
        # self.bind_commands()#page1=PageOne, page2=PageTwo)
        self.show_Page(self.page1)


    

    def bind_commands(self, page1, page2):
        #Achtung, unsinnig, doppelter Aufruf!
        self.page1.buttons["Show Page2"].configure(command= lambda: [self.show_Page(page2), print("Show page 2 pressed")])
        
        
        self.page2.buttons["Show Page1"].configure(command= self.show_Page(page1))

    
    def show_Page(self, frame_class):
        new_frame = frame_class
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()

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


