import tkinter as tk
from tkinter import ttk

import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)  # type: ignore
# from matplotlib import cm
# from matplotlib.figure import Figure
# from matplotlib.colors import ListedColormap
# from mpl_toolkits.axes_grid1 import make_axes_locatable
LARGE_FONT= ("Verdana", 12)

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        
        self.entriesUserInformation = [tk.StringVar(), tk.StringVar(), tk.IntVar(), tk.StringVar()]

        self.page_parent = ttk.Frame(self)
        self.show_startPage()

        #Seite 1 platzieren und Kommandos den buttons hinzufügen
        # self.page1.create_Page(master=self.page_parent)
        # self.bind_commandsToPage(self.page1)


    def show_startPage(self):
        self.page_parent.destroy()
        self.page_parent = ttk.Frame(self, borderwidth=10, relief="sunken")
        self.page_parent.grid(row=0, column=0)
        self.page_parent.rowconfigure(0, weight=1)
        self.page_parent.columnconfigure(0, weight=1)
        
        ttk.Label(master=self.page_parent, text="Startseite", font=LARGE_FONT).grid(row=0, column=0)  
        
        # tk.Label(master=parent_frame, text="Startseite").grid(row=0, column=0)
        ttk.Label(master=self.page_parent, text="""
Willkommen! Diese Anwendung verwendet Mouse-tracking, um Ihr Nutzerverhalten zu analysieren.
Seite 1 dient der Eingabe von Nutzerinformationen. Über diese Seite wird das Tracking gestartet.
Seite 2 wird während des Trackings angezeigt und ermöglicht es, das Tracking zu beenden.
Seite 3 dient der Visualisierung der Ergebnisse.""").grid(row=1, column=0)
            
        ttk.Button(master=self.page_parent, text="Nächste Seite", command= self.show_pageOne).grid(row=2, column=0)

    def show_pageOne(self):
        self.page_parent.destroy()
        self.page_parent = ttk.Frame(self, borderwidth=10, relief="sunken")
        self.page_parent.grid(row=0, column=0)
        self.page_parent.rowconfigure(0, weight=1)
        self.page_parent.columnconfigure(0, weight=1)

        ttk.Label(master=self.page_parent, text="Seite 1: Informationsabfrage", font=LARGE_FONT).grid(row=0, column=1)
        # parent_frame = tk.LabelFrame(master=self.page_parent, text="Seite1")
        # parent_frame.rowconfigure(0, weight=1)
        # parent_frame.columnconfigure(0, weight=1)
        # parent_frame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        labels = ("Name Datensatz:", "Starke Hand:",  "Alter:", "Geschlecht:")

        for row_index, label in enumerate(labels):
            ttk.Label(master=self.page_parent, text=label).grid(row=row_index+1, column=0, sticky="w")



        ttk.Entry(self.page_parent, textvariable=self.entriesUserInformation[0]).grid(row=1, column=1)
        ttk.Radiobutton(self.page_parent, text='links', variable=self.entriesUserInformation[1], value='left').grid(row=2, column=1)
        ttk.Radiobutton(self.page_parent, text='rechts', variable=self.entriesUserInformation[1], value='rechts').grid(row=2, column=2)

        ttk.Entry(self.page_parent, textvariable=self.entriesUserInformation[2]).grid(row=3, column=1)
        ttk.Label(self.page_parent, text="(Eingabe muss Ganzzahl sein(z.B. 23))").grid(row=3, column=2)

        ttk.Radiobutton(self.page_parent, text="männlich", variable=self.entriesUserInformation[3], value="maennlich").grid(row=4, column=1)
        ttk.Radiobutton(self.page_parent, text="weiblich", variable=self.entriesUserInformation[3], value="weiblich").grid(row=4, column=2)
        ttk.Radiobutton(self.page_parent, text="divers", variable=self.entriesUserInformation[3], value="divers").grid(row=4, column=3)
        
        ttk.Button(master=self.page_parent, text="Tracking starten", command=lambda: [self.show_pageTwo(), self.update_dict(self.entriesUserInformation), 
        self.start_ButtonClicked()]).grid(row=5, column=1)


    def show_pageTwo(self):
        self.page_parent.destroy()
        self.page_parent = ttk.Frame(self, borderwidth=10, relief="sunken")
        self.page_parent.grid(row=0, column=0)
        self.page_parent.rowconfigure(0, weight=1)
        self.page_parent.columnconfigure(0, weight=1)

        ttk.Label(master=self.page_parent, text="Seite 2").grid(row=0, column=0) #, font=LARGE_FONT
        # tk.Label(master=parent_frame, text="Livemenü").grid(row=0, column=0)
        ttk.Button(master=self.page_parent, text="Stoppen", command= lambda: [self.show_pageThree(), self.stop_ButtonClicked()]).grid(row=1, column=0)

    def show_pageThree(self):
        self.page_parent.destroy()
        self.page_parent = ttk.Frame(self, borderwidth=10, relief="sunken")
        self.page_parent.grid(row=0, column=0)
        self.page_parent.rowconfigure(0, weight=1)
        self.page_parent.columnconfigure(0, weight=1)

        ttk.Label(master=self.page_parent, text="Seite 3: Analyse-Bereich", font=LARGE_FONT).grid(row=0, column=0)

        analysis_frame = ttk.Frame(master=self.page_parent)
        analysis_frame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        control_frame = ttk.Frame(master=self.page_parent)
        # control_frame.rowconfigure(0, weight=1)
        # control_frame.columnconfigure(0, weight=1)
        control_frame.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

   
        ttk.Button(master=control_frame, text="Zurück zur Startseite", command=lambda:[self.show_startPage()] ).grid(row=0, column=0)
        ttk.Button(master=control_frame, text="Anwendung schließen und Daten speichern", command=lambda: [self.quit(), self.save_dataClicked()]).grid(row=0, column=1)


        heatmap_movement = self.controller.get_Heatmap(nameHeatmap = "Heatmap Bewegung")
        heatmap_clicks = self.controller.get_Heatmap(nameHeatmap = "Heatmap Klicks")
        
        #-------PLOTTING AREA-------------------
        #------COLORMAP

        # Figure und Axes erstellen
        fig, ax = plt.subplots()

        # Untergrundbild hinzufügen
        background_heatmap = plt.imread("backgroundHeatmap.png")      
        ax.imshow(background_heatmap)

        ax.set_title("Heatmap aus Bewegungsdaten")
        ax.set_aspect("equal")

        # #plotting der Heatmap/// Enstrpicht heatmap_list[0]
        
        ax.imshow(heatmap_movement, cmap='hot' , alpha=0.7) #cmap=newcmap
        # ax.imshow(heatmap_clicks, cmap='hot' , alpha=0.7) #cmap=newcmap
        
        #Einstellungen des Plots:
        # plt.colorbar()
        
        #shape von Hintergrund und Heatmap müssen übereinstimmen
        # FigureCanvasTkAgg für das Zeichnen in Tkinter verwenden
        canvas = FigureCanvasTkAgg(fig, master=analysis_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # NavigationToolbar2Tk hinzufügen
        toolbar = NavigationToolbar2Tk(canvas, analysis_frame)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
               



    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller


    def update_dict(self, entries):
        if self.controller:
            entries_model = []
            for index in range(len(entries)):
                entries_model.append(entries[index].get()) 
        
            self.controller.update_dict(entries_model)   

    def save_button_clicked(self):
            """
            Handle button click event
            :return:
            """
            if self.controller:
                print("save Funktion not yet implemented")
                #self.controller.save_DataToCSV(self.nameDataset_var.get())


    def get_heatmap(self, nameHeatmap):
        if self.controller:
            return self.controller.get_heatmap(nameHeatmap)

    def start_ButtonClicked(self):
        if self.controller:
            self.controller.start_Tracking()

    def stop_ButtonClicked(self):
        if self.controller:
            self.controller.stop_Tracking()

    def save_dataClicked(self):
        if self.controller:
            self.controller.save_DataToCSV() 


