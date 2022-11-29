import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        header = ttk.Frame(self, relief="raised", borderwidth=5)
        header.grid(row=0, column=0, sticky="nsew")

        body = ttk.Frame(self, relief="sunken", borderwidth=5)
        body.grid(row=1, column=0, sticky="nsew")
        
        control = ttk.Frame(self, relief="raised", borderwidth=5)
        control.grid(row=2, column=0, sticky="nsew")

        #----------Header
        ttk.Label(header, text="Seite 2: Einstellungen", font=LARGE_FONT).grid()

        #----------Body
        ttk.Label(body, text="gewünschte Optionen auswählen:").grid(row=0, column=0)
        for index, key in enumerate(controller.dictUserSettings):
            # print(controller.dictUserSettings[key]["name"])
            # print(index)
            ttk.Checkbutton(body, text=controller.dictUserSettings[key]["name"],
                            variable= controller.entriesUserSettings[index],
                            onvalue=True, offvalue=False).grid(row=index+1, column=0, sticky="w")       #schöner: variable= controller.dictUserSettings[key]["value"],
        
        #----Entry

        # ttk.Checkbutton(body, text="Tracken?").grid(row=0, column=1)#, text='links', variable=controller.entriesUserSettings[1], value='left').grid(row=1, column=1)
        # ttk.Checkbutton(body, text='rechts', variable=controller.entriesUserSettings[1], value='rechts').grid(row=1, column=2)

        #----------Controls
        button1 = ttk.Button(control, text="vorherige Seite",
                            command=lambda: controller.showFrame(PageOne))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(control, text="Anwendung starten",
                            command=lambda: [controller.showFrame(PageThree), controller.update_dict(controller.dictUserSettings, controller.entriesUserSettings),  controller.tracking(active=True)])
        button2.grid(row=0, column=1)
