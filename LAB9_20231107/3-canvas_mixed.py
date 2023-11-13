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
        
        self.optionVal = [StringVar(value='-1')]
        self.optionVal += [StringVar(value='-1')]
        self.optionVal += [StringVar(value='-1')]
        
        self.currentSet = 0
        self.prevSet = -1
        
        self.mainFrame = ttk.Frame(self, padding=5)
        self.mainFrame.pack(anchor='center', side='top', fill='both', expand=TRUE)
        
        self.optionFrame = ttk.Labelframe(self.mainFrame, text='Drawing Setting')
        self.optionFrame.pack(anchor='center', side='top', fill='none', expand=TRUE, ipadx=5, ipady=5, padx=5, pady=5)
        
        self.drawButton = ttk.Button(self.mainFrame, padding=5, text='Draw', command=self.execute)
        self.drawButton.pack(anchor='center', side='top', fill='none', expand=TRUE)
        
        self.frameWidth = -1
        self.frameHight = -1
        
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
            self.optionVal[type].set('')
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
        
        pos = self.check()
        if type(pos) != type(list()):
            return -1
        
        self.paramGenerate()
        res = self.draw(pos)
        
    def check(self):
        emptyCheck = 0
        res = [0]
        
        self.strList = ['']
        
        for i in range(3):
            temp = self.optionVal[i].get()
            if temp == '':
                message = "You have set empty values.\n"
                message += "Please Try again but this time, use your brain\n"
                message += "Thank you very much for using our application"
                messagebox.showerror(title = "Parameter Setting Error",
                                 message = message)
                return -1
            elif temp == '-1':
                emptyCheck += 1
            
            else:
                res[0] += 1
                res += [i]
                self.strList += [temp]
        
        if emptyCheck == 3:
            message = "You have to select at least one choice from three checkboxes.\n"
            message += "Please Try again but this time, use your brain\n"
            message += "Thank you very much for using our application"
            messagebox.showerror(title = "Parameter Setting Error",
                                 message = message)
            return -2
        
        return res
    
    def paramGenerate(self):
        self.frameWidth = 0
        self.frameHeight = 0
        
        for (i, s) in enumerate(self.strList[1:]):
            j = i+1
            length = 0
            height = 0
            if s[0] == 'R':
                self.strList[j] = [int(s[9:])]
                
                temp = 2*self.strList[j][0]
                self.frameWidth += temp + 20
                
                if(self.frameHeight < temp):
                    self.frameHeight = temp
            else:
                for count, ch in enumerate(s):
                    if ch != 'x': continue
                    length = int(s[0:count])
                    height = int(s[count+1:])
                    self.strList[j] = [length, height]
                    
                    self.frameWidth += self.strList[j][0] + 20
                    
                    if(self.frameHeight < self.strList[j][1]):
                        self.frameHeight = self.strList[j][1]
                    break
        self.frameWidth += 20
        self.frameHeight += 40

    def draw(self, pos):
        print(locals())
        if(self.canvasWindow in self.__dir__ and self.canvasWindow.winfo_exists()):
             self.canvasWindow.destroy()
        
        self.canvasWindow = Toplevel()
        self.canvasWindow.title("RESULT")
        
        self.canvas = Canvas(self.canvasWindow, bg="white", width=self.frameWidth, height=self.frameHeight)
        self.canvas.grid(row=0, column=0, sticky=(N,W,E,S))
        
        self.canvasCloseButton = ttk.Button(self.canvasWindow, text="Close Window", padding=5, command=self.canvasWindow.destroy)
        self.canvasCloseButton.grid(row=1, column=0, sticky=(N,W,E,S))
        
        offset = 20
        next = -1
        
        for i in range(1, pos[0]+1):
            next = offset + self.strList[i][0]
            if pos[i] == 0:
                self.canvas.create_rectangle(offset, 20,
                                             next, 20 + self.strList[i][1],
                                             fill="red", outline="black")
            elif pos[i] == 1:
                self.canvas.create_polygon(offset, 20,
                                           next, 20,
                                           next, 20 + self.strList[i][1],
                                           fill="blue", outline="black")
                
            elif pos[i] == 2:
                next += self.strList[i][0]
                self.canvas.create_oval(offset, 20,
                                        next, 20 + (2*self.strList[i][0]),
                                        fill="yellow", outline="black")
                
            offset = next + 20
            
        return self.canvasWindow

if __name__ == '__main__':
    main = Main()
    main.mainloop()