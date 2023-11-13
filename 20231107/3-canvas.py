from tkinter import *
from tkinter import ttk

class Main(Tk):
    def __init__(self):
        self.geometry("270x165")
        self.title('Canvas Drawing')
        
    def buildFrame(self, root):
        res = ttk.Frame(root, padding=5)
        res.grid()
        return res
        
    def buildLabelFrame(self, root):
        res = ttk.LabelFrame(root, padding=5)

if __name__ == '__main__':
    main = Main()
    main.mainloop()