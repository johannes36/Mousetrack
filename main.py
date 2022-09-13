import tkinter as tk
from tkinter import ttk
from pynput import mouse
# import os
# import csv
#from threading import Thread
import time     
import numpy as np
import seaborn 
import matplotlib.pyplot as plt
import pandas as pd


#to install requirements use:
# pip install -r requirements.txt

move_x   = []   #Liste der Mauspositionen
move_y   = []
click_x  = []  #Lister der Klickpositionen
click_y  = []
time_move   = [] #Liste der Zeitpunkte der Bewegungen
time_click  = [] #Liste der Zeitpunkte der Klicks

# The callback to call when mouse move events occur
def on_move(x, y):

    #print('Maus bewegt zu {0}'.format((x, y)))
    # Daten in Liste abspeichern
    move_x.append(x)
    move_y.append(y)
    time_move.append(time.time() - starttime)

#sobald irgendein mouse klick occurs (left, right, ..) wird diese position in Datei geschrieben
#-----> Ausblick: nur Left clicks relevant?
def on_click(x, y, button, pressed):
    #print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    print('{0}, {1} at {2}'.format(button, 'Pressed' if pressed else 'Released', (x, y)))

    #nur left klicks, keine release sind interessant
    if str(button) == 'Button.left' and pressed:
        click_x.append(x)
        click_y.append(y)
        time_click.append(time.time()- starttime)


def StartPositionTrack():
    # Beginn des Trackings
    listener.start()

    # Timer starten
    global starttime
    starttime = time.time()

    # nächste seite anzeigen
def PausePositionTrack():
    # close file when tracking is paused
    pass

def ContinuePositionTrack():
    # file reopen open('a')''
    pass

def StopPositionTrack():
    # mouse Tracking stoppen
    listener.stop()


    #----------
    #Calcualtions, Outputs an creating files
    #just computze, if checkbutton == true
    Save2D_Data_with_Time(move_x, move_y, time_move, filename= "move.csv")
    Save2D_Data_with_Time(click_x, click_y, time_click, filename= "click.csv")

    heatmove = CalculateHeatmap(move_x, move_y, name="Heatmap Movement")
    # heatclick = CalculateHeatmap(click_x, click_y, name="Heatmap Clicks")

    #[0,0] leer, Lösung finden! Daten anders Speichern z.b.
    pd.DataFrame(heatmove).to_csv('heatmap_move.csv')
    # pd.DataFrame(heatclick).to_csv('heatmap_move.csv')

    # move_velocity = CalculateVelocity(move_x, move_y, time_move)
    #click_velocity = CalculateVelocity(click_x, click_y, time_click)
    # CalculateVelocity(move_x, move_y, time_move)
    CalculateVelocity(click_x, click_y, time_click)

def CalculateVelocity(data_x, data_y, time_event): #acceleration = veränderung von v
    velo_x = np.empty(shape=(np.shape(data_x)))
    velo_y = np.empty(shape=(np.shape(data_y)))

    for i in range(len(data_x)):
        if i == 0:
            velo_x[i] = 0
            velo_y[i] = 0
            
        else:
            velo_x[i] = (abs(data_x[i] - data_x[i-1])) / (time_event[i] - time_event[i-1])
            velo_y[i] = (abs(data_y[i] - data_y[i-1])) / (time_event[i] - time_event[i-1])


    # print(velo_x)
    # print(velo_y)
    return velo_x, velo_y

def CalculateAcceleration():
    pass

def CalculateHeatmap(x_Data, y_Data, name):

    heatmap = np.zeros(shape=(max(y_Data), max(x_Data)))
    # print(type(heatmap))
    # print(np.shape(heatmap))

    for i in range(len(x_Data)):
        heatmap[y_Data[i] - 1, x_Data[i] - 1] = heatmap[y_Data[i] - 1, x_Data[i] - 1] + 1

    # print(np.max(np.max(heatmap)))
    # plt.imshow(heatmap) #, cmap='gray')
    # plt.title(name)
    # plt.show()

    return heatmap 

