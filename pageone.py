import tkinter as tk
from tkinter import ttk

class PageOne():

    button1 = tk.Button(text="next", command=show_nextPage_Button_clicked).grid(row=0, column=0)

    def show_nextPage_Button_clicked():
        
