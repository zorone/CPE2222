from tkinter import *
from random import sample

ans = ''.join(sample('1234567890', 4))

def check():
    hintStr = hintGenerate()
    if(hintStr[0] != 4):
        print(ans)
        res = Label(frame, text="Hint:", justify='center')
        res.grid(row=0, column=6)
        hint = Label(frame, text=hintStr[1], justify='center')
        hint.grid(row=1, column=6)
        return
    
    res = Label(frame, text="*** CORRECT ***", justify='center')
    res.grid(row=0, column=6)
            
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
window.geometry("320x120")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

frame = Frame(window)
frame.anchor('center')
frame.grid()

message = Label(frame, text="Guessing:")
message.grid(row=0, column=0)
entry = list()

for i in range(0, 4):
    entry += [Entry(frame, width=3)]
    entry[i].grid(row=0, column=i+1)


buttonFrame = Frame(frame, width=10)
buttonFrame.anchor('center')
buttonFrame.grid(row=0, column=5, columnspan=3)
button = Button(buttonFrame, text="Submit", command=check)
button.grid(row=0, column=1)

window.mainloop()