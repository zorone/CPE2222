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
    
    def setWidgetType(self, widgetType):
        for t in ['radioButton']:
            if widgetType == 'radioButton':
                self.func = ttk.Radiobutton()
    
    def entryGenerate(self, *arg):
        for i, item in enumerate(arg):
            if(i == 0):
                setWidgetType(item)
        

if __name__ == "__main__":
    main = Main()
    main.mainloop()