def Save2D_Data_with_Time(data_x, data_y, time, filename):
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

def Save_Heatmap(data, filename):
    with open(filename, "w") as file:
        for x, y in data:
            file.writelines(str(x) + '\n')
            file.writelines(str(y) + '\n')


class App(tk.Tk):
    #init function for class App
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Mousetrack")
        self.iconbitmap() #eigenes Icon

    #-----------geometry of window
        window_width  = 500
        window_height = 500

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    #---------------------------
        
        #window is resizable
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    
    # creating a container
        # s = ttk.Style()
        # s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')

        container = ttk.Frame(self, relief='sunken', width=window_width, height=window_height,  borderwidth=2)#, padding=), style='Danger.TFrame'
        # container.pack(side="top", fill="both", expand=True)
        container.grid(row=0, column=0, padx=window_width-10, pady=window_height-10, sticky='n')


        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {}
        
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
            
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        #frame.reset()
        frame.tkraise()

class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        #init function for class Frame
        ttk.Frame.__init__(self, parent)

        #---------Teil 1 Überschrift---------------------

        headline = ttk.Frame(self, relief="ridge").grid(row=0, column=0)
       
        label1 = ttk.Label(headline, text="Startseite von Mousetrack", relief="ridge").grid()
        # ueberschrift = StringVar
        # text=ueberschrift
        # ueberschrift.set('neue Überschrift')
       
        #---------Teil 2 Body---------------------
        
        body = ttk.Frame(self, relief="raised").grid(row=1, column=0)

        #---------Teil 3 control---------------------
        
        control = ttk.Frame(self, relief="raised").grid(row=2, column=0)
        #buttons to switch between pages
        button1 = ttk.Button(control, text="next", command=lambda : controller.show_frame(Page1)).grid()


class Page1(ttk.Frame):
    def __init__(self, parent, controller):
        #init function for class Frame
        ttk.Frame.__init__(self, parent)

        #---------Teil 1 Überschrift---------------------
        headline = ttk.Frame(self)
        headline.pack(side="top", expand=True, fill="both")

        label1  = ttk.Label(headline, text="Seite 1: Informationen", font=(50))
        label1.grid(row=0, column=0)

        


        #---------Teil 2 Body---------------------
        
        body = ttk.Frame(self)
        body.pack(side="top", expand=True, fill="both")

        #Liste der Labels
        labels_abfrage = [
        "Datensatz Name:",
        "starke Hand:",
        "Alter",
        "Technikaffinität",
        "Geschlecht"
        ]        
        #Label anordnen
        for idx, text in enumerate(labels_abfrage):
            
            # Create a Label widget with the text from the labels list
            label = ttk.Label(body, text=text)

            # Use the grid geometry manager to place the Label widgets in the row whose index is idx
            label.grid(row=idx+1, column=0, sticky='w')


        #Eingabe row 1
        self.name_dataset = tk.StringVar()
        ttk.Entry(body, width=10, textvariable=self.name_dataset).grid(row=1, column=1)
        #self.name_dataset.get() #zur Datenspeicherung

        #Eingabe 2
        #alternativ radiobutton
        self.handvar = tk.StringVar()
        ttk.Radiobutton(body, text='links', variable=self.handvar, value='left').grid(row=2, column=1, sticky="w")

        ttk.Radiobutton(body, text='rechts', variable=self.handvar, value='right').grid(row=2, column=2, sticky="w")

        
        # self.handvar1 = tk.BooleanVar()
        # ttk.Checkbutton(body, text="links", variable=self.handvar1, onvalue=True, offvalue=False).grid(row=2, column=1, sticky="w")
        # self.handvar2 = tk.IntVar()
        # ttk.Checkbutton(body, text="rechts", variable=self.handvar2).grid(row=2, column=2, sticky="w") #onvalue= , offvalue=

        #Eingabe 3

        #Eingabe 4

        #Eingabe 5
        self.checkvar1 = tk.IntVar()
        ttk.Checkbutton(body, text="männlich", variable=self.checkvar1).grid(row=5, column=1, sticky="w")
        self.checkvar2 = tk.IntVar()
        ttk.Checkbutton(body, text="weiblich", variable=self.checkvar2).grid(row=5, column=2, sticky="w")
        self.checkvar3 = tk.IntVar()
        ttk.Checkbutton(body, text="divers", variable=self.checkvar3).grid(row=5, column=3, sticky="w")        



        #---------Teil 3 Controls---------------------

        control = ttk.Frame(self)
        control.pack(side="top", expand=True, fill="both")

        #creating buttons to switch between pages
        #anderer Ansatz:Buttons in oberem Bereich der Seite platzieren, siehe Anika
        button1 = ttk.Button(control, text="next", command=lambda : controller.show_frame(Page2)) #without lambda?
        button1.grid(row=10, column=2)

        button2 = ttk.Button(control, text="back", command=lambda : controller.show_frame(StartPage))
        button2.grid(row=10, column=1)

