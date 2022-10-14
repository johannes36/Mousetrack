import tkinter as tk
from tkinter import ttk

import time as time

from pynput import mouse as mouse

import numpy as np

import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

import seaborn as sns

import csv as csv
import os as os

LARGE_FONT= ("Verdana", 12)


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        self.data_info = {
            "info_1":    {"name" : "Name Datensatz:",   "value" : tk.StringVar()},
            "info_2":    {"name" : "Starke Hand:",      "value" : tk.StringVar()},
            "info_3":    {"name" : "Alter:",            "value" : tk.IntVar()},
            "info_4":    {"name" : "Technikaffinität:", "value" : tk.IntVar()},
            "info_5":    {"name" : "Geschlecht:",       "value" : tk.StringVar()},
            }
        self.entries_info = [tk.StringVar(), tk.StringVar(), tk.IntVar(), tk.IntVar(), tk.StringVar()]

        self.data_setting = {
            "setting_1": {"name" : "Geschwindigkeit",  "value" : tk.BooleanVar()},
            "setting_2": {"name" : "Beschleunigung",   "value" : tk.BooleanVar()},
            "setting_3": {"name" : "Speichern",        "value" : tk.BooleanVar()},
            "setting_4": {"name" : "Heatmap",          "value" : tk.BooleanVar()}
        }
        self.entries_setting = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]
        
        #zum Anzeigen der spezifischen Heatmap 
        self.data_visualize = {
            "visualize_1": {"name" : "Positionsdaten",      "value" : tk.BooleanVar()},
            "visualize_2": {"name" : "Geschwindigkeit",     "value" : tk.BooleanVar()},
            "visualize_3": {"name" : "Beschleunigung",      "value" : tk.BooleanVar()},
            "visualize_4": {"name" : "Flips (coming soon)", "value" : tk.BooleanVar()},              

        }
        self.entries_visualize = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]
        #besseren Namen finden


        self.data_export = {
            "export_1": {"name" : "Positionsdaten",            "value" : tk.BooleanVar()},
            "export_2": {"name" : "Geschwindigkeitsdaten",     "value" : tk.BooleanVar()},
            "export_3": {"name" : "Beschleunigungsdaten",      "value" : tk.BooleanVar()},
            "export_4": {"name" : "Flips (coming soon)",       "value" : tk.BooleanVar()},              

        }

        self.entries_export = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]


        # self.tracking = False

        #-----window geometry
        self.title("Mousetrack")
                
        # window_width  = 500
        # window_height = 500

        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()

        # center_x = int(screen_width/2 - window_width / 2)
        # center_y = int(screen_height/2 - window_height / 2)

        # self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        #-------Lists to track behaviour
        #---make them private??
        self.move_x      = []
        self.move_y      = []
        self.click_x     = [] 
        self.click_y     = []
        self.velo_x      = []
        self.velo_y      = []
        self.acc_x       = []  
        self.acc_y       = []  
        self.time_move   = [] 
        self.time_click  = []
        self.random_heatmap = np.random.randint(low=0, high=200, size=(200, 250))        
        

        #---container, evtl. header, ... hier hinzufügen
        container = tk.Frame(self, borderwidth=10, relief="sunken")
        container.grid(sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)


        
        # self.heatmap_move = np.empty()
        # self.heatmap_click = np.empty()


        self.listener = mouse.Listener(on_move=self.on_move, on_click=self.on_click)
        self.mainloop()
    
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
    

    def on_move(self, x, y):

        print('Maus bewegt zu {0}'.format((x, y)))
        self.move_x.append(x)
        self.move_y.append(y)
        self.time_move.append(time.time() - self.starttime)

    def on_click(self, x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        print('{0}, {1} at {2}'.format(button, 'Pressed' if pressed else 'Released', (x, y)))

        #nur left klicks, keine release sind interessant
        if str(button) == 'Button.left' and pressed:
            self.click_x.append(x)
            self.click_y.append(y)
            self.time_click.append(time.time()- self.starttime)

    def start_tracking(self):
        self.listener.start()
        self.starttime = time.time()
        # self.tracking = True

    def stop_tracking(self):
        self.listener.stop()
        # self.tracking = False

        self.finish_dict()

        #Berechnungen weiter unten ausführen, z.b Klasse 5????    
        self.velo_x, self.velo_y = self.calculate_differentiation(self.move_x, self.move_y, self.time_move)
        self.acc_x, self.acc_y   = self.calculate_differentiation(self.velo_x, self.velo_y, self.time_move)

        self.heatmap_move  = self.calculate_heatmap(self.move_x, self.move_y)
        self.heatmap_click = self.calculate_heatmap(self.click_x, self.click_y)

        # self.plot_heatmap(self.heatmap_move, name="Heatmap Movement")
        # self.plot_heatmap(self.heatmap_click, name="Heatmap Clicks")

        # print("Velo x:" + str(self.velo_x))
        # print("Velo y:" + str(self.velo_y))
        # print("Acc x:" + str(self.acc_x))
        # print("Acc y:" + str(self.acc_y))
        
        # print(self.move_x)
        # print(self.move_y)
        # print(self.time_move)


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

        # print("Geschwindigkeit x:" + str(diff_x))
        # print("Geschwindigkeit y:" + str(diff_y))

        return diff_x, diff_y

    def calculate_heatmap(self, x_Data, y_Data):

        heatmap = np.zeros(shape=(max(y_Data), max(x_Data)))
        # print(len(x_Data))
        # print(type(heatmap))
        # print(np.shape(heatmap))

        for i in range(len(x_Data)):
            heatmap[y_Data[i] - 1, x_Data[i] - 1] = heatmap[y_Data[i] - 1, x_Data[i] - 1] + 1

        # print(np.max(np.max(heatmap)))

        return heatmap 


    
    def finish_dict(self):
        #write all data that wants to be saved to a dict
        for key in self.data_setting:
            if self.data_setting[key]["value"]:
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
        self.quit()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        #Different sections of page
        header = ttk.Frame(self, relief="raised", borderwidth=5)
        header.grid(row=0, column=0, sticky="nsew")

        body = ttk.Frame(self, relief="sunken", borderwidth=5)
        body.grid(row=1, column=0, sticky="nsew")
        
        control = ttk.Frame(self, relief="raised", borderwidth=5)
        control.grid(row=2, column=0, sticky="nsew")


        #content of different section
        # ------- Header
        label_header = ttk.Label(header, text="Startseite der Anwendung Mousetrack", font=LARGE_FONT)
        label_header.grid()

        #----------body statt label tk.Text??!!
        label_body = ttk.Label(body, text="Hier könnte ein Informationstext für Anwender stehen")
        label_body.grid()

        # -----------Control
        ttk.Label(control, text="Dies ist der Kontrollbereich").grid(row=0, column=0)

        ttk.Button(control, text="nächste Seite",
                            command=lambda: controller.show_frame(PageOne)).grid(row=1, column=0)

        ttk.Button(control, text="Seite 2",
                            command=lambda: controller.show_frame(PageTwo)).grid(row=1, column=1)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #Different sections of page

        header = ttk.Frame(self, relief="raised", borderwidth=5)
        header.grid(row=0, column=0, sticky="nsew")

        body = ttk.Frame(self, relief="sunken", borderwidth=5)
        body.grid(row=1, column=0, sticky="nsew")
        
        control = ttk.Frame(self, relief="raised", borderwidth=5)
        control.grid(row=2, column=0, sticky="nsew")

        #-------Header
        ttk.Label(header, text="Seite 1: Informationsabfrage", font=LARGE_FONT).grid()

        #--------Body
        for row_index, key in enumerate(controller.data_info):
            # print(key)
            # print(controller.data_info[key])
            # print(controller.data_info[key]["name"])
            ttk.Label(body, text=controller.data_info[key]["name"]).grid(row=row_index, column=0, sticky="w")

        #   Eingabefelder Body
        #-----1------Entry Name Datensatz
        #------ wie adressierer ich dictionary, bzw. speichere Wert ab?
        ttk.Entry(body, textvariable=controller.entries_info[0]).grid(row=0, column=1)

        #-----2------Radiobutton starke Hand
        ttk.Radiobutton(body, text='links', variable=controller.entries_info[1], value='left').grid(row=1, column=1)
        ttk.Radiobutton(body, text='rechts', variable=controller.entries_info[1], value='rechts').grid(row=1, column=2)

        #-----3------Alter, eingabe über Combobox und liste von 20 bis 30 ------> alternative Lösung suchen(0-100 sind zu viele Werte)
        ttk.Entry(body, textvariable=controller.entries_info[2]).grid(row=2, column=1)
        ttk.Label(body, text="(Eingabe muss Ganzzahl sein(z.B. 23))").grid(row=2, column=2)

        #-----4------
        ttk.Radiobutton(body, text='1', variable=controller.entries_info[3], value=1).grid(row=3, column=1)
        ttk.Radiobutton(body, text='2', variable=controller.entries_info[3], value=2).grid(row=3, column=2)
        ttk.Radiobutton(body, text='3', variable=controller.entries_info[3], value=3).grid(row=3, column=3)

        #-----5------
        ttk.Radiobutton(body, text="männlich", variable=controller.entries_info[4], value="maennlich").grid(row=4, column=1)
        ttk.Radiobutton(body, text="weiblich", variable=controller.entries_info[4], value="weiblich").grid(row=4, column=2)
        ttk.Radiobutton(body, text="divers", variable=controller.entries_info[4], value="divers").grid(row=4, column=3)

        #-------Control #Buttoon zur Bestätigung? ---> Drücken übergibt werte an dict? bei next button press übergabe der Werte?
        button1 = ttk.Button(control, text="zurück zu Start",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(control, text="nächste Seite",
                            command=lambda: [controller.show_frame(PageTwo), controller.update_dict(controller.data_info, controller.entries_info)])
        button2.grid(row=0, column=1, sticky="e")

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        header = ttk.Frame(self, relief="raised", borderwidth=5)
        header.grid(row=0, column=0, sticky="nsew")

        body = ttk.Frame(self, relief="sunken", borderwidth=5)
        body.grid(row=1, column=0, sticky="nsew")
        
        control = ttk.Frame(self, relief="raised", borderwidth=5)
        control.grid(row=2, column=0, sticky="nsew")

        #----------Header
        ttk.Label(header, text="Seite 2: Einstellungen", font=LARGE_FONT).grid()

        #----------Body
        ttk.Label(body, text="gewünschte Optionen auswählen:").grid(row=0, column=0)
        for index, key in enumerate(controller.data_setting):
            # print(controller.data_setting[key]["name"])
            # print(index)
            ttk.Checkbutton(body, text=controller.data_setting[key]["name"],
                            variable= controller.entries_setting[index],
                            onvalue=True, offvalue=False).grid(row=index+1, column=0, sticky="w")       #schöner: variable= controller.data_setting[key]["value"],
        
        #----Entry

        # ttk.Checkbutton(body, text="Tracken?").grid(row=0, column=1)#, text='links', variable=controller.entries_setting[1], value='left').grid(row=1, column=1)
        # ttk.Checkbutton(body, text='rechts', variable=controller.entries_setting[1], value='rechts').grid(row=1, column=2)

        #----------Controls
        button1 = ttk.Button(control, text="vorherige Seite",
                            command=lambda: controller.show_frame(PageOne))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(control, text="Anwendung starten",
                            command=lambda: [controller.show_frame(PageThree), controller.update_dict(controller.data_setting, controller.entries_setting),  controller.start_tracking()])
        button2.grid(row=0, column=1)
        
class PageThree(tk.Frame):
    #3te Seite, die das Livemenü darstellen soll
    #evtl. simple Dinge live anzeigen
    #ansonsten einfach nur simple Optionen (Start oder Stopp)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
       
        header = ttk.Frame(self, relief="raised", borderwidth=5)
        header.grid(row=0, column=0, sticky="nsew")
                
        control = ttk.Frame(self, relief="raised", borderwidth=5)
        control.grid(row=1, column=0, sticky="nsew")

        #-------Header
        ttk.Label(header, text="Seite 3, Livemenü").grid()


        #-------Control
        button1 = ttk.Button(control, text="Anwendung pausieren")#,
                            #command=lambda: controller.show_frame(PageThree))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(control, text="Tracking stoppen und  zu Auswertung",
                            command=lambda: [controller.show_frame(PageFour), controller.stop_tracking()])
        button2.grid(row=0, column=1)

class PageFour(tk.Frame):
    def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            
            header = ttk.Frame(self, relief="raised", borderwidth=5)
            header.grid(row=0, column=0, sticky="nsew")

            body = ttk.Frame(self, relief="sunken", borderwidth=5)
            body.grid(row=1, column=0, sticky="nsew")
            
            control = ttk.Frame(self, relief="raised", borderwidth=5)
            control.grid(row=2, column=0, sticky="nsew")

            #----------Header
            ttk.Label(header, text="Seite 4: Auswahlseite", font=LARGE_FONT).grid()

            #------body
            ttk.Label(body, text="Welche Inhalte sollen als Heatmap angezeigt werden?").grid(row=0, column=0)

            for index, key in enumerate(controller.data_visualize):
                ttk.Checkbutton(body, text=controller.data_visualize[key]["name"],
                                variable= controller.entries_visualize[index],
                                onvalue=True, offvalue=False).grid(row=index+1, column=0, sticky="w")

            
            ttk.Label(body, text="Welche Daten sollen als CSV-File exportiert werden?").grid(row=len(controller.entries_visualize)+1, column=0)
        
                    
            for index, key in enumerate(controller.data_export):
                ttk.Checkbutton(body, text=controller.data_export[key]["name"],
                                variable= controller.entries_export[index],
                                onvalue=True, offvalue=False).grid(row=index+len(controller.entries_visualize)+2, column=0, sticky="w")

            
            #-------Control
            button1 = ttk.Button(control, text="zur nächsten Seite", command=lambda: [
                                controller.show_frame(PageFive),
                                controller.update_dict(controller.data_visualize, controller.entries_visualize), 
                                controller.update_dict(controller.data_export, controller.entries_export)
                                ])
            button1.grid(row=0, column=0)

class PageFive(tk.Frame):
    #5te Seite des Gui, die der Darstellung der Informationen dienen soll
    #Graph Page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        header = ttk.Frame(self, relief="raised", borderwidth=5)
        header.grid(row=0, column=0, sticky="nsew")

        body = ttk.Frame(self, relief="sunken", borderwidth=5)
        body.grid(row=1, column=0, sticky="nsew")
        
        control = ttk.Frame(self, relief="raised", borderwidth=5)
        control.grid(row=2, column=0, sticky="nsew")

        #----------Header
        ttk.Label(header, text="Seite 5: Darstellung der Inhalte", font=LARGE_FONT).grid()

        #-------PLOTTING AREA-------------------
        #creating a figure
        fig = plt.figure()
        #adding an axes object
        ax = fig.add_subplot() 
        ax.set_title("Heatmap aus Zufallszahlen")
        #plotting der Heatmap
        ax.imshow(controller.random_heatmap, cmap='hot', interpolation='nearest') #, cmap='gray')
        
        #-------TKINTER AREA ---------creating a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=body)
        canvas.draw()
        #canvas in body platzieren
        canvas.get_tk_widget().pack()
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, body)
        toolbar.update()            
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack
       
        # ttk.Button(body, text="Zeige Heatmap der Mauspostion", command= lambda:
        #                     self.show_heatmap(controller.heatmap_move, parent=canvas_parent, name="Heatmap Mausposition", figure=fig)).grid(row=1, column=0)
        # ttk.Button(body, text="Zeige Heatmap der Mausklicks", command= lambda:
        #                     self.show_heatmap(controller.heatmap_click, parent=canvas_parent, name="Heatmap Klickposition")).grid(row=1, column=1)



                #----------control
        button1 = ttk.Button(control, text="zurück zur Startseite",
                            command=lambda: controller.show_frame(StartPage)) #commmand für neuen Thread, Datenspeicherung, neuer Datensatz (----> Programmende!!)
        button1.grid(row=0, column=0)

        button2 = ttk.Button(control, text="nächstes Diagramm",
                            command=lambda: self.showHeatmap(axes=ax, parent_canvas=canvas, map=controller.heatmap_move, title="Heatmap Moves"))
        button2.grid(row=0, column=1)
        
        button3 = ttk.Button(control, text="Anwendung schließen",
                            command=lambda: [controller.finishApp()])#, controller.writeCSVFile()])
        button3.grid(row=0, column=2)


    # def clear_plot(self, canvas, parent):         
    #     if canvas:
    #         canvas.get_tk_widget().destroy()
    #         # canvas.winfo_children()[0].destroy()
    #         # for child in parent.winfo_children():
    #         #     child.destroy()
            

    def showHeatmap(self, axes, parent_canvas, map, title):
        axes.clear()
        axes.set_title(title)
        axes.imshow(map, cmap='hot', interpolation='nearest')
        parent_canvas.draw()
        parent_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

app = App()
