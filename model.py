from pynput import mouse as mouse

import numpy as np

import pyautogui as pag

import time as time

import os as os
import csv as csv



class Model: 
    
    def __init__(self):
        
        self.dictUserInformation = {
            "info_1":    {"name" : "Name Datensatz:",   "value" : "" },
            "info_2":    {"name" : "Starke Hand:",      "value" : ""},
            "info_3":    {"name" : "Alter:",            "value" : 0},
            "info_4":    {"name" : "Geschlecht:",       "value" : ""},
        }

        
        
        self.dataMovement   = np.zeros(shape=(0,3)) # Achtung, erster Eintrag ist leer!
        self.dataClicks     = np.zeros(shape=(0,3))
        self.starttime      = time.time() #evtl. auch in startTracking 


    def on_MouseMove(self, x, y):
            if (x >= 0 and x < pag.size()[0]) and (y >=0 and y < pag.size()[1]):
                print('Maus bewegt zu {0}'.format((x, y)))
                
                self.dataMovement = np.vstack([self.dataMovement, [x, y, time.time()-self.starttime]])
                
        
    def on_MouseClick(self, x, y, button, pressed):
       
        if str(button) == 'Button.left' and pressed:
            if (x >= 0 and x < pag.size()[0]) and (y >=0 and y < pag.size()[1]):
                
                print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
                print('{0}, {1} at {2}'.format(button, 'Pressed' if pressed else 'Released', (x, y)))

                self.dataClicks = np.vstack([self.dataClicks, [x, y, time.time()-self.starttime]])
               


    def start_Tracking(self):
        self.listener = mouse.Listener(on_move=self.on_MouseMove, on_click=self.on_MouseClick)
        self.listener.start()
        pag.screenshot("backgroundHeatmap.png")  # type: ignore

    
    def stop_Tracking(self):
        self.listener.stop()
        # self.save_DataToCSV(self.dataMovement, self.dictUserInformation["info_1"]["value"], type_ofData="move")
        # self.save_DataToCSV(self.dataClicks, self.dictUserInformation["info_1"]["value"], type_ofData="click")
        
    def update_dict(self, entries):
        print(pag.size()[1])
        print(pag.size()[0])
        for index, key in enumerate (self.dictUserInformation):
            self.dictUserInformation[key]["value"] = entries[index]


    def save_DataToCSV(self, data, nameDataset, type_ofData):
        nameDataset = nameDataset + "_" + type_ofData + ".csv"
        with open(os.path.expanduser(nameDataset), 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    for line in data:
                        writer.writerow(line)

    
    def calculate_heatmap(self, data):
        # heatmap = np.zeros(shape=(max(y_Data), max(x_Data)))
        
        x_Data = data[:,0]
        y_Data = data[:,1]
        heatmap = np.zeros(shape=(pag.size()[1], pag.size()[0]), dtype=int)


        print("x Länge:")
        print(np.max(x_Data))
        print("y Länge:")
        print(np.max(y_Data))
        print("Shape mAp:")
        print(np.shape(heatmap))
        
        
        for i in range(len(x_Data)):
            heatmap[int(x_Data[i]) - 1, int(y_Data[i]) - 1] = heatmap[int(x_Data[i]) - 1, int(y_Data[i]) - 1] + 1
        
        return heatmap
