from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math

class Main(Tk):
    def __init__(self):
        self.geometry('270x165')
        self.title('Canvas Drawing')
        
        self.rectangleSet = IntVar(value=0)
        self.triangleSet = IntVar(value=0)
        self.circleSet = IntVar(value=0)
        
        self.rectangleVal = StringVar()
        self.triangleVal = StringVar()
        self.circleVal = StringVar()
        
        self.mainFrame = ttk.Frame(self, padding=5)
        self.mainFrame.pack(anchor='center', side='top', fill='both', expand=TRUE)
        
        self.optionFrame = ttk.Labelframe(self.mainFrame, text='Drawing Setting')
        self.optionFrame.pack(anchor='center', side='top', fill='both', expand=TRUE, ipad=5, ipady=5, padx=5, pady=5)
        
        self.drawButton = ttk.Button(self.mainFrame, padding=5, text='Draw')
        self.drawButton.pack(anchor='center', side='top', fill='both', expand=TRUE)
        
        self.rectangleTick = ttk.Checkbutton(self.optionFrame, text='Rectangle', onvalue=1, offvalue=0, variable=self.rectangleSet, command=self.showOption)
        self.rectangleTick.anchor('w')
        self.rectangleTick.grid(column=0, row=0, sticky=(N,W,E,S))
        
        self.triangleTick = ttk.Checkbutton(self.optionFrame, text='Right Triangle', onvalue=1, offvalue=0, variable=self.triangleSet)
        self.triangleTick.anchor('w')
        self.triangleTick.grid(column=0, row=1, sticky=(N,W,E,S))
        
        self.circleTick = ttk.Checkbutton(self.optionFrame, text='Circle', onvalue=1, offvalue=0, variable=self.circleSet)
        self.circleTick.anchor('w')
        self.circleTick.grid(column=0, row=2, sticky=(N,W,E,S))
        
        self.rectangleLabel = ttk.Label(self.optionFrame, text='Size:', anchor='e', justify='right')
        self.triangleLabel = ttk.Label(self.optionFrame, text='Size:', anchor='e', justify='right')
        self.circleLabel = ttk.Label(self.optionFrame, text='Size:', anchor='e', justify='right')
        
        self.polygonOption = ['50x50', '100x50', '50x100']
        self.radiusOption = ['Radius = 25', 'Radius = 50', 'Radius = 75']
        
        self.rectangleOption = ttk.OptionMenu(self.optionFrame, self.rectangleVal, *self.polygonOption)
        self.triangleOption = ttk.OptionMenu(self.optionFrame, self.triangleVal, *self.polygonOption)
        self.circleOption = ttk.OptionMenu(self.optionFrame, self.circleVal, *self.radiusOption)
        
    def showOption(self):
        print
        
if __name__ == '__main__':
    main = Main()
    main.mainloop()