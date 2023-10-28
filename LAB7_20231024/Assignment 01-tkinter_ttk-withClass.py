from tkinter import *
import tkinter as tk
from tkinter import ttk
from random import sample

class Main(tk.Tk):
    def __init__(self, ):
        super().__init__()
        self.title("Bull and Cow guessing game")
        self.geometry("360x80")
        
        self.style = ttk.Style()
        
        self.mainFrame = ttk.Frame(self, padding=5)
        self.mainFrame.anchor('center')
        self.mainFrame.grid(row=0, column=0, sticky=(N,W,E,S))
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.label = ttk.Label(self.mainFrame, text="Guessing:")
        self.label.grid(column=0, row=0, sticky=E)
        
        self.entry = list()
        for i in range(0, 4):
            entry += (ttk.Entry(self.mainFrame, width=3), )
            entry[i].grid(row=0, column=i+1, sticky=(W,E))
        
        self.button = ttk.Button(self.mainFrame, padding=2, text="Submit", sticky=(W,E), command=self.check)
        self.button.grid(row=0, column=5)
        
        self.res = ttk.Label(self.mainFrame, anchor='center', text='')
        self.hint = ttk.Label(self.mainFrame, anchor='center', text='')
        
        
    
    def check(self):
        for e in self.entry:
            if(e.get() in '0123456789'):
                print('pass')
            else:
                self.res.config(text='ERROR!!!')
                

if __name__ == "__main__":
    main = Main()
    main.mainloop()