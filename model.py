from pynput import mouse as mouse

import numpy as np

import pyautogui as pag

import time as time

import os as os
import csv as csv

from scipy.ndimage import convolve




class Model: 
    
    def __init__(self):
        
        self.dictUserInformation = {
            "info_1":    {"name" : "Name Datensatz:",   "value" : ""},
            "info_2":    {"name" : "Starke Hand:",      "value" : ""},
            "info_3":    {"name" : "Alter:",            "value" : 0},
            "info_4":    {"name" : "Geschlecht:",       "value" : ""},
        }

        
        
        self.dataMovement   = np.zeros(shape=(0,3)) # Achtung, erster Eintrag ist leer!
        self.dataClicks     = np.zeros(shape=(0,3))
        


    def on_mouseMove(self, x, y):
            if (x >= 0 and x < pag.size()[0]) and (y >=0 and y < pag.size()[1]):
                print('Maus bewegt zu {0}'.format((x, y)))
                
                self.dataMovement = np.vstack([self.dataMovement, [x, y, time.time()-self.starttime]])      # type: ignore
              
                
        
    def on_mouseClick(self, x, y, button, pressed):
       
        if str(button) == 'Button.left' and pressed:
            if (x >= 0 and x < pag.size()[0]) and (y >=0 and y < pag.size()[1]):
                
                print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
                print('{0}, {1} at {2}'.format(button, 'Pressed' if pressed else 'Released', (x, y)))

                self.dataClicks = np.vstack([self.dataClicks, [x, y, time.time()-self.starttime]])  # type: ignore
               


    def start_tracking(self):
        self.listener = mouse.Listener(on_move=self.on_mouseMove, on_click=self.on_mouseClick)
        self.listener.start()
        self.dataMovement   = np.zeros(shape=(0,3)) # Achtung, erster Eintrag ist leer!
        self.dataClicks     = np.zeros(shape=(0,3))
        self.starttime      = time.time() #evtl. auch in startTracking 
        
        pag.screenshot("backgroundHeatmap.png")  # type: ignore

    
    def stop_tracking(self):
        self.listener.stop()
        # self.save_DataToCSV(self.dataMovement, self.dictUserInformation["info_1"]["value"], type_ofData="move")
        # self.save_DataToCSV(self.dataClicks, self.dictUserInformation["info_1"]["value"], type_ofData="click")
        
    def update_dict(self, entries):
        print(pag.size()[1])
        print(pag.size()[0])
        for index, key in enumerate (self.dictUserInformation):
            self.dictUserInformation[key]["value"] = entries[index]


    def save_dataToCSV(self, data, nameDataset, type_ofData):
        nameDataset = nameDataset + "_" + type_ofData + ".csv"
        with open(os.path.expanduser(nameDataset), 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    for line in data:
                        writer.writerow(line)

    
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

    
        
        
        #Bearbeitung der Heatmap, damit umliegende Pixel auch eingefärbt werden, damit Pixel auf Hintergrund
        #sichtbar sein werden
        #gauss, mittelwert, media, .... 

        # gauss_filter = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) #/ 16

        return filtered_heatmap
