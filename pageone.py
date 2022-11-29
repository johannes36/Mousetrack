import tkinter as tk
from tkinter import ttk


class PageOne(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        
        
        self.buttons = {}

        
        


        control_frame = tk.LabelFrame(master=self, text="Input data")
        control_frame.rowconfigure(0, weight=1)
        control_frame.columnconfigure(0, weight=1)
        control_frame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        label = tk.Label(control_frame, text="Seite 1").grid(row=0, column=0)
        
        self.create_button(frame=control_frame, name="Show Page2", row=1, column=0)


    def create_button(self, frame, name, row, column):
        self.buttons[name] = tk.Button(frame)
        self.buttons[name]["text"] = name
        self.buttons[name].grid(row=row, column=column)

    def create_frame(self):
        pass