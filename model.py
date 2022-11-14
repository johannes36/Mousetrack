from pynput import mouse as mouse

import numpy as np

import pyautogui as pag

import time as time

import os as os
import csv as csv



class Model:
    def __init__(self):
        self.dataMovement   = np.zeros(shape=(0,3)) # Achtung, erster Eintrag ist leer!
        self.dataClicks     = np.zeros(shape=(0,3))
        self.starttime      = time.time() #evtl. auch in startTracking 
        
        # @property
        # def nameDataset(self):
        #     return self._nameDataset

        # @nameDataset.setter
        # def nameDataset(self, value):


    def on_MouseMove(self, x, y):
            if (x >= 0 and x < pag.size()[1]) and (y >=0 and y < pag.size()[0]):
                print('Maus bewegt zu {0}'.format((x, y)))
                
                self.dataMovement = np.vstack([self.dataMovement, [x, y, time.time()-self.starttime]])
                
        
    def on_MouseClick(self, x, y, button, pressed):
       
        if str(button) == 'Button.left' and pressed:
            if (x >= 0 and x < pag.size()[1]) and (y >=0 and y < pag.size()[0]):
                
                print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
                print('{0}, {1} at {2}'.format(button, 'Pressed' if pressed else 'Released', (x, y)))

                self.dataClicks = np.vstack([self.dataClicks, [x, y, time.time()-self.starttime]])
               


    def start_Tracking(self):
        self.listener = mouse.Listener(on_move=self.on_MouseMove, on_click=self.on_MouseClick)
        self.listener.start()
    
    def stop_Tracking(self):
        self.listener.stop()

    def save_DataToCSV(self, data, nameDataset):
        nameDataset = nameDataset + ".csv"
        with open(os.path.expanduser(nameDataset), 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    for line in data:
                        writer.writerow(line)

    