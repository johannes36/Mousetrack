import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)

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
        
                    
            for index, key in enumerate(controller.dictExportData):
                ttk.Checkbutton(body, text=controller.dictExportData[key]["name"],
                                variable= controller.entriesExportData[index],
                                onvalue=True, offvalue=False).grid(row=index+len(controller.entries_visualize)+2, column=0, sticky="w")

            
            #-------Control
            button1 = ttk.Button(control, text="zur nächsten Seite", command=lambda: [
                                controller.showFrame(PageFive),
                                controller.update_dict(controller.data_visualize, controller.entries_visualize), 
                                controller.update_dict(controller.dictExportData, controller.entriesExportData)
                                ])
            button1.grid(row=0, column=0)
