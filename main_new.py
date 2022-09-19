import tkinter as tk
from tkinter import ttk

import time as time

from pynput import mouse as mouse


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
        self.entries_setting = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]

        #-----window geometry
        self.title("Mousetrack")
                
        # window_width  = 500
        # window_height = 500

        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()

        # center_x = int(screen_width/2 - window_width / 2)
        # center_y = int(screen_height/2 - window_height / 2)

        # self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        

        #---container, evtl. header, ... hier hinzufügen
        container = tk.Frame(self, borderwidth=10, relief="sunken")
        container.grid(sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

        #-------List to track behaviour
        self.move_x   = []
        self.move_y   = []
        self.click_x  = [] 
        self.click_y  = []
        self.time_move   = [] 
        self.time_click  = []

        self.listener = mouse.Listener(on_move=self.on_move, on_click=self.on_click)
    
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
    
    def update_dict(self, dict, entries):

        for index, key in enumerate (dict):
            dict[key]["value"] = entries[index].get()
        print(dict)
    
    def on_move(self, x, y):

        print('Maus bewegt zu {0}'.format((x, y)))
        self.move_x.append(x)
        self.move_y.append(y)
        self.time_move.append(time.time() - self.starttime)

    def on_click(self, x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        print('{0}, {1} at {2}'.format(button, 'Pressed' if pressed else 'Released', (x, y)))

        #nur left klicks, keine release sind interessant
        if str(button) == 'Button.left' and pressed:
            self.click_x.append(x)
            self.click_y.append(y)
            self.time_click.append(time.time()- self.starttime)

    def StartPositionTrack(self):
        self.listener.start()
        self.starttime = time.time()

    def StopPositionTrack(self):
        self.listener.stop()

        # Save2D_Data_with_Time(move_x, move_y, time_move, filename= "move.csv")
        # Save2D_Data_with_Time(click_x, click_y, time_click, filename= "click.csv")

        # heatmove = CalculateHeatmap(move_x, move_y, name="Heatmap Movement")
        # heatclick = CalculateHeatmap(click_x, click_y, name="Heatmap Clicks")

        #[0,0] leer, Lösung finden! Daten anders Speichern z.b.
        # pd.DataFrame(heatmove).to_csv('heatmap_move.csv')
        # pd.DataFrame(heatclick).to_csv('heatmap_move.csv')

        # move_velocity = CalculateVelocity(move_x, move_y, time_move)
        #click_velocity = CalculateVelocity(click_x, click_y, time_click)
        # CalculateVelocity(move_x, move_y, time_move)
        # CalculateVelocity(click_x, click_y, time_click)

    def CalculateVelocity(self, data_x, data_y, time_event): #acceleration = veränderung von v
        # velo_x = np.empty(shape=(np.shape(data_x)))
        # velo_y = np.empty(shape=(np.shape(data_y)))
        pass
        # for i in range(len(data_x)):
        #     if i == 0:
        #         velo_x[i] = 0
        #         velo_y[i] = 0
                
        #     else:
        #         velo_x[i] = (abs(data_x[i] - data_x[i-1])) / (time_event[i] - time_event[i-1])
        #         velo_y[i] = (abs(data_y[i] - data_y[i-1])) / (time_event[i] - time_event[i-1])

        # return velo_x, velo_y

    def CalculateHeatmap(self, x_Data, y_Data, name):
        pass
        # heatmap = np.zeros(shape=(max(y_Data), max(x_Data)))
        # # print(type(heatmap))
        # # print(np.shape(heatmap))

        # for i in range(len(x_Data)):
        #     heatmap[y_Data[i] - 1, x_Data[i] - 1] = heatmap[y_Data[i] - 1, x_Data[i] - 1] + 1

        # # print(np.max(np.max(heatmap)))
        # # plt.imshow(heatmap) #, cmap='gray')
        # # plt.title(name)
        # # plt.show()

        # return heatmap 

    def Save2D_Data_with_Time(self, data_x, data_y, time, filename):
        #function to write data in csv file with timepoints
        #data has 3 inputs, x, y and time 
        #daten und Klicks mit Zeitpunkten in File speichern

            # if os.path.exists("demo.txt"):
        #     #kreiere eine neue Datei, mit anderer Endung
        #     os.remove("demo.txt")
        #     file = open("demo.txt", "w")
        # else:
        #     file = open("demo.txt", "x")

        with open(filename, "w") as file:
            for pos in data_x, data_y, time:
                file.writelines(str(pos) + '\n')

    def Save_Heatmap(self, data, filename):
        with open(filename, "w") as file:
            for x, y in data:
                file.writelines(str(x) + '\n')
                file.writelines(str(y) + '\n')


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
                            command=lambda: [controller.show_frame(PageTwo), controller.update_dict(controller.data_info, controller.entries_info)])
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
        for index, key in enumerate(controller.data_setting):
            print(controller.data_setting[key]["name"])
            print(index)
            ttk.Checkbutton(body, text=controller.data_setting[key]["name"],
                            variable= controller.entries_setting[index],
                            onvalue=True, offvalue=False).grid(row=index+1, column=0, sticky="w")       #schöner: variable= controller.data_setting[key]["value"],
        
        #----Entry

        # ttk.Checkbutton(body, text="Tracken?").grid(row=0, column=1)#, text='links', variable=controller.entries_setting[1], value='left').grid(row=1, column=1)
        # ttk.Checkbutton(body, text='rechts', variable=controller.entries_setting[1], value='rechts').grid(row=1, column=2)

        #----------Controls
        button1 = ttk.Button(control, text="vorherige Seite",
                            command=lambda: controller.show_frame(PageOne))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(control, text="Anwendung starten",
                            command=lambda: [controller.show_frame(PageThree), controller.update_dict(controller.data_setting, controller.entries_setting),  controller.StartPositionTrack()])
        button2.grid(row=0, column=1)
        
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
                            #command=lambda: controller.show_frame(PageThree))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(control, text="Tracking stoppen und  zu Auswertung",
                            command=lambda: [controller.show_frame(PageFour), controller.StopPositionTrack()])
        button2.grid(row=0, column=1)

class PageFour(tk.Frame):
    #4te Seite des Gui, die der Darstellung der Informationen dienen soll

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
        ttk.Label(header, text="Seite 4: Auswertung", font=LARGE_FONT).grid()

        #----------control
        button1 = ttk.Button(control, text="zurück zur Startseite",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(control, text="nächstes Diagramm")#,
                            #command=lambda: [controller.show_frame(StartPage)])
        button2.grid(row=0, column=1)
        
        button3 = ttk.Button(control, text="Anwendung schließen")#,
                            # command=lambda: controller.quit)
        button3.grid(row=0, column=2)


app = App()
app.mainloop()