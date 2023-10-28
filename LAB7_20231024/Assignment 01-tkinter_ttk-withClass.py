from tkinter import *
import tkinter as tk
from tkinter import ttk
from random import sample

class Main(tk.Tk):
    def __init__(self, ):
        super().__init__()
        self.title("Bull and Cow guessing game")
        self.geometry("400x80")
        
        self.style = ttk.Style()
        
        self.ans = ''.join(sample('0123456789', 4))
        self.bull = 0
        self.cow = 0
        
        self.mainFrame = ttk.Frame(self, padding=5)
        self.mainFrame.anchor('center')
        self.mainFrame.grid(row=0, column=0, sticky=(N,W,E,S))
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.label = ttk.Label(self.mainFrame, text="Guessing:")
        self.label.grid(column=0, row=0, sticky=E)
        
        self.entry = list()
        for i in range(0, 4):
            self.entry += (ttk.Entry(self.mainFrame, width=3), )
            self.entry[i].grid(row=0, column=i+1, sticky=(W,E))
        
        self.button = ttk.Button(self.mainFrame, padding=2, text="Submit", command=self.check)
        self.button.grid(row=0, column=5, sticky=(W,E))
        
        self.res = ttk.Label(self.mainFrame, anchor='center', text='')
        self.hint = ttk.Label(self.mainFrame, anchor='center', text='')
        self.res.grid(row=0, column=6)
        self.hint.grid(row=1, column=6)
    
    def check(self):
        self.test = '0123456789'
        
        for i, e in enumerate(self.entry):
            val = e.get()
            if(val == ''):
                self.res.config(text='ERROR!!!')
                self.hint.config(text='Input value is empty')
                break
            elif(self.isNotRepeat(e)):
                self.hintCount(e, i)
                self.generateHint()
            elif(self.isNum(e)):
                break
            else:
                self.res.config(text='ERROR!!!')
                self.hint.config(text='Input value not implement')
                break

    def isNotRepeat(self, val):
        if val in self.test:
            self.test = self.test.replace(val, '')
            return True
        self.res.config(text='ERROR!!!')
        self.hint.config(text='Duplicate Input value')
        return False
    
    def isNum(self, val):
        if val in '0123456789':
            return True
        return False

    def hintCount(self, val, index):
        if val == self.ans[index]:
            self.bull += 1
        elif val in self.ans:
            self.cow += 1

    def generateHint(self):
        if self.bull == 4:
            self.res.config(text="*** CORRECT ***")
            self.hint.config(text='')
            return
        self.res.config(text="Hint:")
        self.hint.config(text=f"Bulls:{self.bull} and Cows:{self.cow}")

if __name__ == "__main__":
    main = Main()
    main.mainloop()