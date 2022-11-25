import tkinter as tk
from tkinter import ttk

from viewer import MainView

from pagetwo_old import PageTwo

LARGE_FONT= ("Verdana", 12)

class PageOne(MainView):
    def __init__(self, parent, controller):
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

        self.ButtonNextPage = ttk.Button(self, text="next", command=self.showFrame_ButtonClicked(PageTwo))

"""
class FirstPage(MainView):
    def __init__(self, parent):
        super().__init__(parent)



 self.controller = controller
        #Different sections of page

        header = ttk.Frame(self, relief="raised", borderwidth=5)
        header.pack(fill="both", pady=20, padx=20)

        body = ttk.Frame(self, relief="sunken", borderwidth=5)
        body.pack(fill="both", pady=20, padx=20)
        
        control = ttk.Frame(self, relief="raised", borderwidth=5)
        control.pack(fill="both", pady=20, padx=20)

        #-------Header
        ttk.Label(header, text="Seite 1: Informationsabfrage", font=LARGE_FONT).pack(fill="both")

        #--------Body
        for row_index, key in enumerate(controller.dictUserInformation):
            # print(key)
            # print(controller.dictUserInformation[key])
            # print(controller.dictUserInformation[key]["name"])
            ttk.Label(body, text=controller.dictUserInformation[key]["name"]).grid(row=row_index, column=0, sticky="w")

        #   Eingabefelder Body
        #-----1------Entry Name Datensatz
        #------ wie adressierer ich dictionary, bzw. speichere Wert ab?
        ttk.Entry(body, textvariable=controller.entriesUserInformation[0]).grid(row=0, column=1)

        #-----2------Radiobutton starke Hand
        ttk.Radiobutton(body, text='links', variable=controller.entriesUserInformation[1], value='left').grid(row=1, column=1)
        ttk.Radiobutton(body, text='rechts', variable=controller.entriesUserInformation[1], value='rechts').grid(row=1, column=2)

        #-----3------Alter, eingabe über Combobox und liste von 20 bis 30 ------> alternative Lösung suchen(0-100 sind zu viele Werte)
        ttk.Entry(body, textvariable=controller.entriesUserInformation[2]).grid(row=2, column=1)
        ttk.Label(body, text="(Eingabe muss Ganzzahl sein(z.B. 23))").grid(row=2, column=2)

        #-----4------
        ttk.Radiobutton(body, text='1', variable=controller.entriesUserInformation[3], value=1).grid(row=3, column=1)
        ttk.Radiobutton(body, text='2', variable=controller.entriesUserInformation[3], value=2).grid(row=3, column=2)
        ttk.Radiobutton(body, text='3', variable=controller.entriesUserInformation[3], value=3).grid(row=3, column=3)

        #-----5------
        ttk.Radiobutton(body, text="männlich", variable=controller.entriesUserInformation[4], value="maennlich").grid(row=4, column=1)
        ttk.Radiobutton(body, text="weiblich", variable=controller.entriesUserInformation[4], value="weiblich").grid(row=4, column=2)
        ttk.Radiobutton(body, text="divers", variable=controller.entriesUserInformation[4], value="divers").grid(row=4, column=3)

        #-------Control #Buttoon zur Bestätigung? ---> Drücken übergibt werte an dict? bei next button press übergabe der Werte?
        button1 = ttk.Button(control, text="zurück zu Start",
                            command=lambda: controller.showFrame(StartPage))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(control, text="nächste Seite",
                            command=lambda: [controller.showFrame(PageTwo), controller.update_dict(controller.dictUserInformation, controller.entriesUserInformation)])
        button2.grid(row=0, column=1, sticky="e")
"""