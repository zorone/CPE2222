from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Main(Tk):
    def __init__(self):
        self.geometry('270x165')
        self.title('Canvas Drawing')
        
        self.mainFrame = ttk.Frame(self, padding=5)
        self.mainFrame.pack(anchor='center', side='top')
        
        self.optionFrame = ttk.Labelframe(self.mainFrame, padding=5, text='Drawing Setting')
        self.optionFrame.pack()
        
if __name__ == '__main__':
    main = Main()
    main.mainloop()