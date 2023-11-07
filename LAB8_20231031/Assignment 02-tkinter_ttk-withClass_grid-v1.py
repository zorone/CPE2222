from tkinter import *
from tkinter import ttk

class Main(Tk):
    
    
    def __init__(self,):
        super().__init__()
        
        self.title("CPE2222")
        self.style = ttk.Style()
        
        self.mainFrame = self.buildFrame(self, x=0, y=0, width=3, height=7)
        self.optionFrame = self.buildLabelFrame(self.mainFrame, text="Calculation", x=0, y=0, width=1, height=3)

    def buildFrame(self, host, x, y, width=1, height=1, pos=(N,W,E,S)):
        res = ttk.Labelframe(host, padding=5)
        res.grid(column=x, row=y, columnspan=width, rowspan=height, sticky=pos)
        return res

    def buildLabelFrame(self, host, text, x, y, width=1, height=1, pos=(N,W,E,S)):
        res = ttk.Labelframe(host, text=text, padding=5)
        res.grid(column=x, row=y, columnspan=width, rowspan=height, sticky=pos)
        return res

if __name__ == "__main__":
    main = Main()
    main.mainloop()