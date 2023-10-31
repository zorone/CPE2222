from tkinter import *
from tkinter import ttk

class Main(Tk):
    def __init__(self, ):
        super().__init__()
        
        self.title("CPE2222")
        self.style = ttk.Style()
        
        self.mainFrame = ttk.Frame(self, padding=5)
        self.mainFrame.pack()
        
        self.calcOption = ttk.Labelframe(self.mainFrame, padding=5, text='Calculation')
        self.calcOption.pack()
        
        self.calcEntry = ["Area of Rectangle", "Area of Triangle", "Pythagorean"]
        self.calcSelected = IntVar()
        
        for i, title in enumerate(self.calcEntry):
            self.calcEntry[i] = ttk.Radiobutton(self.calcOption, text=title, value=i, variable=self.calcSelected)
            self.calcEntry[i].pack()

if __name__ == "__main__":
    main = Main()
    main.mainloop()