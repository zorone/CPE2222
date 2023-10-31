from tkinter import *
from tkinter import ttk

class Main(Tk):
    def __init__(self, ):
        super().__init__()
        
        self.title("CPE2222")
        self.style = ttk.Style()
        
        self.mainFrame = Frame(self, padding=5)
        self.mainFrame.pack()
        
        self.calcOption = Frame(self.mainFrame, padding=5, name='Calculation')
        self.calcOption.pack()
        
        self.calcEntry = list()
        self.calcValue = IntVar(-1)
    
    def entryGenerate(self):
        
        
if __name__ == "__main__":
    main = Main()
    main.mainloop()