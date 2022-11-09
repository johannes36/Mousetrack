from pynput import mouse as mouse

import numpy as np

import pyautogui as pag

import time as time



class Model:
    def __init__(self):
        self.dataMovement   = np.zeros(shape=(0,3)) # Achtung, erster Eintrag ist leer!
        self.dataClicks     = np.zeros(shape=(0,3))
        self.starttime      = time.time() #evtl. auch in startTracking
        

    def start_Tracking(self):
        self.listener = mouse.Listener(on_move=self.on_MouseMove, on_click=self.on_MouseClick)
        self.listener.start()
    
    def stop_Tracking(self):
        self.listener.stop()
        print("Klicks:")
        print(self.dataClicks)
        print("Moves:")
        print(self.dataMovement)
        print("Zeile1:")
        print(self.dataMovement[0])
        print("Moves_x : ")
        print(self.dataMovement[0, 0])
        print("Moves_y : ")
        print(self.dataMovement[0, 1])
        print("Time Move : ")
        print(self.dataMovement[0, 2])


#create new line for new pair of data!
    def on_MouseMove(self, x, y):
        if (x >= 0 and x < pag.size()[1]) and (y >=0 and y < pag.size()[0]):
            print('Maus bewegt zu {0}'.format((x, y)))
            
            self.dataMovement = np.vstack([self.dataMovement, [x, y, time.time()-self.starttime]])
            
        
    def on_MouseClick(self, x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        print('{0}, {1} at {2}'.format(button, 'Pressed' if pressed else 'Released', (x, y)))

        if str(button) == 'Button.left' and pressed:
            if (x >= 0 and x < pag.size()[1]) and (y >=0 and y < pag.size()[0]):

                self.dataClicks = np.vstack([self.dataClicks, [x, y, time.time()-self.starttime]])
               