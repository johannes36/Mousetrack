import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        #Different sections of page
        # header = ttk.Frame(self, relief="raised", borderwidth=5)
        # header.grid(row=0, column=0, sticky="nsew")

        # body = ttk.Frame(self, relief="sunken", borderwidth=5)
        # body.grid(row=1, column=0, sticky="nsew")
        
        # control = ttk.Frame(self, relief="raised", borderwidth=5)
        # control.grid(row=2, column=0, sticky="nsew")

        header = ttk.Frame(self, relief="raised", borderwidth=5)
        header.pack(fill="both", pady=20, padx=20)

        body = ttk.Frame(self, relief="sunken", borderwidth=5)
        body.pack(fill="both", pady=20, padx=20)
        
        control = ttk.Frame(self, relief="raised", borderwidth=5)
        control.pack(fill="both", pady=20, padx=20)



        #content of different section
        # ------- Header
        label_header = ttk.Label(header, text="Startseite der Anwendung Mousetrack", font=LARGE_FONT)
        label_header.grid()

        #----------body statt label tk.Text??!!
        label_body = ttk.Label(body, text="Hier könnte ein Informationstext für Anwender stehen")
        label_body.grid()

        # -----------Control
        ttk.Label(control, text="Dies ist der Kontrollbereich").grid(row=0, column=0)

        ttk.Button(control, text="nächste Seite",
                            command=lambda: controller.showFrame(PageOne)).grid(row=1, column=0)

        ttk.Button(control, text="Seite 2",
                            command=lambda: controller.showFrame(PageTwo)).grid(row=1, column=1)
