import tkinter as tk
from tkinter import ttk

import numpy as np

import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)  # type: ignore
from matplotlib import cm
from matplotlib.figure import Figure
from matplotlib.colors import ListedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable
import seaborn as sns

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        
        self.entriesUserInformation = [tk.StringVar(), tk.StringVar(), tk.IntVar(), tk.StringVar()]

        self.page_parent = ttk.Frame(self)
        self.show_pageOne()

        #Seite 1 platzieren und Kommandos den buttons hinzufügen
        # self.page1.create_Page(master=self.page_parent)
        # self.bind_commandsToPage(self.page1)


    def show_pageOne(self):
        self.page_parent.destroy()

        self.page_parent = ttk.Frame(self)
        self.page_parent.grid(row=0, column=0)
        
        self.page_parent.destroy()
        self.page_parent = ttk.Frame(self)
        self.page_parent.grid(row=0, column=0)

        parent_frame = tk.LabelFrame(master=self.page_parent, text="Seite1")
        parent_frame.rowconfigure(0, weight=1)
        parent_frame.columnconfigure(0, weight=1)
        parent_frame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        tk.Label(master=parent_frame, text="Mousetrack").grid(row=0, column=0)
        tk.Label(master=parent_frame, text="Dies ist eine Anwendung, mit der sich das Mausverhalten\n  an einem Computer visualisieren lässt").grid(row=0, column=0)
            
        ttk.Button(master=parent_frame, text="Nächste Seite", command= self.show_pageTwo).grid(row=1, column=0)

    def show_pageTwo(self):
        self.page_parent.destroy()
        self.page_parent = ttk.Frame(self)
        self.page_parent.grid(row=0, column=0)


        parent_frame = tk.LabelFrame(master=self.page_parent, text="Seite2")
        parent_frame.rowconfigure(0, weight=1)
        parent_frame.columnconfigure(0, weight=1)
        parent_frame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        tk.Label(master=parent_frame, text="Informationsabfrage").grid(row=0, column=0)

        labels = ("Name Datensatz:", "Starke Hand:",  "Alter:", "Geschlecht:")

        for row_index, label in enumerate(labels):
            ttk.Label(master=parent_frame, text=label).grid(row=row_index+1, column=0, sticky="w")

        ttk.Entry(parent_frame, textvariable=self.entriesUserInformation[0]).grid(row=1, column=1)

        ttk.Radiobutton(parent_frame, text='links', variable=self.entriesUserInformation[1], value='left').grid(row=2, column=1)
        ttk.Radiobutton(parent_frame, text='rechts', variable=self.entriesUserInformation[1], value='rechts').grid(row=2, column=2)

        ttk.Entry(parent_frame, textvariable=self.entriesUserInformation[2]).grid(row=3, column=1)
        ttk.Label(parent_frame, text="(Eingabe muss Ganzzahl sein(z.B. 23))").grid(row=3, column=2)

        ttk.Radiobutton(parent_frame, text="männlich", variable=self.entriesUserInformation[3], value="maennlich").grid(row=4, column=1)
        ttk.Radiobutton(parent_frame, text="weiblich", variable=self.entriesUserInformation[3], value="weiblich").grid(row=4, column=2)
        ttk.Radiobutton(parent_frame, text="divers", variable=self.entriesUserInformation[3], value="divers").grid(row=4, column=3)
        
        ttk.Button(master=parent_frame, text="Tracking starten", command=lambda: [self.show_pageThree(), self.update_dict(self.entriesUserInformation), 
        self.start_ButtonClicked()]).grid(row=5, column=1)


    def show_pageThree(self):
        self.page_parent.destroy()
        self.page_parent = ttk.Frame(self)
        self.page_parent.grid(row=0, column=0)

        parent_frame = tk.LabelFrame(master=self.page_parent, text="Seite3")
        parent_frame.rowconfigure(0, weight=1)
        parent_frame.columnconfigure(0, weight=1)
        parent_frame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        tk.Label(master=parent_frame, text="Livemenü").grid(row=0, column=0)
        ttk.Button(master=parent_frame, text="Stoppen", command= lambda: [self.show_pageFour(), self.stop_ButtonClicked()]).grid(row=1, column=0)

    def show_pageFour(self):
        self.page_parent.destroy()
        self.page_parent = ttk.Frame(self)
        self.page_parent.grid(row=0, column=0)

        parent_frame = tk.LabelFrame(master=self.page_parent, text="Seite4")
        parent_frame.rowconfigure(0, weight=1)
        parent_frame.columnconfigure(0, weight=1)
        parent_frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

   
        ttk.Button(master=parent_frame, text="Zurück zur Startseite", command=lambda:[self.show_pageOne()] ).grid(row=0, column=0)
        ttk.Button(master=parent_frame, text="Anwendung schließen und Daten speichern", command=lambda: [self.quit()]).grid(row=0, column=1)

        background_heatmap = plt.imread("backgroundHeatmap.png")
        heatmap_movement = self.controller.get_Heatmap(nameHeatmap = "Heatmap Bewegung")
        heatmap_clicks = self.controller.get_Heatmap(nameHeatmap = "Heatmap Klicks")
        
        # #-------PLOTTING AREA-------------------

        colormap = mpl.colormaps['YlOrRd']  # type: ignore
        newcolors = colormap(np.linspace(0.3, 1, 256))
        white = np.array([1, 1, 1, 1])
        newcolors[:25, :] = white

        # cmap = cm.get_cmap("YlOrRd", 100)
        # self.newcmap = ListedColormap(cmap(np.linspace(0, 0.7, 100)))  # type: ignore
        self.newcmap = ListedColormap(newcolors)  # type: ignore
        #creating a figure
        fig = plt.figure()
        #adding an axes object
        ax = fig.add_subplot() 
        ax.set_title("Heatmap aus Bewegungsdaten")
        #plotting der Heatmap/// Enstrpicht heatmap_list[0]
        
        #ax.imshow(.....)

        plt.imshow(background_heatmap)

        plt.pcolormesh(heatmap_movement, alpha=0.8)#, cmap=self.newcmap) #vmin, vmax -> range of colornao
        
        # hmax = sns.heatmap(heatmap_movement, alpha=0.7, cmap=self.newcmap, annot=True, zorder=2)
        # hmax.imshow(background_heatmap, aspect = hmax.get_aspect(), extent = hmax.get_xlim() + hmax.get_ylim(), zorder = 1)


        # divider = make_axes_locatable(ax)
        # cax = divider.append_axes("right", size="5%", pad=0.25)

        # plt.colorbar(cax=cax)

        #Skalierung(Bild zu Heatmap prüfen und evtl. Heatmap nur int(ist aber eig nur  int))
        #-------TKINTER AREA ---------creating a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self.page_parent)
        canvas.draw()
        
        #canvas in body platzieren
        canvas.get_tk_widget().grid()
        # creating the Matplotlib toolbar
        
        # toolbar = NavigationToolbar2Tk(canvas, parent_analyseFrame)
        # toolbar.update() 
                   
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().grid
       



        print("SHape Map:")
        print(np.shape(heatmap_movement))


        print("SHape Backgrpund:")
        print(np.shape(background_heatmap))


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


