from tkinter import *
from tkinter import ttk

class Main(Tk):
    def __init__(self, ):
        super().__init__()
        
        self.title("CPE2222")
        self.style = ttk.Style()
        
        self.mainFrame = ttk.Frame(self, padding=5)
        self.mainFrame.pack(expand='TRUE', fill='both')
        
        self.topFrame = ttk.Frame(self.mainFrame, padding=5)
        self.topFrame.pack(side='top', expand='TRUE', fill='both')
        
        self.calcOption = ttk.Labelframe(self.topFrame, padding=5, text='Calculation')
        self.calcOption.pack(side='left', expand='TRUE', fill='both')
        
        self.calcEntry = ["Area of Rectangle", "Area of Triangle", "Pythagorean"]
        self.calcSelected = IntVar()
        
        self.paramLabel = list()
        self.paramFrame = list()
        self.paramEntry = list()
        self.paramVar = list()
        self.prevSession = -1
        self.currentSession = 0
        
        self.paramVal = [0, 0]
        self.result = int()
        self.res = str()
        self.resCheck = False
        
        self.widgetText = [['Length:', 'Width:', 'Area'],
                           ['Base:', 'Height:', 'Area'],
                           ['The 1st size:', 'The 2nd size:', 'Pythagorean Theory']]
        
        self.pane = False
        
        for i, title in enumerate(self.calcEntry):
            self.calcEntry[i] = ttk.Radiobutton(self.calcOption, text=title, value=i, variable=self.calcSelected, command=self.calcOptionSet)
            self.calcEntry[i].pack(side='top', anchor='w', expand='TRUE', fill='y')
        
    def calcOptionSet(self):
        self.paramGenerate()
        self.setText()
            

    def paramGenerate(self):
        if self.pane:
            return
        
        self.pane = True

        self.paramOption = ttk.Labelframe(self.topFrame, padding=5, text='Parameter Setting')
        self.paramOption.pack(side='left', expand='TRUE', fill='both')
        
        for i in range(2):
            self.paramFrame +=[ttk.Frame(self.paramOption)]
            self.paramFrame[i].pack(expand='TRUE', fill='both')
            self.paramLabel += [ttk.Label(self.paramFrame[i], justify='right')]
            self.paramLabel[i].pack(side='left', expand='TRUE', fill='y')
            self.paramVar += [DoubleVar()]
            self.paramEntry += [ttk.Spinbox(self.paramFrame[i], justify='left', textvariable=self.paramVar[i])]
            self.paramEntry[i].pack(side='left', expand='TRUE', fill='y')
        
        self.paramFrame +=[ttk.Frame(self.paramOption)]
        self.paramFrame[2].pack(expand='TRUE', fill='both')
        self.paramEntry += [ttk.Button(self.paramFrame[2], padding=5, command=self.activate)]
        self.paramEntry[2].pack(side='right', expand='TRUE', fill='y')
        self.paramEntry += [ttk.Frame(self.paramFrame[2], padding=5)]
        self.paramEntry[3].pack(side='right', expand='TRUE', fill='y')
        
    def setText(self):
        self.currentSession = self.calcSelected.get()
        if self.prevSession == self.currentSession:
            return
        
        self.prevSession = self.currentSession
        
        for i in range(2):
            self.paramLabel[i].config(text=self.widgetText[self.currentSession][i])
        
        self.paramEntry[2].config(text=self.widgetText[self.currentSession][2])

    def activate(self):
        self.get()
        self.calculate()
        self.respond()
        
    def get(self):
        for i in range(2):
            self.paramVal[i] = self.paramVar[i].get()

    def calculate(self):
        if self.currentSession == 0:
            self.rectangleArea()
        elif self.currentSession == 1:
            self.triangleArea()
        elif self.currentSession == 2:
            self.pythagorean()
        else:
            print('Not implement')

    def rectangleArea(self):
        self.result = self.paramVal[0] * self.paramVal[1]
        self.res = 'The area of rectangle with length of {} and width of {} is {}'.format(self.paramVal[0], self.paramVal[1], self.result)

    def triangleArea(self):
        self.result = (1/2)*self.paramVal[0] * self.paramVal[1]
        self.res = 'The area of triangle with base of {} and height of {} is {}'.format(self.paramVal[0], self.paramVal[1], self.result)

    def pythagorean(self):
        self.result = (self.paramVal[0]**2 + self.paramVal[1]**2)**(1/2)
        self.res = 'The longest size of right triangle with ({}, {}) is {}'.format(self.paramVal[0], self.paramVal[1], self.result)
        
    def respond(self):
        if self.resCheck:
            self.resLabel.config(text=self.res)
        else:
            self.resCheck = True
            self.resFrame = ttk.Frame(self.mainFrame, padding=5)
            self.resFrame.pack(side='top', fill='none')
            
            self.resLabel = ttk.Label(self.resFrame, text=self.res, justify='center', anchor='center')
            self.resLabel.pack(expand='TRUE', fill='both')
if __name__ == "__main__":
    main = Main()
    main.mainloop()