from tkinter import *
from tkinter import ttk

class Main(Tk):
    
    
    def __init__(self,):
        super().__init__()
        
        self.title("CPE2222")
        self.style = ttk.Style()
        
        self.mainFrame = ttk.Frame(self, padding=5)
        self.mainFrame.grid(row=0, column=0, rowspan=3, columnspan=3, sticky=(N,W,E,S))
        
        self.optionFrame = ttk.Labelframe(self.mainFrame, text="Calculation", padding=5)
        self.optionFrame.grid(row=0, column=0, sticky=(N,W,E,S))

if __name__ == "__main__":
    main = Main()
    main.mainloop()