import tkinter as tk
from tkinter import ttk
from pynput import mouse
# import os
# import csv
#from threading import Thread
import time

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


    #Bewegungsdaten und Klicks mit Zeitpunkten in File speichern
    with open("move.csv", "w") as file1:
        for pos in move_x, move_y, time_move:
            file1.writelines(str(pos) + '\n')
    
    with open("click.csv", "w") as file2:
        for pos in click_x, click_y, time_click:
            file2.writelines(str(pos) + '\n')


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



    # if os.path.exists("demo.txt"):
    #     #kreiere eine neue Datei, mit anderer Endung
    #     os.remove("demo.txt")
    #     file = open("demo.txt", "w")
    # else:
    #     file = open("demo.txt", "x")
        