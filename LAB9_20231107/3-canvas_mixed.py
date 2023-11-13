from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math

class Main(Tk):
    def __init__(self):
        self.geometry('270x165')
        self.title('Canvas Drawing')
        
        self.mainFrame = ttk.Frame(self, padding=5)
        self.mainFrame.pack(anchor='center', side='top', fill='both', expand=TRUE)
        
        self.optionFrame = ttk.Labelframe(self.mainFrame, padding=5, text='Drawing Setting')
        self.optionFrame.pack(anchor='center', side='top', fill='both', expand=TRUE)
        
        self.drawButton = ttk.button(self.mainFrame, padding=5, )
        
if __name__ == '__main__':
    main = Main()
    main.mainloop()
    
size = [[50, 50], [50, 100], 75, ]
if(size[0][0])