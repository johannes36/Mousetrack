import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)

class PageThree(tk.Frame):
    #3te Seite, die das Livemenü darstellen soll
    #evtl. simple Dinge live anzeigen
    #ansonsten einfach nur simple Optionen (Start oder Stopp)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
       
        header = ttk.Frame(self, relief="raised", borderwidth=5)
        header.grid(row=0, column=0, sticky="nsew")
                
        control = ttk.Frame(self, relief="raised", borderwidth=5)
        control.grid(row=1, column=0, sticky="nsew")

        #-------Header
        ttk.Label(header, text="Seite 3, Livemenü").grid()


        #-------Control
        button1 = ttk.Button(control, text="Anwendung pausieren")#,
                            #command=lambda: controller.showFrame(PageThree))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(control, text="Tracking stoppen und  zu Auswertung",
                            command=lambda: [controller.showFrame(PageFour), controller.tracking(active=False)])
        button2.grid(row=0, column=1)
