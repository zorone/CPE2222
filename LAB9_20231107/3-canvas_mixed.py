from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math

class Main(Tk):
    def __init__(self):
        self.geometry('270x165')
        self.title('Canvas Drawing')
        
        self.rectangleSet = 0
        self.triangleSet = 0
        self.circleSet = 0
        
        self.mainFrame = ttk.Frame(self, padding=5)
        self.mainFrame.pack(anchor='center', side='top', fill='both', expand=TRUE)
        
        self.optionFrame = ttk.Labelframe(self.mainFrame, text='Drawing Setting')
        self.optionFrame.pack(anchor='center', side='top', fill='both', expand=TRUE, ipad=5, ipady=5, padx=5, pady=5)
        
        self.drawButton = ttk.Button(self.mainFrame, padding=5, text='Draw')
        self.drawButton.pack(anchor='center', side='top', fill='both', expand=TRUE)
        
        self.rectangleTick = ttk.Checkbutton(self.optionFrame, name='Rectangle', onvalue=1, offvalue=0, variable=self.rectangleSet)
        
if __name__ == '__main__':
    main = Main()
    main.mainloop()