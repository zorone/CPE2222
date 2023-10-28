from tkinter import *
from tkinter import tk
from tkinter import ttk
from random import sample

class Main(tk.Tk):
    def __init__(self):
        self.title("Bull and Cow guessing game")
        self.geometry("360x80")
        
        self.mainFrame = ttk.Frame(self, padding=5)
        self.mainFrame.grid(column=0, row=0, sticky=(N,W,E,S))
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

if __name__ == "__main__":
    main = Main()
    main.mainloop()