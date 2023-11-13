from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math

class Main(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('270x165')
        self.title('Canvas Drawing')
        
        self.optionSet = [IntVar(), IntVar(), IntVar()]
        
        self.optionVal = [StringVar()]
        self.optionVal += [StringVar()]
        self.optionVal += [StringVar()]
        
        self.currentSet = 0
        self.prevSet = -1
        
        self.mainFrame = ttk.Frame(self, padding=5)
        self.mainFrame.pack(anchor='center', side='top', fill='both', expand=TRUE)
        
        self.optionFrame = ttk.Labelframe(self.mainFrame, text='Drawing Setting')
        self.optionFrame.pack(anchor='center', side='top', fill='none', expand=TRUE, ipadx=5, ipady=5, padx=5, pady=5)
        
        self.drawButton = ttk.Button(self.mainFrame, padding=5, text='Draw', command=self.execute)
        self.drawButton.pack(anchor='center', side='top', fill='none', expand=TRUE)
        
        # Need to declare before self.rectangleTick because it will error at checking phase -- No variable defined.
        self.optionLabel = [ttk.Label(self.optionFrame, text='Size:', anchor='e', justify='right')]
        self.optionLabel += [ttk.Label(self.optionFrame, text='Size:', anchor='e', justify='right')]
        self.optionLabel += [ttk.Label(self.optionFrame, text='Size:', anchor='e', justify='right')]
        
        self.polygonOption = ['', '50x50', '100x50', '50x100']
        self.radiusOption = ['', 'Radius = 25', 'Radius = 50', 'Radius = 75']
        
        self.optionList = [ttk.OptionMenu(self.optionFrame, self.optionVal[0], *self.polygonOption)]
        self.optionList += [ttk.OptionMenu(self.optionFrame, self.optionVal[1], *self.polygonOption)]
        self.optionList += [ttk.OptionMenu(self.optionFrame, self.optionVal[2], *self.radiusOption)]
        
        self.rectangleTick = ttk.Checkbutton(self.optionFrame, text='Rectangle', onvalue=1, offvalue=0, variable=self.optionSet[0], command=self.showOption)
        self.rectangleTick.anchor('w')
        self.rectangleTick.grid(column=0, row=0, sticky=(N,W,E,S))
        
        self.triangleTick = ttk.Checkbutton(self.optionFrame, text='Right Triangle', onvalue=2, offvalue=0, variable=self.optionSet[1], command=self.showOption)
        self.triangleTick.anchor('w')
        self.triangleTick.grid(column=0, row=1, sticky=(N,W,E,S))
        
        self.circleTick = ttk.Checkbutton(self.optionFrame, text='Circle', onvalue=4, offvalue=0, variable=self.optionSet[2], command=self.showOption)
        self.circleTick.anchor('w')
        self.circleTick.grid(column=0, row=2, sticky=(N,W,E,S))
        
    def showOption(self):
        self.currentSet = 0
        for i in range(3):
            self.currentSet += self.optionSet[i].get()
        if(self.prevSet == -1):
            type = self.currentSet
        else:
            type = self.currentSet - self.prevSet
        
        self.prevSet = self.currentSet

        if(type > 0):
            type = int(math.log2(type))
            self.optionLabel[type].grid(column=1, row=type, sticky=(N,W,E,S))
            self.optionList[type].grid(column=2, row=type, sticky=(N,W,E,S))
        elif(type < 0):
            type = abs(type)
            type = int(math.log2(type))
            self.optionLabel[type].grid_forget()
            self.optionList[type].grid_forget()
            
            self.optionVal[type].set('-1')
        else:
            print("Initialize...")
    
    def execute(self):
        
        size = self.check()
        if size:
            return -1
        
        size = self.valueExtract(size)
        res = self.draw(size)
        
    def check(self):
        emptyCheck = 0
        res = list()
        
        for i in range(3):
            temp = self.optionVal[i].get()
            if temp == '':
                messagebox.showerror("Parameter Setting Error",
                                 """
                                 You have empty values.
                                 Please Try again but this time, use your brain
                                 Thank you very much for using our application
                                 """)
                return -1
            elif temp == '-1':
                emptyCheck += 1
            
            else:
                res += [i]
        
        if emptyCheck == 3:
            messagebox.showerror("Parameter Setting Error",
                                 """
                                 You have to select at least one choice from three checkboxes.
                                 Please Try again but this time, use your brain
                                 Thank you very much for using our application
                                 """)
            return -2
        
        return res
    
    def valueExtract(self, str):
        
if __name__ == '__main__':
    main = Main()
    main.mainloop()