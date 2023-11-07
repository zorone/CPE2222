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
        self.respond = False
        
        self.spinBoxVar = [DoubleVar(), DoubleVar()]
        self.spinBoxVal = [float(), float()]
        self.res = float()
        
        self.mainFrame = self.buildFrame(self, x=0, y=0, width=3, height=7)
        self.optionFrame = self.buildLabelFrame(self.mainFrame, text="Calculation", x=0, y=0, width=1, height=3)
        self.optionList = self.buildRadioButton(self.optionFrame, self.option, self.optionText, amount=3)
        
        for option in self.optionList:
            option.config(command=self.trigger)
        
    def trigger(self):
        if not self.expand:
            self.expand = True
            self.expandWindow()
        
        self.setText()
        
    def activate(self):
        if self.optionVal == 0:
            res = self.areaRectangle()
        elif self.optionVal == 1:
            res = self.areaTriangle()
        elif self.optionVal == 2:
            res = self.pythagorean()

        if not self.respond:
            self.resLabel = ttk.Label(column=3, row=0, column justify='center', text='')

    def expandWindow(self):
        self.paramText = ['', '', '']
        
        self.actionFrame = self.buildLabelFrame(self.mainFrame, text="Parameter Setting", x=2, y=0, width=1, height=3)
        self.paramLabel = self.buildLabel(self.actionFrame, self.paramText, amount=3, pos=(E), justify='right')
        self.spinBoxParam = self.buildSpinBox(self.actionFrame, self.spinBoxVar, amount=2, startx=1, starty=0)
        self.paramSubmit = self.buildButton(self.actionFrame, startx=1, starty=2)
        self.paramSubmit[0].config(command=self.activate)

    def setText(self):
        labelText = [['Length:', 'Width:', 'Area'],
                     ['Base:', 'Height:', 'Area'],
                     ['The 1st side:', 'The 2nd side:', 'Pythagorean Theory']]
        
        self.optionVal = self.option.get()
        
        self.paramLabel[0].config(text=labelText[self.optionVal][0])
        self.paramLabel[1].config(text=labelText[self.optionVal][1])
        self.paramSubmit[0].config(text=labelText[self.optionVal][2])

    def buildFrame(self, host, x, y, width=1, height=1, pos=(N,W,E,S)):
        res = ttk.Frame(host, padding=5)
        res.grid(column=x, row=y, columnspan=width, rowspan=height, sticky=pos)
        return res

    def buildLabelFrame(self, host, text, x, y, width=1, height=1, pos=(N,W,E,S)):
        res = ttk.Labelframe(host, text=text, padding=5)
        res.grid(column=x, row=y, columnspan=width, rowspan=height, sticky=pos, padx=20, pady=(10, 20))
        return res
    
    def buildLabel(self, host, textList, amount=1, startx=0, starty=0, incrX=0, incrY=1, pos=(N,W,E,S), justify='center'):
        res = list()
        for i in range(0, amount):
            res += [ttk.Label(host, text=textList[i], justify=justify)]
            res[i].grid(column=startx, row=starty, sticky=pos)
            startx += incrX
            starty += incrY
        return res
    
    def buildRadioButton(self, host, var, textList, amount=1, startx=0, starty=0, incrX=0, incrY=1, pos=(N,W,E,S)):
        res = list()
        for i in range(0, amount):
            res += [ttk.Radiobutton(host, text=textList[i], value=i, variable=var)]
            res[i].grid(column=startx, row=starty, sticky=pos)
            startx += incrX
            starty += incrY
        return res
    
    def buildSpinBox(self, host, varList, amount=1, startx=0, starty=0, incrX=0, incrY=1, incr=0.1, pos=(N,W,E,S)):
        res = list()
        for i in range(0, amount):
            varList[i].set(1)
            res += [ttk.Spinbox(host, textvariable=varList[i], from_=1, to=100, increment=incr)]
            res[i].grid(column=startx, row=starty, sticky=pos)
            startx += incrX
            starty += incrY
        return res
    
    def buildButton(self, host, text='', amount=1, startx=0, starty=0, incrX=0, incrY=1, pos=(N,W,E,S)):
        res = list()
        for i in range(0, amount):
            res += [ttk.Button(host, padding=5, text=text)]
            res[i].grid(column=startx, row=starty, sticky=pos)
            startx += incrX
            starty += incrY
        return res
    

if __name__ == "__main__":
    main = Main()
    main.mainloop()