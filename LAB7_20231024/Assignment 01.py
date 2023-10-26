from tkinter import *
from random import sample

ans = ''.join(sample('1234567890', 4))

def check():
    hintStr = hintGenerate()
    if(hintStr[0] != 4):
        res = Label(window, text="Hint:", justify='center')
        res.grid(row=0, grid=5)
        hint = Label(window, text=hintStr[1], justify='center')
        hint.grid(row=1, grid=5)
        return
    
    res = Label(window, text="*** CORRECT ***", justify='center')
    res.grid(row=0, grid=5)
            
def hintGenerate():
    bull = 0
    cow = 0
    for i in range(0, 4):
        if(ans[i] == entry[i].get()):
            bull += 1
        elif(entry[i] in ans):
            cow += 1
    
    hintStr = "Bulls:{} and Cows:{}".format(bull, cow)
    return (bull, hintStr)

window = Tk()
window.title("Bull and Cow guessing game")
window.geometry("320x120")

message = Label(window, text="Guessing")
message.grid(row=0, column=0)
entry = list()

for i in range(0, 4):
    entry += [Entry(window, width=3)]
    entry[i].grid(row=0, column=i+1)

button = Button(window, text="Submit", command=check)

window.mainloop()