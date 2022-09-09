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

    print('Maus bewegt zu {0}'.format((x, y)))
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

    Save2D_Data_with_Time(move_x, move_y, time_move, filename= "move.csv")
    Save2D_Data_with_Time(click_x, click_y, time_click, filename= "click.csv")

    heatmove = Calculate_Heatmap(move_x, move_y, name="Heatmap Movement")
    # heatclick = Calculate_Heatmap(click_x, click_y, name="Heatmap Clicks")

    #[0,0] leer, Lösung finden! Daten anders Speichern z.b.
    pd.DataFrame(heatmove).to_csv('heatmap_move.csv')
    # pd.DataFrame(heatclick).to_csv('heatmap_move.csv')


    #Save_Heatmap(heatmove, filename="heatmap_move.csv")
    #Save_Heatmap(heatclick, filename="heatmap_click.csv")

def Calculate_Heatmap(x_Data, y_Data, name):

    heatmap = np.zeros(shape=(max(x_Data),max(y_Data)))
    print(type(heatmap))
    print(np.shape(heatmap))

    for x in x_Data:
        for y in y_Data:
            heatmap[x-1, y-1] = heatmap[x-1, y-1] + 1


    plt.imshow(heatmap, cmap='gray')
    plt.title(name)
    plt.show()

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


# def Save    


app = tk.Tk()
app.title("Mousetrack")


wholePage = tk.Frame(app).grid()

label1 = tk.Label(wholePage, text="Input 1:").grid(row=0, column=0, rowspan=2, columnspan=4)
label2 = tk.Label(wholePage, text="Check 1:").grid(row=2, column=0, rowspan=2, columnspan=4)

# start only once callable, for new start, new thread has to be started
button_Start = ttk.Button(wholePage, text="Starte Anwendung", command=lambda: StartPositionTrack()).grid(row=4, column=0)
button_Stopp = ttk.Button(wholePage, text="Stopp", command=lambda: StopPositionTrack()).grid(row=4, column=1)


# controller = mouse.Controller()
listener = mouse.Listener(on_move=on_move, on_click=on_click)


# shortcut to stop imediately 


app.mainloop()


#Aublick
# Version 1.0.5
#     die zuvor hinzugefügten Features werden in ein GUI eingefügt
#         1. Seite 1 zur Informationsabfrage
#         2. Seite 2 zum Vornehmen von Einstellungen und Starten der Anwendung
#         3. Live Seite während des Trackings mit Timer und Stop
#         4. Seite 3 nach Ende des Trackings, die die Möglichkeit bietet die getrackten Parameter darzustellen (Heatmap,...) 

       


        