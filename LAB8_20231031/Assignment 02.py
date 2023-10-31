from tkinter import *
from tkinter import ttk

class Main(Tk):
    def __init__(self, ):
        super().__init__()
        
        self.title("CPE2222")
        self.style = ttk.Style()
        
        self.mainFrame = ttk.Frame(self, padding=5)
        self.mainFrame.pack()
        
        self.calcOption = ttk.Labelframe(self.mainFrame, padding=5, text='Calculation')
        self.calcOption.pack(side='left')
        
        self.calcEntry = ["Area of Rectangle", "Area of Triangle", "Pythagorean"]
        self.calcSelected = IntVar()
        
        self.paramLabel = list()
        self.paramEntry = list()
        self.paramVar = list()
        self.prevSession = int()
        
        self.widgetText = [['Length:', 'Width:', 'Area'],
                           ['Base', 'Height', 'Area'],
                           ['The 1st size:', 'The 2nd size:', 'Pythagorean Theory']]
        
        self.pane = False
        
        for i, title in enumerate(self.calcEntry):
            self.calcEntry[i] = ttk.Radiobutton(self.calcOption, text=title, value=i, variable=self.calcSelected, command=self.calcOptionSet)
            self.calcEntry[i].pack(side='top', anchor='w')
        
    def calcOptionSet(self):
        self.paramGenerate()
        self.prevSession = self.calcSelected
        self.setText()
            

    def paramGenerate(self):
        if self.pane:
            return
        
        self.pane = True

        self.paramOption = ttk.Labelframe(self.mainFrame, padding=5, text='Parameter Setting')
        self.paramOption.pack(side='left')
        
        for i in range(2):
            self.paramLabel += [ttk.Label(self.paramOption, justify='right')]
            self.paramLabel[i].pack(side='top')
            self.paramVar += [DoubleVar()]
            self.paramEntry += [ttk.Spinbox(self.paramOption, justify='left', textvariable=self.paramVar[i])]
            self.paramEntry[i].pack(side='left')
        
        self.submitButton = ttk.Button(self.paramOption, padding=5, command=self.calculate)
        self.submitButton.pack(side='top')
        
    def setText(self):
        if self.prevSession == self.calcSelected
        return

    def calculate(self):
        print()
    
if __name__ == "__main__":
    main = Main()
    main.mainloop()