import tkinter as tk
from tkinter import ttk

from pynput import mouse as mouse

import numpy as np

import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


class App(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # self.root = tk.Tk()
        

        self.move_x      = []
        self.move_y      = []
        self.random_heatmap = np.random.randint(low=0, high=200, size=(200, 250))        
    
        container = ttk.Frame(self, relief="sunken", borderwidth=10)
        container.grid(sticky="nsew")
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (PageOne, PageTwo):
            frame = F(parent=container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame(PageOne)



        self.listener = mouse.Listener(on_move=self.onMove, on_click=self.onClick)
        self.mainloop()

    def onMove(self, x, y):

        print('Maus bewegt zu {0}'.format((x, y)))
        self.move_x.append(x)
        self.move_y.append(y)

    def onClick(self, x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        print('{0}, {1} at {2}'.format(button, 'Pressed' if pressed else 'Released', (x, y)))

    def showFrame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def startApp(self):
        self.listener.start()


    def stopApp(self):
        self.listener.stop()        
        # self.heatmap_move, self.standartHeatmap = self.calculateHeatmap(self.move_x, self.move_y)
        self.heatmap_move = self.calculateHeatmap(self.move_x, self.move_y)
        

    def calculateHeatmap(self, x_Data, y_Data):

        heatmap = np.zeros(shape=(max(y_Data), max(x_Data)))

        for i in range(len(x_Data)):
            heatmap[y_Data[i] - 1, x_Data[i] - 1] = heatmap[y_Data[i] - 1, x_Data[i] - 1] + 1

        return heatmap

    def finishApp(self):
        # self.root.destroy()
        self.quit()


class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        ttk.Label(self, text="Seite 1, Start und Stopp").grid(row=0, column=0, rowspan=2, columnspan=5, sticky="nsew")

        ttk.Button(self, text="Starten", command=lambda: controller.startApp()).grid(row=1, column=0)
        ttk.Button(self, text="Stoppen und next Page", command=lambda: [
                                                    controller.stopApp(),  
                                                    controller.showFrame(PageTwo)
                                                    ]).grid(row=1, column=1)



class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        header = ttk.Frame(self, relief="raised", borderwidth=5)
        header.grid(row=0, column=0, sticky="nsew")

        body = ttk.Frame(self, relief="sunken", borderwidth=5)
        body.grid(row=1, column=0, sticky="nsew")
        
        control = ttk.Frame(self, relief="raised", borderwidth=5)
        control.grid(row=2, column=0, sticky="nsew")


        ttk.Label(header, text="Seite 2, Auswertung").grid(row=0, column=0, rowspan=2, columnspan=5, sticky="nsew")


        #Standart Map plotten und anzeigen
        # canvas_parent = tk.Canvas(body)
        # Figure(figsize=(5, 4), dpi=100)
        # im = ax.imshow(controller.random_heatmap)



        # canvas = FigureCanvasTkAgg(fig, body)
        # canvas.draw()
        # canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
 
        # toolbar = NavigationToolbar2Tk(canvas, body, pack_toolbar=False)
        # toolbar.update()
        # toolbar.pack(side=tk.BOTTOM, fill=tk.X)#

        #--------Eigenes Vorgehen Plot der Standartheatmap
        #creating a figure
        self.fig = plt.figure()

        #adding an axes object
        self.ax = self.fig.add_subplot(111) 
        self.ax.set_title("Heatmap aus Zufallszahlen")
        #plotting der Heatmap
        self.ax.imshow(controller.random_heatmap, cmap='hot', interpolation='nearest') #, cmap='gray')
        #creating a Tkinter canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=body)
        self.canvas.draw()

        #canvas in body platzieren
        self.canvas.get_tk_widget().pack()

        # creating the Matplotlib toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas,
                                    body)
        self.toolbar.update()            

        # placing the toolbar on the Tkinter window
        self.canvas.get_tk_widget().pack

        #-----------Control Section
        ttk.Button(control, text="Show Heatmap der Moves",
                             command=lambda:
                             self.showHeatmap(parent=body, figure=self.fig, map=controller.heatmap_move, title="cleared")
                             ).grid(row=0, column=0)
        # ttk.Button(control, text="Anwendung beenden",
        #                     command= lambda: controller.finishApp()).grid(row=0, column=1)
        ttk.Button(header, text="Anwendung beenden",
                            command= lambda: controller.finishApp()).grid(row=2, column=1)


    #Plot aktualiseren, wenn Klicks dazukommen an Skalierung denken
    def showHeatmap(self, parent, figure, map, title):
        plt.clf()
        self.ax.set_title(title)
        
        self.ax.figure.canvas.draw()
        # plt.title(title)
        # canvas = FigureCanvasTkAgg(figure, parent)
        # canvas.draw()
        # canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# if __name__ == "__main__":
    
app = App()