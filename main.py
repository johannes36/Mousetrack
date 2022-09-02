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

move_x = []   #Liste der Mauspositionen
move_y = []
click_x = []  #Lister der Klickpositionen
click_y = []
time_move = [] #Liste der Zeitpunkte der Bewegungen
time_click = [] #Liste der Zeitpunkte der Klicks


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


    #Daten in Heatmaps darstellen
    #Häufigkeit des Auftreffen eines Positionspaars muss ermittelt werden
    #np.array mit Index als Position (x, y) und Häufgkeit des Auftreffen dieser Position
    
    # print("move_x:" + str(move_x))
    # print(type(move_x))
    # print(np.shape(move_x))

    #sortieren der movement listen
    #evtl. datenspeicerung to csv vorschieben um Variablen zu sparen
    move_x_sort = np.sort(move_x)
    move_y_sort = np.sort(move_y)

    # print("move_x_sort nach Initialisierung:" + str(move_x_sort))
    # print(type(move_x_sort))
    # print(np.shape(move_x_sort))
    # print("Länge von move_x_sort:" + str(len(move_x_sort)))


    # print("maximmum Pixel in x Richtung: " + str(max(move_x_sort)))
    # print("maximmum Pixel in x Richtung: " + str(max(move_x)))
    

    heat_move = np.zeros(shape=(max(move_x_sort), max(move_y_sort)))
    
    print("heat_move nach Initialisierung:" + str(heat_move))
    print(type(heat_move))
    print(np.shape(heat_move))

    for i in range(len(move_x_sort)): #Pixel in x-Richtung/ schönere Methode überlegen um Pixel des Bildschirm zu bekommen        
        for j in range(len(move_y_sort)):
            #Bedingung für letzten Schhleifendurchlauf (move[x + 1] existiert nicht!)
            # if i == len(move_x_sort) - 1 and j == len(move_y_sort) - 1:
            if i == len(move_x_sort) - 1:# and j == len(move_y_sort) - 1:
   
                print("letzter Schleifendurchlauf bei: i= " + str(i) + "j=" + str(j))
                break
            
            # elif i == len(move_x_sort) - 1 or j == len(move_y_sort) - 1:      
            elif j == len(move_y_sort) - 1:      

                #print("out of range Schleifendurchlauf bei: i= " + str(i) + "j=" + str(j))
                continue
            
            else:
                #wenn vorherige Position gleich aktueller Position
                
                pixel_x = move_x_sort[i] - 1
                pixel_y = move_y_sort[j] - 1

                #print("aktueller Schleifendurchlauf bei: i= " + str(i) + "j=" + str(j))
                #print("aktueller x-Pixel:", pixel_x)
                #print("aktueller y-Pixel:", pixel_y)

                if move_x_sort[i] == move_x_sort[i+1] and move_y_sort[j] == move_y_sort[j+1]:
                    heat_move[pixel_x, pixel_y] = heat_move[pixel_x, pixel_y] + 1


    print(np.shape(heat_move))
    #Heatmap plotten
    # seaborn.heatmap(heat_move)
    

    
    #Bewegungsdaten und Klicks mit Zeitpunkten in File speichern
    with open("move.csv", "w") as file1:
        for pos in move_x, move_y, time_move:
            file1.writelines(str(pos) + '\n')
    
    with open("click.csv", "w") as file2:
        for pos in click_x, click_y, time_click:
            file2.writelines(str(pos) + '\n')

    # with open("heatmap_move.csv", "w") as file3:
    #     for pos in heat_move:
    #         file3.writelines(str(pos) + '\n')
    pd.DataFrame(heat_move).to_csv("heatmap_move.csv")




app = tk.Tk()
app.title("Mousetrack")

wholePage = tk.Frame(app).grid()

label1 = tk.Label(wholePage, text="Input 1:").grid(row=0, column=0, rowspan=2, columnspan=4)
label2 = tk.Label(wholePage, text="Check 1:").grid(row=2, column=0, rowspan=2, columnspan=4)

# start only once callable, for new start, new thread has to be started
button_Start = ttk.Button(wholePage, text="Starte Anwendung", command=lambda: StartPositionTrack()).grid(row=4, column=0)  # hier später timer starten
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

       

    # if os.path.exists("demo.txt"):
    #     #kreiere eine neue Datei, mit anderer Endung
    #     os.remove("demo.txt")
    #     file = open("demo.txt", "w")
    # else:
    #     file = open("demo.txt", "x")
        