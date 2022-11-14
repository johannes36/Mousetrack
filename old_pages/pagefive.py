import tkinter as tk

from tkinter import ttk
import matplotlib as mpl

mpl.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)  # type: ignore

# from matplotlib.figure import Figure
from matplotlib import cm
from matplotlib.colors import ListedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable

import numpy as np
LARGE_FONT= ("Verdana", 12)




class PageFive(tk.Frame): #Rename
    #5te Seite des Gui, die der Darstellung der Informationen dienen soll
    #Graph Page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        header = ttk.Frame(self, relief="raised", borderwidth=5)
        header.grid(row=0, column=0, columnspan=3, sticky="nsew")

        body = ttk.Frame(self, relief="sunken", borderwidth=5)
        body.grid(row=1, column=0, columnspan=3, sticky="nsew")
        
        control = ttk.Frame(self, relief="raised", borderwidth=5)
        control.grid(row=2, column=0, columnspan=3 ,sticky="nsew")

        #----------Header
        ttk.Label(header, text="Seite 5: Darstellung der Inhalte", font=LARGE_FONT).grid()

        #-------PLOTTING AREA-------------------
        self.background = plt.imread("backgroundHeatmap.png")

        colormap = mpl.colormaps['YlOrRd']  # type: ignore
        newcolors = colormap(np.linspace(0.3, 1, 256))
        white = np.array([1, 1, 1, 1])
        newcolors[:25, :] = white
        # cmap = cm.get_cmap("YlOrRd", 100)
        # self.newcmap = ListedColormap(cmap(np.linspace(0, 0.7, 100)))  # type: ignore
        self.newcmap = ListedColormap(newcolors)  # type: ignore
        print("in init: " + str(self.newcmap))
        #creating a figure
        fig = plt.figure()
        #adding an axes object
        ax = fig.add_subplot() 
        ax.set_title("Heatmap aus Zufallszahlen")
        #plotting der Heatmap/// Enstrpicht heatmap_list[0]
        
        #ax.imshow(.....)
        plt.imshow(controller.standart_background)
        plt.pcolormesh(controller.random_heatmap, alpha=0.8, cmap=self.newcmap)
        
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.25)

        plt.colorbar(cax=cax)

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
                            command=lambda: controller.showFrame(StartPage)) #commmand für neuen Thread, Datenspeicherung, neuer Datensatz (----> Programmende!!)
        button1.grid(row=0, column=0)

        self.button2 = ttk.Button(control, text="Heatmaps anzeigen",
                            command=lambda: self.ShowHeatmap(axes=ax, parent_canvas=canvas, value_list=controller.heatmap_list, name_list=controller.heatmap_names, parent_frame=control, controller=self.controller))
        self.button2.grid(row=0, column=1, columnspan=2)
        
        # self.button2 = ttk.Button(control, text="Heatmaps anzeigen",
        #                     command=lambda: self.ShowHeatmap(axes=ax, parent_canvas=canvas, value_list=controller.heatmap_list, name_list=controller.heatmap_names, parent_frame=control, controller=self.controller))
        # self.button2.grid(row=0, column=1, columnspan=2)
        

        button3 = ttk.Button(control, text="Anwendung schließen",
                            command=lambda: [controller.finishApp()])#, controller.writeCSVFile()])
        button3.grid(row=0, column=3)
            

    def ShowHeatmap(self, axes, parent_canvas, value_list, name_list, parent_frame, controller):
        #use image viewer example
        #Alter Ansatz mit dict
        # axes.clear()
        # axes.set_title(dict["map_2"]["title"])
        # axes.imshow(dict["map_2"]["value"], cmap='hot', interpolation='nearest')


        

        axes.clear()
        axes.set_title(name_list[1])
        axes.imshow(self.background)
        plt.pcolormesh(value_list[1], alpha=0.8, cmap=self.newcmap)
        print("in ShowHeat: " + str(self.newcmap))


        parent_canvas.draw()
        parent_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.button2.grid_forget()

        
        #Code für Image List
        # my_label = tk.Label(image=imagelist[imagenumber])
        # my_label.grid()

        self.button_back = ttk.Button(parent_frame, text="<<", command= lambda:
        self.showPreviousHeatmap(axes=axes, parent_canvas=parent_canvas, parent_frame=parent_frame, value_list=controller.heatmap_list, name_list=controller.heatmap_names, seite=0, controller=controller))
        self.button_back.grid(row=0, column=1)

        self.button_forward = ttk.Button(parent_frame, text=">>", command= lambda:
        self.showNextHeatmap(axes=axes, parent_canvas=parent_canvas, parent_frame=parent_frame, value_list=controller.heatmap_list, name_list=controller.heatmap_names, seite=2, controller=controller))
        self.button_forward.grid(row=0, column=2)



    def showNextHeatmap(self, axes, parent_canvas, parent_frame, value_list, name_list, seite, controller):#, parent_frame, controller):
        #Alter Ansatz mit dict:
        # axes.clear()
        # axes.set_title(dict["map_3"]["title"])
        # axes.imshow(dict["map_3"]["value"], cmap='hot', interpolation='nearest')
        # parent_canvas.draw()
        # parent_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        axes.clear()
        axes.set_title(name_list[seite])
        # plt.imshow(self.background)
        axes.imshow(self.background)
        plt.pcolormesh(value_list[seite], alpha=0.8, cmap=self.newcmap)
        print("in ShowNext: " + str(self.newcmap))

        parent_canvas.draw()
        parent_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.button_back.grid_forget()
        self.button_forward.grid_forget()
        self.button_back    = ttk.Button(parent_frame, text="<<", command= lambda: self.showPreviousHeatmap(axes=axes, parent_canvas=parent_canvas, parent_frame=parent_frame, value_list=controller.heatmap_list, name_list=controller.heatmap_names, seite=seite-1, controller=controller))
        self.button_forward = ttk.Button(parent_frame, text=">>", command= lambda: self.showNextHeatmap(axes=axes, parent_canvas=parent_canvas, parent_frame=parent_frame, value_list=controller.heatmap_list, name_list=controller.heatmap_names, seite=seite+1, controller=controller))
        self.button_back.grid(row=0, column=1)
        self.button_forward.grid(row=0, column=2)
        
        if seite==2:
            print("forward disabled")
            self.button_forward = ttk.Button(parent_frame, text=">>", state='disabled')
            self.button_forward.grid(row=0, column=2)
        
    def showPreviousHeatmap(self, axes, parent_canvas, parent_frame, value_list, name_list, seite, controller):
        
        # axes.clear()
        # axes.set_title(dict["map_1"]["title"])
        # axes.imshow(dict["map_1"]["value"], cmap='hot', interpolation='nearest')
        # parent_canvas.draw()
        # parent_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        axes.clear()
        axes.set_title(name_list[seite])
        #plt.imshow(self.background)
        axes.imshow(self.background)
        plt.pcolormesh(value_list[seite], alpha=0.8, cmap=self.newcmap)
        print("in ShowPrevious: " + str(self.newcmap))
        
        parent_canvas.draw()
        parent_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.button_back.grid_forget()
        self.button_forward.grid_forget()
        self.button_back    = ttk.Button(parent_frame, text="<<", command= lambda: self.showPreviousHeatmap(axes=axes, parent_canvas=parent_canvas, parent_frame=parent_frame, value_list=controller.heatmap_list, name_list=controller.heatmap_names, seite=seite-1, controller=controller))
        self.button_forward = ttk.Button(parent_frame, text=">>", command= lambda: self.showNextHeatmap(axes=axes, parent_canvas=parent_canvas, parent_frame=parent_frame, value_list=controller.heatmap_list, name_list=controller.heatmap_names, seite=seite+1, controller=controller))
        self.button_back.grid(row=0, column=1)
        self.button_forward.grid(row=0, column=2)
               
        if seite==0:
            print("back disabled")
            self.button_back = ttk.Button(parent_frame, text="<<", state='disabled')
            self.button_back.grid(row=0, column=1)