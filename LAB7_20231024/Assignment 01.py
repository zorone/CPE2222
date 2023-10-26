from tkinter import *
from random import sample

ans = ''.join(sample('1234567890', 4))

def check():
    resFrame.grid()
    hintStr = hintGenerate()
    if(hintStr[0] != 4):
        print(res)
        res = Label(resFrame, text="Hint:", justify='center')
        res.grid(row=1, column=6)
        hint = Label(resFrame, text=hintStr[1], justify='center')
        hint.grid(row=2, column=6)
        return
    
    hintStr = ''
    res = Label(resFrame, text="*** CORRECT ***", justify='center')
    res.grid(row=1, column=6)
            
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

frame = Frame(window, border=3)
frame.anchor('center')
frame.grid(sticky=(N, W, E, S))

displayFrame = Frame(frame, height=4)
displayFrame.anchor('w')
displayFrame.grid()
message = Label(displayFrame, text="Guessing:")
message.grid(row=1, column=0)
entry = list()

for i in range(0, 4):
    entry += [Entry(displayFrame, width=3)]
    entry[i].grid(row=1, column=i+1)


buttonFrame = Frame(frame, width=10, height=4)
buttonFrame.anchor('center')
buttonFrame.grid()
button = Button(buttonFrame, text="Submit", command=check)
button.grid(row=1, column=0)

resFrame = Frame(frame, height=4)
resFrame.anchor('e')

window.mainloop()