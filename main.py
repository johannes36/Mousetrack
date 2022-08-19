import tkinter as tk
from tkinter import ttk
from pynput import mouse

app = tk.Tk()
app.title("Mousetrack")

wholePage = tk.Frame(app).grid()

label1 = tk.Label(wholePage, text="Input 1:").grid(row=0, column=0, rowspan=2, columnspan=4)
label2 = tk.Label(wholePage, text="Check 1:").grid(row=2, column=0, rowspan=2, columnspan=4)

button_Start = ttk.Button(wholePage, text="Starte Anwendung", command=lambda : StartPositionTrack()).grid(row=4, column=0)
button_Stopp = ttk.Button(wholePage, text="Stopp", command=lambda : StopPositionTrack()).grid(row=4, column=1)

mouse = mouse.Listener(on_move=on_move)


def on_move(x,y):
    print("Maus bewegt zu Koordinate: {0}".format((x, y)))

def on_click(x, y, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))

    if not pressed:
        return False


def StartPositionTrack():
    #Beginn des Trackings 
    #mousePosition = mouse.postion
    mouse.start()
    print("Aktuelle Position: {0}".format(mouse.position))

    #nächste seite anzeigen 
def PausePositionTrack():
    #close file when tracking is paused
    pass

def ContinuePositionTrack():
    #file reopen open('a')''
    pass

def StopPositionTrack():
    #mouse Tracking stoppen
    mouse.stop()

    #close file
    






#shortcut to stop imediately


app.mainloop()