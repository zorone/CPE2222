from tkinter import *
from tkinter import ttk

class Build:
    def frame(host, x, y, width, height):
        res = ttk.Frame(host, padding=5)
        res.grid(row=x, column)
class Main(Tk):
    
    build = Build()
    
    def __init__(self,):
        super().__init__()
        
        self.title("CPE2222")
        self.style = ttk.Style()
        

if __name__ == "__main__":
    main = Main()
    main.mainloop()