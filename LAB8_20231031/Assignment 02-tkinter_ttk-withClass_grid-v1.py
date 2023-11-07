from tkinter import *
from tkinter import ttk

class Main(Tk):
    
    
    def __init__(self,):
        super().__init__()
        
        self.title("CPE2222")
        self.style = ttk.Style()
        
        self.option = IntVar()
        self.optionText = ['Area of Rectangle', 'Area of Triangle', 'Pythagorean']
        
        self.expand = False
        
        self.mainFrame = self.buildFrame(self, x=0, y=0, width=3, height=7)
        self.optionFrame = self.buildLabelFrame(self.mainFrame, text="Calculation", x=0, y=0, width=1, height=3)
        self.optionList = self.buildRadioButton(self.optionFrame, self.option, self.optionText, amount=3)
        
        for option in self.optionList:
            option.config(command=self.trigger)
        
    def trigger(self):
        if not self.expand:
            self.expand = True
            self.expandWindow()
        else:
            print()
            
    def expandWindow(self):
        self.paramText = ['', '', '']
        
        self.actionFrame = self.buildLabelFrame(self.mainFrame, text="Parameter Setting", x=2, y=0, width=1, height=3)
        self.paramLabel = self.buildLabel(self.actionFrame, self.paramText, 3, pos=(E))

    def buildFrame(self, host, x, y, width=1, height=1, pos=(N,W,E,S)):
        res = ttk.Frame(host, padding=5)
        res.grid(column=x, row=y, columnspan=width, rowspan=height, sticky=pos)
        return res

    def buildLabelFrame(self, host, text, x, y, width=1, height=1, pos=(N,W,E,S)):
        res = ttk.Labelframe(host, text=text, padding=5)
        res.grid(column=x, row=y, columnspan=width, rowspan=height, sticky=pos, padx=5)
        return res
    
    def buildLabel(self, host, textList, amount=1, pos=(N,W,E,S)):
        res = list()
        for i in range(0, amount):
            res += [ttk.Label(host, text=textList[i], justify='center')]
            res[i].grid(column=0, row=i, sticky=pos)
    
    def buildRadioButton(self, host, var, textList, amount=1, pos=(N,W,E,S)):
        res = list()
        for i in range(0, amount):
            res += [ttk.Radiobutton(host, text=textList[i], value=i, variable=var)]
            res[i].grid(column=0, row=i, sticky=pos)
        return res

if __name__ == "__main__":
    main = Main()
    main.mainloop()