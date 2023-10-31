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
        
        self.calcEntry = ["radioButton", "Area of Rectangle", "Area of Triangle", "Pythagorean"]
        self.calcSelected = IntVar(-1)
        
        self.calcEntry = self.entryGenerate(self.calcEntry)
    
    def setWidgetType(self, widgetType):
        if widgetType == 'radioButton':
            self.func = ttk.Radiobutton()
    
    def entryGenerate(self, *arg):
        for i, item in enumerate(arg):
            if(i == 0):
                self.setWidgetType(item)
                continue
            
            
        

if __name__ == "__main__":
    main = Main()
    main.mainloop()