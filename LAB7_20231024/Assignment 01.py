from tkinter import *
from random import sample

ans = ''.join(sample('1234567890', 4))

def check():
    secondLine.grid()
    hintStr = hintGenerate()
    if(hintStr[0] != 4):
        resStr = "Hint:"
        
    else:
        resStr = "*** CORRECT ***"
        hintStr[1] = ''
        
    res = Label(firstLine, text=resStr, padx=2, justify='center')
    res.grid(row=1, column=6)
    hint = Label(secondLine, text=hintStr[1], padx=2, justify='center')
    hint.grid(row=2, column=6)
            
def hintGenerate():
    bull = 0
    cow = 0
    for i in range(0, 4):
        temp = entry[i].get()
        if(ans[i] == temp):
            bull += 1
        elif(temp in ans):
            cow += 1
    
    hintStr = "Bulls:{} and Cows:{}".format(bull, cow)
    return (bull, hintStr)

window = Tk()
window.title("Bull and Cow guessing game")
window.geometry("320x100")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

frame = Frame(window, border=3)
frame.anchor('center')
frame.grid(sticky=(N, W, E, S))

firstLine = Frame(frame, height=4)
firstLine.grid()
message = Label(firstLine, text="Guessing:")
message.grid(row=1, column=0)
entry = list()

for i in range(0, 4):
    entry += [Entry(firstLine, width=3)]
    entry[i].grid(row=1, column=i+1)

button = Button(firstLine, text="Submit", padx=2, command=check)
button.grid(row=1, column=5)

secondLine = Frame(frame, height=4)

window.mainloop()