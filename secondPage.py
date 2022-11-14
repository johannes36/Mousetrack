import tkinter as tk
from tkinter import ttk

from firstPage import FirstPage

class SecondPage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        button_nextPage = ttk.Button(self, text="weiter", command=self.buttonNextPageClicked(FirstPage))


    def buttonNextPageClicked(self, next):
        
        
        self.frames = {}

        for F in (startpage, pageone, pagetwo, pagethree, pagefour, pagefive):

            frame = F(parent=container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            # frame.pack(fill="both")
        self.showFrame(startpage)
        
        # self.heatmap_move = np.empty()
        # self.heatmap_click = np.empty()

        self.protocol("WM_DELETE_WINDOW", func=self.finishApp())
        self.mainloop()
    
    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  
