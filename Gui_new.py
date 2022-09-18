import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        self.data_info = {
            "info_1":    {"name" : "Name Datensatz:",   "value" : tk.StringVar()},
            "info_2":    {"name" : "Starke Hand:",      "value" : tk.StringVar()},
            "info_3":    {"name" : "Alter:",            "value" : tk.IntVar()},
            "info_4":    {"name" : "Technikaffinität:", "value" : tk.IntVar()},
            "info_5":    {"name" : "Geschlecht:",       "value" : tk.StringVar()},
            }
        self.entries_info = [tk.StringVar(), tk.StringVar(), tk.IntVar(), tk.IntVar(), tk.StringVar()]

        self.data_setting = {
            "setting_1": {"name" : "Geschwindigkeit",  "value" : tk.BooleanVar()},
            "setting_2": {"name" : "Beschleunigung",   "value" : tk.BooleanVar()},
            "setting_3": {"name" : "Speichern",        "value" : tk.BooleanVar()},
        }
        # self.entries_setting = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]

        #-----window geometry
        self.title("Mousetrack")
                
        window_width  = 500
        window_height = 500

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        

        #---container, evtl. header, ... hier hinzufügen
        container = tk.Frame(self, borderwidth=10, relief="sunken")
        container.grid(sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
    
    

    def update_dict(self): #update dictionary wihle operating through list of entrys

        for index, key in enumerate(self.data_info):
            self.data_info[key]["value"] = self.entries_info[index].get()
            print(self.entries_info[index])
            print(self.data_info[key]["value"])

        print(self.data_info)



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        #Different sections of page
        header = ttk.Frame(self, relief="raised", borderwidth=5)
        header.grid(row=0, column=0, sticky="nsew")

        body = ttk.Frame(self, relief="sunken", borderwidth=5)
        body.grid(row=1, column=0, sticky="nsew")
        
        control = ttk.Frame(self, relief="raised", borderwidth=5)
        control.grid(row=2, column=0, sticky="nsew")


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
                            command=lambda: controller.show_frame(PageOne)).grid(row=1, column=0)

        ttk.Button(control, text="Seite 2",
                            command=lambda: controller.show_frame(PageTwo)).grid(row=1, column=1)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #Different sections of page

        header = ttk.Frame(self, relief="raised", borderwidth=5)
        header.grid(row=0, column=0, sticky="nsew")

        body = ttk.Frame(self, relief="sunken", borderwidth=5)
        body.grid(row=1, column=0, sticky="nsew")
        
        control = ttk.Frame(self, relief="raised", borderwidth=5)
        control.grid(row=2, column=0, sticky="nsew")

        #-------Header
        ttk.Label(header, text="Seite 1: Informationsabfrage", font=LARGE_FONT).grid()

        #--------Body
        for row_index, key in enumerate(controller.data_info):
            # print(key)
            # print(controller.data_info[key])
            # print(controller.data_info[key]["name"])
            ttk.Label(body, text=controller.data_info[key]["name"]).grid(row=row_index, column=0, sticky="w")

        #   Eingabefelder Body
        #-----1------Entry Name Datensatz
        #------ wie adressierer ich dictionary, bzw. speichere Wert ab?
        ttk.Entry(body, textvariable=controller.entries_info[0]).grid(row=0, column=1)

        #-----2------Radiobutton starke Hand
        ttk.Radiobutton(body, text='links', variable=controller.entries_info[1], value='left').grid(row=1, column=1)
        ttk.Radiobutton(body, text='rechts', variable=controller.entries_info[1], value='rechts').grid(row=1, column=2)

        #-----3------Alter, eingabe über Combobox und liste von 20 bis 30 ------> alternative Lösung suchen(0-100 sind zu viele Werte)
        ttk.Entry(body, textvariable=controller.entries_info[2]).grid(row=2, column=1)
        ttk.Label(body, text="(Eingabe muss Ganzzahl sein(z.B. 23))").grid(row=2, column=2)

        #-----4------
        ttk.Radiobutton(body, text='1', variable=controller.entries_info[3], value=1).grid(row=3, column=1)
        ttk.Radiobutton(body, text='2', variable=controller.entries_info[3], value=2).grid(row=3, column=2)
        ttk.Radiobutton(body, text='3', variable=controller.entries_info[3], value=3).grid(row=3, column=3)

        #-----5------
        ttk.Radiobutton(body, text="männlich", variable=controller.entries_info[4], value="maennlich").grid(row=4, column=1)
        ttk.Radiobutton(body, text="weiblich", variable=controller.entries_info[4], value="weiblich").grid(row=4, column=2)
        ttk.Radiobutton(body, text="divers", variable=controller.entries_info[4], value="divers").grid(row=4, column=3)

        #-------Control #Buttoon zur Bestätigung? ---> Drücken übergibt werte an dict? bei next button press übergabe der Werte?
        button1 = ttk.Button(control, text="zurück zu Start",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(control, text="nächste Seite",
                            command=lambda: [controller.show_frame(PageTwo), controller.update_dict()])
        button2.grid(row=0, column=1, sticky="e")


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
        for row_index, key in enumerate(controller.data_setting):
            print(controller.data_setting[key]["name"])
            print(row_index)
            ttk.Checkbutton(body, text=controller.data_setting[key]["name"],
                            variable= controller.data_setting[key]["value"],
                            onvalue=True, offvalue=False).grid(row=row_index+1, column=0, sticky="w")
        
        #----Entry

        # ttk.Checkbutton(body, text="Tracken?").grid(row=0, column=1)#, text='links', variable=controller.entries_setting[1], value='left').grid(row=1, column=1)
        # ttk.Checkbutton(body, text='rechts', variable=controller.entries_setting[1], value='rechts').grid(row=1, column=2)

        #----------Controls
        button1 = ttk.Button(control, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(control, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.grid(row=0, column=1)
        
class PageThree():
    #3te Seite, die das Livemenü darstellen soll
    #evtl. simple Dinge live anzeigen
    #ansonsten einfach nur simple Optionen (Start oder Stopp)
    pass

class PageFour():
    #4te Seite des Gui, die der Darstellung der Informationen dienen soll
    pass

class Tracking():
    #Klasse in der alle Trackingfunktionen gespeichert werden
    pass

app = App()
app.mainloop()