import tkinter as tk
from tkinter import ttk

#Test for Page 1
class App(tk.Tk):
    #init function for class App,  general information, settings of GUI
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Mousetrack")
        self.iconbitmap() #eigenes Icon

    #-----------geometry of window
        window_width  = 500
        window_height = 500

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    #---------------------------
        
        #window is resizable
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    
    # creating a container
        # s = ttk.Style()
        # s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')

        container = ttk.Frame(self, width=window_width, height=window_height, relief='sunken')#, padding=), style='Danger.TFrame'
        # container.pack(side="top", fill="both", expand=True)
        container.grid(sticky='nesw', padx=window_width, pady=window_height)

        # container.grid_rowconfigure(0, weight = 1)
        # container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array

        self.frames = {}
        
        
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1):#, Page1, Page2):
            
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(sticky ="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        #frame.reset()
        frame.tkraise()

class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        #init function for class Frame
        ttk.Frame.__init__(self, parent)


class Page1(ttk.Frame):
    def __init__(self, parent, controller):
        #init function for class Frame
        ttk.Frame.__init__(self, parent)






if __name__ == "__main__":
    
    app = App()

    for child in app.winfo_children(): 
           child.grid_configure(padx=5, pady=5)

    print(app.grid_slaves())
    for w in app.grid_slaves(row=2): print(w)
    # namelbl.grid_info()
    #namelbl.grid_configure(sticky=(E,W))
    app.mainloop()