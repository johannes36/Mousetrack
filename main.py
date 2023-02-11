import tkinter as tk
from tkinter import ttk

import time as time

from pynput import mouse as mouse

import numpy as np

import matplotlib as mpl

mpl.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)  # type: ignore

# from matplotlib.figure import Figure
from matplotlib import cm
from matplotlib.colors import ListedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable


import csv as csv
import os as os

import pyautogui as pag

from scipy.ndimage import convolve

# python -m pip --version
#-TKINTER STYLE CONSTANTS
LARGE_FONT= ("Verdana", 12)


class MainWindow(tk.Tk):
# class App(tk.Frame):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)


        #-----------SETTING VARIABLEN
        self.dictUserInformation = {
            "info_1":    {"name" : "Name Datensatz:",   "value" : tk.StringVar()},
            "info_2":    {"name" : "Starke Hand:",      "value" : tk.StringVar()},
            "info_3":    {"name" : "Alter:",            "value" : tk.IntVar()},
            "info_4":    {"name" : "Geschlecht:",       "value" : tk.StringVar()},
        } #"info_4":    {"name" : "Technikaffinität:", "value" : tk.IntVar()},
        self.entriesUserInformation = [tk.StringVar(), tk.StringVar(), tk.IntVar(), tk.StringVar()]
                                        #tk.IntVar(), 

        """
        self.dictUserSettings = {
            "setting_1": {"name" : "Geschwindigkeit",  "value" : tk.BooleanVar()},
            "setting_2": {"name" : "Beschleunigung",   "value" : tk.BooleanVar()},
            "setting_3": {"name" : "Speichern",        "value" : tk.BooleanVar()},
            "setting_4": {"name" : "Heatmap",          "value" : tk.BooleanVar()}
        }
        self.entriesUserSettings = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]
        """     

        #zum Anzeigen der spezifischen Heatmap 
        self.data_visualize = {
            "visualize_1": {"name" : "Positionsdaten",      "value" : tk.BooleanVar()},
            "visualize_2": {"name" : "Geschwindigkeit",     "value" : tk.BooleanVar()},
            "visualize_3": {"name" : "Beschleunigung",      "value" : tk.BooleanVar()},
            "visualize_4": {"name" : "Flips (coming soon)", "value" : tk.BooleanVar()},              

        }
        self.entries_visualize = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]
        #besseren Namen finden

        """
        self.dictExportData = {
            "export_1": {"name" : "Positionsdaten",            "value" : tk.BooleanVar()},# "data" : self.move},
            "export_2": {"name" : "Geschwindigkeitsdaten",     "value" : tk.BooleanVar()},
            "export_3": {"name" : "Beschleunigungsdaten",      "value" : tk.BooleanVar()},
            "export_4": {"name" : "Flips (coming soon)",       "value" : tk.BooleanVar()},              

        }

        self.entriesExportData = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]
            """
        self.map_dict = {
            "map_1": {"title" : "Standartheatmap",        "value" : np.empty},
            "map_2": {"title" : "Heatmap Mausposition",   "value" : np.empty},
            "map_3": {"title" : "Heatmap Klickposition",  "value" : np.empty},
            "map_4": {"title" : "Heatmap Geschwindigkeit","value" : np.empty},
            "map_5": {"title" : "Heatmap Beschleunigung", "value" : np.empty},
        }

        #--------------BEHAVIOUR VARIRABLEN
        #-------Lists to track behaviour
        self.dataMovement   = np.zeros(shape=(0,3)) # Achtung, erster Eintrag ist leer!
        self.dataClicks     = np.zeros(shape=(0,3))
        
        
        
        
        self.move_x      = []
        self.move_y      = []
        self.click_x     = [] 
        self.click_y     = []
        self.velo_x      = []
        self.velo_y      = []
        self.acc_x       = []  
        self.acc_y       = []  
        self.time_move   = [] 
        self.time_click  = []
        self.heatmap_names = ["Standartheatmap", "Heatmap Mausposition", "Heatmap Klickposition", "Heatmap Geschwindigkeit", "Heatmap Beschleunigung" ]
        self.heatmap_list = []
        self.standart_background = plt.imread("old_backgroundHeatmap.png")
        self.random_heatmap = np.random.randint(low=0, high=50, size=(np.shape(self.standart_background)[0], np.shape(self.standart_background)[1]))
        
        print("Form von shape [0]: " + str(np.shape(self.standart_background)[0]))
        print("Form von shape [1]: " + str(np.shape(self.standart_background)[1]))
        print("Form von shape [2]: " + str(np.shape(self.standart_background)[2]))
             


        #-----WINDOW SETTINGS
        #-----window geometry
        self.title("Mousetrack")
        # self.geometry("420x720")        
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
        container = ttk.Frame(self, borderwidth=10, relief="sunken")
        container.grid(sticky="nsew", pady=20, padx=20)
        # container.pack(fill="both")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):#, PageFour, PageFive):

            frame = F(parent=container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            # frame.pack(fill="both")
        self.showFrame(StartPage)
        
        # self.heatmap_move = np.empty()
        # self.heatmap_click = np.empty()

        self.protocol("WM_DELETE_WINDOW", func=self.finishApp())
        self.mainloop()
    
    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  

    def onMouseMove(self, x, y):
        #negative Werte weglassem
        #nur Pixelpositionen aufnehmen, die Form 1080x1920 erfüllen
        
        if (x >= 0 and x < pag.size()[0]) and (y >=0 and y < pag.size()[1]):
                print('Maus bewegt zu {0}'.format((x, y)))
                
                self.dataMovement = np.vstack([self.dataMovement, [x, y, time.time()-self.starttime]])  # type: ignore


    def onMouseClick(self, x, y, button, pressed):
        if str(button) == 'Button.left' and pressed:
            if (x >= 0 and x < pag.size()[0]) and (y >=0 and y < pag.size()[1]):
                
                print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
                print('{0}, {1} at {2}'.format(button, 'Pressed' if pressed else 'Released', (x, y)))

                self.dataClicks = np.vstack([self.dataClicks, [x, y, time.time()-self.starttime]])  # type: ignore
        
    def start_tracking(self):
        self.listener = mouse.Listener(on_move=self.onMouseMove, on_click=self.onMouseClick)
        self.listener.start()
        
        self.dataMovement   = np.zeros(shape=(0,3)) # Achtung, erster Eintrag ist leer!
        self.dataClicks     = np.zeros(shape=(0,3))
        self.starttime = time.time()

        # self.move_x      = []
        # self.move_y      = []
        # self.click_x     = [] 
        # self.click_y     = []
        # self.velo_x      = []
        # self.velo_y      = []
        # self.acc_x       = []  
        # self.acc_y       = []  
        # self.time_move   = [] 
        # self.time_click  = []
       

        
        pag.screenshot("old_backgroundHeatmap.png")  # type: ignore

    
    def stop_tracking(self):
        self.listener.stop()
        self.velo_x, self.velo_y = self.calculate_differentiation(self.dataMovement)
        self.map_dict["map_1"]["value"]  = self.random_heatmap
        self.map_dict["map_2"]["value"]  = self.calculate_heatmap(self.dataMovement)
        self.map_dict["map_3"]["value"]  = self.calculate_heatmap(self.dataClicks)
           
        self.heatmap_move   = self.calculate_heatmap(self.dataMovement)
        self.heatmap_click  = self.calculate_heatmap(self.dataClicks)

        self.heatmap_list  = [self.random_heatmap, self.heatmap_move, self.heatmap_click]#, self.heatmap_velo, self.heatmap_acc]
                
    
    
    def update_dict(self, dict, entries):
        for index, key in enumerate (dict):
            dict[key]["value"] = entries[index].get()
        print(dict)
    
    def calculate_differentiation(self, data): #acceleration = veränderung von v
        data_x = data[:,1]
        data_y = data[:,0]
        time_event = data[:,2]

        diff_x = [] 
        diff_y = []
        
        for i in range(len(data_x)):

            if i == 0:
                diff_x.append(0)
                diff_y.append(0)

            elif (time_event[i] - time_event[i-1]) == 0:
                diff_x.append(diff_x[i-1])
                diff_y.append(diff_y[i-1])

            else:
                diff_x.append((abs(data_x[i] - data_x[i-1])) / (time_event[i] - time_event[i-1]))
                diff_y.append((abs(data_y[i] - data_y[i-1])) / (time_event[i] - time_event[i-1]))

        return diff_x, diff_y

    def calculate_heatmap(self, data):
        # heatmap = np.zeros(shape=(max(y_Data), max(x_Data)))
        
        print("function started")
        x_Data = data[:,1]
        y_Data = data[:,0]
        heatmap = np.zeros(shape=(pag.size()[1], pag.size()[0]), dtype=int)

        
        print("Zeros erstellt")
        # print("x Länge:")
        # print(np.max(x_Data))
        # print("y Länge:")
        # print(np.max(y_Data))
        # print("Shape mAp:")
        print("erlaubte shape:")
        print(np.shape(heatmap))
        
        print("i sollte sein:")
        print(len(x_Data))
        #Schleife über alle Positionen, die aufgenommen wurden
        for i in range(len(x_Data)):
            
            heatmap[int(x_Data[i]) - 1, int(y_Data[i]) - 1] = heatmap[int(x_Data[i]) - 1, int(y_Data[i]) - 1] + 1
            
        #manipulation der Heatmap mit Methode um umliegende Pixel auch hohe Werte zuzuweisen
        # Gauss Filter?
        gauss_filter = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16

        # Bildbearbeitung mithilfe Dilatation
        #Strukturelement: wie funktioniert convolve genau
        structuring_element = np.array([[1, 1, 1, 1, 1],
                                        [1, 1, 1, 1, 1],
                                        [1, 1, 1, 1, 1],
                                        [1, 1, 1, 1, 1],
                                        [1, 1, 1, 1, 1]])

        filtered_heatmap = convolve(heatmap, structuring_element)

        return filtered_heatmap


    def writeCSVFile(self, filenamePath, lines, delimiter=','):
        with open(os.path.expanduser(filenamePath), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=delimiter)
            for line in lines:
                writer.writerow(line)
    def finishApp(self):
        print("finished")
        self.quit()

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

        header = ttk.Frame(self)#, relief="raised", borderwidth=5)
        header.pack(fill="both", pady=20, padx=20)

        body = ttk.Frame(self)#, relief="sunken", borderwidth=5)
        body.pack(fill="both", pady=20, padx=20)
        
        control = ttk.Frame(self)#, relief="raised", borderwidth=5)
        control.pack(fill="both", pady=20, padx=20)



        #content of different section
        # ------- Header
        label_header = ttk.Label(header, text="Startseite der Anwendung Mousetrack", font=LARGE_FONT)
        label_header.grid()

        #----------body statt label tk.Text??!!
        label_body = ttk.Label(body, text="""Willkommen! 
Diese Anwendung verwendet Mouse-Tracking, um Ihr Nutzerverhalten zu analysieren.
Seite 1 bietet die Möglichkeit, Nutzerinformationen anzugeben. Über diese Seite wird das Tracking gestartet.
Seite 2 wird während des Trackings angezeigt und ermöglicht es, das Tracking zu beenden.
Seite 3 dient der Visualisierung der Ergebnisse.
""")
        label_body.grid()

        # -----------Control
        # ttk.Label(control, text="Dies ist der Kontrollbereich").grid(row=0, column=0)

        ttk.Button(control, text="nächste Seite",
                            command=lambda: controller.showFrame(PageOne)).grid(row=1, column=0)

        # ttk.Button(control, text="Seite 2", command=lambda: controller.showFrame(PageTwo)).grid(row=1, column=1)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #Different sections of page

        header = ttk.Frame(self)#, relief="raised", borderwidth=5)
        header.pack(fill="both", pady=20, padx=20)

        body = ttk.Frame(self)#, relief="sunken", borderwidth=5)
        body.pack(fill="both", pady=20, padx=20)
        
        control = ttk.Frame(self)#, relief="raised", borderwidth=5)
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
        # ttk.Radiobutton(body, text='1', variable=controller.entriesUserInformation[3], value=1).grid(row=3, column=1)
        # ttk.Radiobutton(body, text='2', variable=controller.entriesUserInformation[3], value=2).grid(row=3, column=2)
        # ttk.Radiobutton(body, text='3', variable=controller.entriesUserInformation[3], value=3).grid(row=3, column=3)

        #-----5------
        ttk.Radiobutton(body, text="männlich", variable=controller.entriesUserInformation[3], value="maennlich").grid(row=3, column=1)
        ttk.Radiobutton(body, text="weiblich", variable=controller.entriesUserInformation[3], value="weiblich").grid(row=3, column=2)
        ttk.Radiobutton(body, text="divers", variable=controller.entriesUserInformation[3], value="divers").grid(row=3, column=3)

        #-------Control #Buttoon zur Bestätigung? ---> Drücken übergibt werte an dict? bei next button press übergabe der Werte?
        button1 = ttk.Button(control, text="zurück zu Start",
                            command=lambda: controller.showFrame(StartPage))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(control, text="Tracking starten",
                            command=lambda: [controller.showFrame(PageTwo), controller.update_dict(controller.dictUserInformation, controller.entriesUserInformation), controller.start_tracking()])
        button2.grid(row=0, column=1, sticky="e")

"""
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
"""        

class PageTwo(tk.Frame):
    #3te Seite, die das Livemenü darstellen soll
    #evtl. simple Dinge live anzeigen
    #ansonsten einfach nur simple Optionen (Start oder Stopp)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
       
        header = ttk.Frame(self)#, relief="raised", borderwidth=5)
        header.grid(row=0, column=0, sticky="nsew")
                
        control = ttk.Frame(self)#, relief="raised", borderwidth=5)
        control.grid(row=1, column=0, sticky="nsew")

        #-------Header
        ttk.Label(header, text="Seite 2").grid()


        #-------Control
        button1 = ttk.Button(control, text="Anwendung pausieren")#,
                            #command=lambda: controller.showFrame(PageThree))
        # button1.grid(row=0, column=1)

        button2 = ttk.Button(control, text="Tracking stoppen",
                            command=lambda: [controller.showFrame(PageThree), controller.stop_tracking()])
        button2.grid(row=0, column=0)
"""
class PageFour(tk.Frame):
    def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            
            header = ttk.Frame(self)#, relief="raised", borderwidth=5)
            header.grid(row=0, column=0, sticky="nsew")

            body = ttk.Frame(self)#, relief="sunken", borderwidth=5)
            body.grid(row=1, column=0, sticky="nsew")
            
            control = ttk.Frame(self)#, relief="raised", borderwidth=5)
            control.grid(row=2, column=0, sticky="nsew")

            #----------Header
            ttk.Label(header, text="Seite 3: Auswahlseite", font=LARGE_FONT).grid()

            #------body
            ttk.Label(body, text="Welche Inhalte sollen als Heatmap angezeigt werden?").grid(row=0, column=0)

            for index, key in enumerate(controller.data_visualize):
                ttk.Checkbutton(body, text=controller.data_visualize[key]["name"],
                                variable= controller.entries_visualize[index],
                                onvalue=True, offvalue=False).grid(row=index+1, column=0, sticky="w")

            
            ttk.Label(body, text="Welche Daten sollen als CSV-File exportiert werden?").grid(row=len(controller.entries_visualize)+1, column=0)
        
                    
            for index, key in enumerate(controller.dictExportData):
                ttk.Checkbutton(body, text=controller.dictExportData[key]["name"],
                                variable= controller.entriesExportData[index],
                                onvalue=True, offvalue=False).grid(row=index+len(controller.entries_visualize)+2, column=0, sticky="w")

            
            #-------Control
            button1 = ttk.Button(control, text="zur nächsten Seite", command=lambda: [
                                controller.showFrame(PageFive),
                                controller.update_dict(controller.data_visualize, controller.entries_visualize), 
                                controller.update_dict(controller.dictExportData, controller.entriesExportData)
                                ])
            button1.grid(row=0, column=0)
"""
class PageThree(tk.Frame):
    #5te Seite des Gui, die der Darstellung der Informationen dienen soll
    #Graph Page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        header = ttk.Frame(self)#, relief="raised", borderwidth=5)
        header.grid(row=0, column=0, columnspan=3, sticky="nsew")

        body = ttk.Frame(self)#, relief="sunken", borderwidth=5)
        body.grid(row=1, column=0, columnspan=3, sticky="nsew")
        
        control = ttk.Frame(self)#, relief="raised", borderwidth=5)
        control.grid(row=2, column=0, columnspan=3 ,sticky="nsew")

        #----------Header
        ttk.Label(header, text="Seite 3: Darstellung der Inhalte", font=LARGE_FONT).grid()

        #-------PLOTTING AREA-------------------
        self.background = plt.imread("old_backgroundHeatmap.png")

        colormap = mpl.colormaps['YlOrRd']  # type: ignore
        newcolors = colormap(np.linspace(0.3, 1, 256))
        white = np.array([1, 1, 1, 1])
        newcolors[:25, :] = white
        # cmap = cm.get_cmap("YlOrRd", 100)
        # self.newcmap = ListedColormap(cmap(np.linspace(0, 0.7, 100)))  # type: ignore
        self.newcmap = ListedColormap(newcolors)  # type: ignore
        

        #creating a figure
        fig, ax = plt.subplots()        #adding an axes object
        
        ax.set_title("Heatmap aus Zufallszahlen")
        #plotting der Heatmap/// Enstrpicht heatmap_list[0]
        
        ax.set_aspect("equal")


        ax.imshow(self.background)


        ax.imshow(controller.random_heatmap, cmap='hot' , alpha=0.7)
        
        # divider = make_axes_locatable(ax)
        # cax = divider.append_axes("right", size="5%", pad=0.25)

        # plt.colorbar(cax=cax)

        #shape von Hintergrund und Heatmap müssen übereinstimmen
        #-------TKINTER AREA ---------creating a Tkinter canvas        
        canvas = FigureCanvasTkAgg(fig, master=body)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # NavigationToolbar2Tk hinzufügen
        toolbar = NavigationToolbar2Tk(canvas, body)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # ttk.Button(body, text="Zeige Heatmap der Mauspostion", command= lambda:
        #                     self.show_heatmap(controller.heatmap_move, parent=canvas_parent, name="Heatmap Mausposition", figure=fig)).grid(row=1, column=0)
        # ttk.Button(body, text="Zeige Heatmap der Mausklicks", command= lambda:
        #                     self.show_heatmap(controller.heatmap_click, parent=canvas_parent, name="Heatmap Klickposition")).grid(row=1, column=1)



                #----------control
        button1 = ttk.Button(control, text="zurück zur Startseite",
                            command=lambda: controller.showFrame(StartPage)) #commmand für neuen Thread, Datenspeicherung, neuer Datensatz (----> Programmende!!)
        button1.grid(row=0, column=0)

        self.button2 = ttk.Button(control, text="Heatmaps anzeigen",
                            command=lambda: self.ShowHeatmap(axes=ax, parent_canvas=canvas, value_list=controller.heatmap_list, name_list=controller.heatmap_names, parent_frame=control, controller=self.controller))
        self.button2.grid(row=0, column=1, columnspan=2)
        
        # self.button2 = ttk.Button(control, text="Heatmaps anzeigen",
        #                     command=lambda: self.ShowHeatmap(axes=ax, parent_canvas=canvas, value_list=controller.heatmap_list, name_list=controller.heatmap_names, parent_frame=control, controller=self.controller))
        # self.button2.grid(row=0, column=1, columnspan=2)
        

        button3 = ttk.Button(control, text="Anwendung schließen",
                            command=lambda: [controller.finishApp()])#, controller.writeCSVFile()])
        button3.grid(row=0, column=3)
            

    def ShowHeatmap(self, axes, parent_canvas, value_list, name_list, parent_frame, controller):
        #use image viewer example
        #Alter Ansatz mit dict
        # axes.clear()
        # axes.set_title(dict["map_2"]["title"])
        # axes.imshow(dict["map_2"]["value"], cmap='hot', interpolation='nearest')


        self.background = plt.imread("old_backgroundHeatmap.png")

        axes.clear()
        axes.set_title(name_list[1])
        axes.imshow(self.background)
        axes.imshow(value_list[1], cmap='hot' , alpha=0.7)


        parent_canvas.draw()
        parent_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.button2.grid_forget()

        
        #Code für Image List
        # my_label = tk.Label(image=imagelist[imagenumber])
        # my_label.grid()

        self.button_back = ttk.Button(parent_frame, text="<<", command= lambda:
        self.showPreviousHeatmap(axes=axes, parent_canvas=parent_canvas, parent_frame=parent_frame, value_list=controller.heatmap_list, name_list=controller.heatmap_names, seite=0, controller=controller))
        self.button_back.grid(row=0, column=1)

        self.button_forward = ttk.Button(parent_frame, text=">>", command= lambda:
        self.showNextHeatmap(axes=axes, parent_canvas=parent_canvas, parent_frame=parent_frame, value_list=controller.heatmap_list, name_list=controller.heatmap_names, seite=2, controller=controller))
        self.button_forward.grid(row=0, column=2)



    def showNextHeatmap(self, axes, parent_canvas, parent_frame, value_list, name_list, seite, controller):#, parent_frame, controller):
        #Alter Ansatz mit dict:
        # axes.clear()
        # axes.set_title(dict["map_3"]["title"])
        # axes.imshow(dict["map_3"]["value"], cmap='hot', interpolation='nearest')
        # parent_canvas.draw()
        # parent_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.background = plt.imread("old_backgroundHeatmap.png")

        axes.clear()
        axes.set_title(name_list[seite])
        axes.imshow(self.background)
        axes.imshow(value_list[seite], cmap='hot' , alpha=0.7)


        parent_canvas.draw()
        parent_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.button_back.grid_forget()
        self.button_forward.grid_forget()
        self.button_back    = ttk.Button(parent_frame, text="<<", command= lambda: self.showPreviousHeatmap(axes=axes, parent_canvas=parent_canvas, parent_frame=parent_frame, value_list=controller.heatmap_list, name_list=controller.heatmap_names, seite=seite-1, controller=controller))
        self.button_forward = ttk.Button(parent_frame, text=">>", command= lambda: self.showNextHeatmap(axes=axes, parent_canvas=parent_canvas, parent_frame=parent_frame, value_list=controller.heatmap_list, name_list=controller.heatmap_names, seite=seite+1, controller=controller))
        self.button_back.grid(row=0, column=1)
        self.button_forward.grid(row=0, column=2)
        
        if seite==2:
            print("forward disabled")
            self.button_forward = ttk.Button(parent_frame, text=">>", state='disabled')
            self.button_forward.grid(row=0, column=2)
        
    def showPreviousHeatmap(self, axes, parent_canvas, parent_frame, value_list, name_list, seite, controller):
                
        self.background = plt.imread("old_backgroundHeatmap.png")

        axes.clear()
        axes.set_title(name_list[seite])
        axes.imshow(self.background)
        axes.imshow(value_list[seite], cmap='hot' , alpha=0.7)


        parent_canvas.draw()
        parent_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.button_back.grid_forget()
        self.button_forward.grid_forget()
        self.button_back    = ttk.Button(parent_frame, text="<<", command= lambda: self.showPreviousHeatmap(axes=axes, parent_canvas=parent_canvas, parent_frame=parent_frame, value_list=controller.heatmap_list, name_list=controller.heatmap_names, seite=seite-1, controller=controller))
        self.button_forward = ttk.Button(parent_frame, text=">>", command= lambda: self.showNextHeatmap(axes=axes, parent_canvas=parent_canvas, parent_frame=parent_frame, value_list=controller.heatmap_list, name_list=controller.heatmap_names, seite=seite+1, controller=controller))
        self.button_back.grid(row=0, column=1)
        self.button_forward.grid(row=0, column=2)
               
        if seite==0:
            print("back disabled")
            self.button_back = ttk.Button(parent_frame, text="<<", state='disabled')
            self.button_back.grid(row=0, column=1)
        


app = MainWindow()
# app.geometry()

# if __name__ == "__main__":
#     root = tk.Tk()
#     App(root).pack(side="top", fill="both", expand=True)
#     root.mainloop()