class Page2(ttk.Frame):
    def __init__(self, parent, controller):
        #init function for class Frame
        ttk.Frame.__init__(self, parent)

        #---------Teil 1 Überschrift---------------------

        headline = ttk.Frame(self)
        headline.pack(side="top", expand=True, fill="both")

        label1  = ttk.Label(headline, text="Seite 2: Einstellungen", font=(50))
        label1.grid(row=0, column=0)


        #---------Teil 2 Body---------------------
        
        body = ttk.Frame(self)
        body.pack(side="top", expand=True, fill="both")

        #Liste der Labels
        labels_einstellungen = [
        "Geschwindigkeit:",
        "Beschleunigung:",
        "Daten in CSV-File speichern",
        "Dauer der Anwendung",
        ]

        for idx, text in enumerate(labels_einstellungen):
            
            # Create a Label widget with the text from the labels list
            label = ttk.Label(body, text=text)

            # Use the grid geometry manager to place the Label widgets in the row whose index is idx
            label.grid(row=idx+1, column=0, sticky='w')

        #---------Teil 3 controls---------------------

        control = ttk.Frame(self)
        control.pack(side="top", expand=True, fill="both")

        #creating buttons to switch between pages
        #anderer Ansatz:Buttons in oberem Bereich der Seite platzieren, siehe Anika
        # start only once callable, for new start, new thread has to be started
        button1 = ttk.Button(control, text="Starte Mousetracking!", command=lambda : StartPositionTrack())
        button1.grid(row=10, column=1)

        button3 = ttk.Button(control, text="Stoppe Tracking", command=lambda : StopPositionTrack())
        button3.grid(row=10, column=2)     

        button2 = ttk.Button(control, text="back", command=lambda : controller.show_frame(Page1))
        button2.grid(row=10, column=3)

   
        




# shortcut to stop imediately 

if __name__ == "__main__":
    
    app = App()

    listener = mouse.Listener(on_move=on_move, on_click=on_click)

    for child in app.winfo_children(): 
           child.grid_configure(padx=5, pady=5)

    app.mainloop()

# root.bind("<Return>", show_frame)

#Aublick
# Version 1.0.6
#     die zuvor hinzugefügten Features werden in ein GUI eingefügt
#         1. Seite 1 zur Informationsabfrage
#         2. Seite 2 zum Vornehmen von Einstellungen und Starten der Anwendung
#         
#         4. Seite 3 nach Ende des Trackings, die die Möglichkeit bietet die getrackten Parameter darzustellen (Heatmap,...) 

        # Zukunft: 
        # 3. Live Seite während des Trackings mit Timer und Stop

       


        