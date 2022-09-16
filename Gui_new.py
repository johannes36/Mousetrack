import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        self.app_data = {
            "name_datensatz": tk.StringVar(),
            "starke_hand"   : tk.StringVar(),
            "alter"         : tk.IntVar(),
            "technikaffinitaet": tk.IntVar(),
            "geschlecht"    : tk.StringVar(),
            "geschwindigkeit": tk.BooleanVar(),
            "beschleunigung": tk.BooleanVar(),
            "speichern"     : tk.BooleanVar(),
        }


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
    
    def print_dict(self):
        # datensatz = self.app_data["name_datensatz"].get()
        # print(f"Name des Datensatz ist: {datensatz}")
        # print(self.app_data.values())
        value = list(self.app_data.values())
        # for i in range(len(self.app_data)):
        #     # value[i] = self.app_data[i].get()
        #     print(self.app_data[i])
        print(value)
        
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
        label_header = ttk.Label(header, text="Head of Start Page", font=LARGE_FONT)
        label_header.grid()

        #----------body
        label_body = ttk.Label(body, text="Body of Start Page", font=LARGE_FONT)
        label_body.grid()

        # -----------Control
        ttk.Label(control, text="Control of Start Page", font=LARGE_FONT).grid(row=0, column=0)

        ttk.Button(control, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne)).grid(row=1, column=0)

        ttk.Button(control, text="Visit Page 2",
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
        label_abfrage = ["Datensatz Name:", "starke Hand:", "Alter:", "Technikaffinität:", "Geschlecht:"] #Label über Dictionary adressieren?
        for index_row, text in enumerate(label_abfrage):
            ttk.Label(body, text=text).grid(row=index_row, column=0, sticky="w")

        #   Eingabefelder Body
        #-----1------Entry Name Datensatz
        ttk.Entry(body, textvariable=self.controller.app_data["name_datensatz"]).grid(row=0, column=1)

        #Testbutton
        ttk.Button(body, text="print Dict", command=lambda: controller.print_dict()).grid(row=0, column=2)

        #-----2------Radiobutton starke Hand
        ttk.Radiobutton(body, text='links', variable=self.controller.app_data["starke_hand"], value='left').grid(row=1, column=1)
        ttk.Radiobutton(body, text='rechts', variable=self.controller.app_data["starke_hand"], value='rechts').grid(row=1, column=2)

        #-----3------Alter, eingabe über Combobox und liste von 20 bis 30 ------> alternative Lösung suchen(0-100 sind zu viele Werte)
        ttk.Entry(body, textvariable=self.controller.app_data["alter"]).grid(row=2, column=1)
        ttk.Label(body, text="(Eingabe muss Ganzzahl sein(z.B. 23))").grid(row=2, column=2)

        #-----4------

        #-----5------

        #-------Control #Buttoon zur Bestätigung? ---> Drücken übergibt werte an dict? bei next button press übergabe der Werte?
        button1 = ttk.Button(control, text="Back to Start",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(control, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=0, column=1, sticky="e")


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        header = ttk.Frame(self, relief="raised", borderwidth=5)
        header.grid(row=0, column=0, sticky="nsew")

        body = ttk.Frame(self, relief="sunken", borderwidth=5)
        body.grid(row=0, column=0, sticky="nsew")
        
        control = ttk.Frame(self, relief="raised", borderwidth=5)
        control.grid(row=0, column=0, sticky="nsew")

        label = ttk.Label(header, text="Page Two!!!", font=LARGE_FONT)
        label.grid()

        button1 = ttk.Button(control, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(control, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.grid(row=0, column=1)
        


app = App()
app.mainloop()