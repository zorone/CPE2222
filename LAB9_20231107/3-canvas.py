from tkinter import *
from tkinter import ttk

class Main(Tk):
    def __init__(self):
        self.geometry("270x165")
        self.title('Canvas Drawing')
        
        self.mainFrameOption = {
            x: 0,
            y: 0,
        }
        self.mainFrame = buildFrame(self, self.mainFrameOption)
        
    def buildFrame(self, root, **options):
        res = ttk.Frame(root, padding=5)
        res.grid()
        return res
        
    def buildLabelFrame(self, root, text, **options):
        res = ttk.LabelFrame(root, padding=5, text=text)
        res.grid()
        return res

if __name__ == '__main__':
    main = Main()
    main.mainloop()