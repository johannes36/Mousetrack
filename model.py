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
        self.starttime      = time.time() 
        
        pag.screenshot("backgroundHeatmap.png")  # type: ignore

    
    def stop_tracking(self):
        self.listener.stop()
        
    def update_dict(self, entries):
        for index, key in enumerate (self.dictUserInformation):
            self.dictUserInformation[key]["value"] = entries[index]


    def save_dataToCSV(self, data, nameDataset, type_ofData):
        nameDataset = nameDataset + "_" + type_ofData + ".csv"
        with open(os.path.expanduser(nameDataset), 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    for line in data:
                        writer.writerow(line)

    
    def calculate_heatmap(self, data):
        
        print("function started")
        x_Data = data[:,1]
        y_Data = data[:,0]
        heatmap = np.zeros(shape=(pag.size()[1], pag.size()[0]), dtype=int)

        for i in range(len(x_Data)):
            
            heatmap[int(x_Data[i]) - 1, int(y_Data[i]) - 1] = heatmap[int(x_Data[i]) - 1, int(y_Data[i]) - 1] + 1
       
        structuring_element = np.array([[1, 1, 1, 1, 1],
                                        [1, 1, 1, 1, 1],
                                        [1, 1, 1, 1, 1],
                                        [1, 1, 1, 1, 1],
                                        [1, 1, 1, 1, 1]])

        filtered_heatmap = convolve(heatmap, structuring_element)
        
        return filtered_heatmap


    def calculate_differentiation(self, data): #acceleration = veränderung von v
        data_x = data[:,1]
        data_y = data[:,0]
        time_event = data[:,2]


        # diff = np.zeros(shape=(0,2))
        diff_x = [] 
        diff_y = []
        
        for i in range(len(data_x)):

            if i == 0:
                # diff = np.vstack([diff, [0, 0]])
                diff_x.append(0)
                diff_y.append(0)

            elif (time_event[i] - time_event[i-1]) == 0:
                # diff = np.vstack([diff, [diff[i-1,:], diff[:,i-1]]])
                diff_x.append(diff_x[i-1])
                diff_y.append(diff_y[i-1])

            else:
                diff_x.append((abs(data_x[i] - data_x[i-1])) / (time_event[i] - time_event[i-1]))
                diff_y.append((abs(data_y[i] - data_y[i-1])) / (time_event[i] - time_event[i-1]))

        return diff_x, diff_y
