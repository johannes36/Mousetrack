import tkinter as tk
from tkinter import ttk
from pynput import mouse
import os


# The callback to call when mouse move events occur
def on_move(x, y):
    print('Maus bewegt zu {0}'.format((x, y)))

    # store Positiondata, später über with statement und Prüfung ob bereits vorhanden
    #f.writelines("{0}".format((x, y)))
    f.write("{0}".format((x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))

    if not pressed:
        return False


def StartPositionTrack():
    # Beginn des Trackings
    listener.start()

    # File zum Daten Spoeichern erzeugen und Prüfung ob File vbereitsw vorhanden

    # Timer starten

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

    # close file


app = tk.Tk()
app.title("Mousetrack")

wholePage = tk.Frame(app).grid()

label1 = tk.Label(wholePage, text="Input 1:").grid(row=0, column=0, rowspan=2, columnspan=4)
label2 = tk.Label(wholePage, text="Check 1:").grid(row=2, column=0, rowspan=2, columnspan=4)

# start only once callable, for new start, new thread has to be started
button_Start = ttk.Button(wholePage, text="Starte Anwendung", command=lambda: StartPositionTrack()).grid(row=4, column=0)  # hier später timer starten
button_Stopp = ttk.Button(wholePage, text="Stopp", command=lambda: listener.stop()).grid(row=4, column=1)

# controller = mouse.Controller()
listener = mouse.Listener(on_move=on_move, on_click=on_click)
# listener.start()
# mouse = mouse.Listener(on_move=on_move)

if os.path.exists("demo.txt"):
    os.remove("demo.txt")
    f = open("demo.txt", "w")
else:
    f = open("demo.txt", "x")


# shortcut to stop imediately


app.mainloop()
