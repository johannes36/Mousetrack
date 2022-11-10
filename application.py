import tkinter as tk
from tkinter import ttk



import numpy as np

import csv as csv
import os as os


import startpage as StartPage
import pageone as PageOne
import pagetwo as PageTwo
import pagethree as PageThree
import pagefour as PageFour
import pagefive as PageFive

import matplotlib.pyplot as plt

class App(tk.Tk):
# class App(tk.Frame):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)


        #-----------SETTING VARIABLEN
        self.dictUserInformation = {
            "info_1":    {"name" : "Name Datensatz:",   "value" : tk.StringVar()},
            "info_2":    {"name" : "Starke Hand:",      "value" : tk.StringVar()},
            "info_3":    {"name" : "Alter:",            "value" : tk.IntVar()},
            "info_4":    {"name" : "Technikaffinität:", "value" : tk.IntVar()},
            "info_5":    {"name" : "Geschlecht:",       "value" : tk.StringVar()},
        }
        self.entriesUserInformation = [tk.StringVar(), tk.StringVar(), tk.IntVar(), tk.IntVar(), tk.StringVar()]

        self.dictUserSettings = {
            "setting_1": {"name" : "Geschwindigkeit",  "value" : tk.BooleanVar()},
            "setting_2": {"name" : "Beschleunigung",   "value" : tk.BooleanVar()},
            "setting_3": {"name" : "Speichern",        "value" : tk.BooleanVar()},
            "setting_4": {"name" : "Heatmap",          "value" : tk.BooleanVar()}
        }
        self.entriesUserSettings = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]
        
        #zum Anzeigen der spezifischen Heatmap 
        self.data_visualize = {
            "visualize_1": {"name" : "Positionsdaten",      "value" : tk.BooleanVar()},
            "visualize_2": {"name" : "Geschwindigkeit",     "value" : tk.BooleanVar()},
            "visualize_3": {"name" : "Beschleunigung",      "value" : tk.BooleanVar()},
            "visualize_4": {"name" : "Flips (coming soon)", "value" : tk.BooleanVar()},              

        }
        self.entries_visualize = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]
        #besseren Namen finden


        self.dictExportData = {
            "export_1": {"name" : "Positionsdaten",            "value" : tk.BooleanVar()},# "data" : self.move},
            "export_2": {"name" : "Geschwindigkeitsdaten",     "value" : tk.BooleanVar()},
            "export_3": {"name" : "Beschleunigungsdaten",      "value" : tk.BooleanVar()},
            "export_4": {"name" : "Flips (coming soon)",       "value" : tk.BooleanVar()},              

        }

        self.entriesExportData = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]

        self.map_dict = {
            "map_1": {"title" : "Standartheatmap",        "value" : np.empty},
            "map_2": {"title" : "Heatmap Mausposition",   "value" : np.empty},
            "map_3": {"title" : "Heatmap Klickposition",  "value" : np.empty},
            "map_4": {"title" : "Heatmap Geschwindigkeit","value" : np.empty},
            "map_5": {"title" : "Heatmap Beschleunigung", "value" : np.empty},
        }

        #--------------BEHAVIOUR VARIRABLEN
        #-------Lists to track behaviour
        self.move_x      = []
        self.move_y      = []
        self.move        = []
        self.click_x     = [] 
        self.click_y     = []
        self.velo_x      = []
        self.velo_y      = []
        self.acc_x       = []  
        self.acc_y       = []  
        self.time_move   = [] 
        self.time_click  = []
        self.heatmap_names = ["Standartheatmap", "Heatmap Mausposition", "Heatmap Klickposition", "Heatmap Geschwindigkeit", "Heatmap Beschleunigung" ]
        self.heatmap_list = []
        self.standart_background = plt.imread("backgroundHeatmap.png")
        self.random_heatmap = np.random.randint(low=0, high=200, size=(np.shape(self.standart_background)[0], np.shape(self.standart_background)[1]))
        
        print("Form von shape [0]: " + str(np.shape(self.standart_background)[0]))
        print("Form von shape [1]: " + str(np.shape(self.standart_background)[1]))
        print("Form von shape [2]: " + str(np.shape(self.standart_background)[2]))
             


        #-----WINDOW SETTINGS
        #-----window geometry
        self.title("Mousetrack")
        # self.geometry("420x720")        
        # window_width  = 500
        # window_height = 500

        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()

        # center_x = int(screen_width/2 - window_width / 2)
        # center_y = int(screen_height/2 - window_height / 2)

        # self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
    
    
        #---container, evtl. header, ... hier hinzufügen
        container = ttk.Frame(self, borderwidth=10, relief="sunken")
        container.grid(sticky="nsew", pady=20, padx=20)
        # container.pack(fill="both")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):

            frame = F(parent=container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            # frame.pack(fill="both")
        self.showFrame(StartPage)
        
        # self.heatmap_move = np.empty()
        # self.heatmap_click = np.empty()

        self.protocol("WM_DELETE_WINDOW", func=self.finishApp())
        self.mainloop()
    
    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  

    

    def tracking(self, active):
        #Hieraus 2 Funktionen machen -> On Start App und On Stop App?
        
        if active:
            self.listener = mouse.Listener(on_move=self.onMouseMove, on_click=self.onMouseClick)
            self.listener.start()
            self.starttime = time.time()
            print("started")
            
            pag.screenshot("backgroundHeatmap.png")  # type: ignore

        else:
            print("stopped")
            self.listener.stop()
            self.finish_dict()

            #lieber erst in Page5 einlesen?
            # self.new_background = plt.imread("backgroundHeatmap")

            #Berechnungen weiter unten ausführen, z.b Klasse 5????    
            self.velo_x, self.velo_y = self.calculate_differentiation(self.move_x, self.move_y, self.time_move)
            self.acc_x, self.acc_y   = self.calculate_differentiation(self.velo_x, self.velo_y, self.time_move)

            # for key in self.map_dict:
            #     if self.dictUserSettings[key]["value"]:
                
            # self.map_dict["map_1"]["value"]  = np.random.randint(low=0, high=200, size=(200, 250))
            self.map_dict["map_1"]["value"]  = self.random_heatmap
            self.map_dict["map_2"]["value"]  = self.calculate_heatmap(self.move_x, self.move_y)
            self.map_dict["map_3"]["value"]  = self.calculate_heatmap(self.click_x, self.click_y)
            # self.map_dict["map_1"]["value"]  = np.random.randint(low=0, high=200, size=(200, 250))
            # self.map_dict["map_1"]["value"]  = np.random.randint(low=0, high=200, size=(200, 250))
            # self.map_dict["map_1"]["value"]  = np.random.randint(low=0, high=200, size=(200, 250))


            self.heatmap_move   = self.calculate_heatmap(self.move_x, self.move_y)
            self.heatmap_click  = self.calculate_heatmap(self.click_x, self.click_y)

            print(self.heatmap_move)
            #Heatmap Berechnung für Velo und Acc anpassen
            # self.heatmap_velo   = self.calculate_heatmap(self.velo_x, self.velo_y)
            # self.heatmap_acc   = self.calculate_heatmap(self.acc_x, self.acc_y)
            self.heatmap_list  = [self.random_heatmap, self.heatmap_move, self.heatmap_click]#, self.heatmap_velo, self.heatmap_acc]
            # save_2D_data_with_time(move_x, move_y, time_move, filename= "move.csv")
            # save_2D_data_with_time(click_x, click_y, time_click, filename= "click.csv")

            #[0,0] leer, Lösung finden! Daten anders Speichern z.b.
            # pd.DataFrame(heatmove).to_csv('heatmap_move.csv')
            # pd.DataFrame(heatclick).to_csv('heatmap_move.csv')

            # move_velocity = CalculateVeli(, move_y, time_move)
            #click_velocity = CalculateVeli(x, click_y, time_click)
            # CalculateVelocity(click_x, click_y, time_click)

    def update_dict(self, dict, entries):
        for index, key in enumerate (dict):
            dict[key]["value"] = entries[index].get()
        print(dict)
    
    def calculate_differentiation(self, data_x, data_y, time_event): #acceleration = veränderung von v
        diff_x = [] 
        diff_y = []
        
        for i in range(len(data_x)):

            if i == 0:
                diff_x.append(0)
                diff_y.append(0)

            elif (time_event[i] - time_event[i-1]) == 0:
                diff_x.append(diff_x[i-1])
                diff_y.append(diff_y[i-1])

            else:
                diff_x.append((abs(data_x[i] - data_x[i-1])) / (time_event[i] - time_event[i-1]))
                diff_y.append((abs(data_y[i] - data_y[i-1])) / (time_event[i] - time_event[i-1]))

        return diff_x, diff_y

    def calculate_heatmap(self, x_Data, y_Data):

        # heatmap = np.zeros(shape=(max(y_Data), max(x_Data)))
        heatmap = np.zeros(shape=(np.shape(self.standart_background)[0], np.shape(self.standart_background)[1]))
        print("Form der Heatmap: " + str(np.shape(heatmap)))
        print("Länge des x_Data Vektor: " + str(len(x_Data)))    
        for i in range(len(x_Data)):
            heatmap[y_Data[i] - 1, x_Data[i] - 1] = heatmap[y_Data[i] - 1, x_Data[i] - 1] + 1

        # print(np.max(np.max(heatmap)))

        return heatmap 

    def finish_dict(self):
        #write all data that wants to be saved to a dict
        for key in self.dictUserSettings:
            if self.dictUserSettings[key]["value"]:
                pass

    def save_2D_data_with_time(self, data_x, data_y, time, filename):
        #function to write data in csv file with timepoints
        #data has 3 inputs, x, y and time 
        #daten und Klicks mit Zeitpunkten in File speichern

        # if os.path.exists("demo.txt"):
        #     #kreiere eine neue Datei, mit anderer Endung
        #     os.remove("demo.txt")
        #     file = open("demo.txt", "w")
        # else:
        #     file = open("demo.txt", "x")

        # with open(filename, "w") as file:
        #     for pos in data_x, data_y, time:
        #         file.writelines(str(pos) + '\n')
        pass

    def writeCSVFile(self, filenamePath, lines, delimiter=','):
        with open(os.path.expanduser(filenamePath), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=delimiter)
            for line in lines:
                writer.writerow(line)

    def save_heatmap(self, data, filename):
        # with open(filename, "w") as file:
        #     for x, y in data:
        #         file.writelines(str(x) + '\n')
        #         file.writelines(str(y) + '\n')
        pass
    # def writeCSVFile(filenamePath, lines, delimiter=','):
    #     with open(os.path.expanduser(filenamePath), 'w', newline='') as csvfile:
    #         writer = csv.writer(csvfile, delimiter=delimiter)
    #         for line in lines:
    #             writer.writerow(line)
    def finishApp(self):
        print("finished")
        self.quit()
