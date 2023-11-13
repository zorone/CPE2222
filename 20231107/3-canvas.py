from tkinter import *
from tkinter import ttk

class Main(Tk):
    def __init__(self):
        self.geometry("270x165")
        self.title('Canvas Drawing')
        
    def buildFrame(self):
        res = ttk.Frame()
        
    def buildLabelFrame(self):
        print()

if __name__ == '__main__':
    main = Main()
    main.mainloop()