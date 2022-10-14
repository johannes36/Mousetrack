import tkinter as tk
from tkinter import ttk


LARGE_FONT = ("Verdana", 12)

class App(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Mousetrack")
        # self.iconbitmap()

        window_width  = 500
        window_height = 500

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
    
        container = ttk.Frame(self, relief="sunken", borderwidth=10)
        container.grid(sticky="nsew")
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(parent=container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        self.style = ttk.Style()
        self.style.configure("header.TFrame", background="green")
        
        header = ttk.Frame(self, style="header.TFrame", borderwidth=10).grid(sticky="nsew")#pack(expand=True, fill="both")#grid(sticky="nsew")
        self.style = ttk.Style()
        self.style.configure("header.TFrame", background="green")
        # header = ttk.Frame(self, style="header.TFrame").grid(row=0, column=0)
        # ttk.Label(header, text="Kopf Bereich").grid()

        # # ttk.Label(header, text="This is the header area of the StartPage", font=LARGE_FONT).grid(row=0, column=0, rowspan=2, columnspan=5, sticky="nsew")
        # self.style.configure("body.TFrame", background="red")
        # body    = ttk.Frame(self, style="body.TFrame").grid(row=1, column=0)

        # self.style.configure("control.TFrame", background="yellow")
        # control = ttk.Frame(self, style="control.TFrame").grid(row=2, column=0)
        # ttk.Label(control, text="Control Bereich").grid()


        # label1 = ttk.Label(self, text="This is the Headersssssssssssss", font=LARGE_FONT)
        # label1.grid(row=1, column=3, sticky="n")
        # label2 = ttk.Label(self, text="This is the Body", font=LARGE_FONT)
        # label2.grid(row=0, column=2, sticky="e")
        # label3 = ttk.Label(self, text="This is the control", font=LARGE_FONT)
        # label3.grid(row=0, column=3, sticky="ew")

class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        ttk.Label(self, text="Das ist die Ueberschrift von Page One").grid(row=0, column=0, rowspan=2, columnspan=5, sticky="nsew")

        labels_abfrage = ["Datensatz Name:", "starke Hand:", "Alter", "Technikaffinität", "Geschlecht"]
        for index_row, text in enumerate(labels_abfrage):
            ttk.Label(self, text=text).grid(row=index_row+2, column=0, sticky="nsew")

        ttk.Label(self, text="Hier ist der Kontrollbereich").grid(row=len(labels_abfrage)+2, column=0)

class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
 

if __name__ == "__main__":
    
    app = App()

    # for child in app.winfo_children(): 
    #        child.grid_configure(padx=5, pady=5)

    # print(app.grid_slaves())
    # for w in app.grid_slaves(row=2): print(w)
    # namelbl.grid_info()
    #namelbl.grid_configure(sticky=(E,W))
    app.mainloop()