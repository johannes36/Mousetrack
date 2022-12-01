import tkinter as tk
from tkinter import ttk

from pageone import PageOne
from pagetwo import PageTwo

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # self.parent = parent

        self.controller = None

        self._actualShownPage = None


        self.page1 = PageOne(parent)
        self.page2 = PageTwo(parent)
        
        # new approach
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.bind_commandsToButtons(page1=self.page1, page2=self.page2)

        self.frames = {}

        for F in (PageOne, PageTwo):
            frame = F(master=container)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

            frame.rowconfigure(0, weight=1)
            frame.columnconfigure(0, weight=1)

        # self.show_Page("PageOne")
        # self.bind_commands()#page1=PageOne, page2=PageTwo)
        self.show_Page(self.page1)

 

    def bind_commandsToButtons(self, page1: PageOne, page2: PageTwo):
        page1.buttons["Show Page 2"].configure(command= lambda: [self.show_Page(page2), print("Show page 2 pressed")])
        print(page1.buttons)
        page2.buttons["Show Page 1"].configure(command= lambda: [self.show_Page(page1), print("Show page 1 pressed")])

    
    def show_Page(self, page_toShow):
        frame = self.frames[page_toShow]
        print("Show Page pressed succesfull")
        frame.tkraise()

        if self._actualShownPage is not None:
            self._actualShownPage.destroy()

        self._actualShownPage = page_toShow
        self._actualShownPage.grid()
        self._actualShownPage.tkraise()

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


