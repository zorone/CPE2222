from tkinter import *
from random import sample

ans = ''.join(sample('1234567890', 4))

def check():
    hintStr = hintGenerate()
    if(hintStr[0] != 4):
        print(ans)
        res.config(text="Hint:")

    else:
        res.config(text="  *** CORRECT ***")
        hintStr[1] = ""

    hint.config(text=hintStr[1])
    
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
    return [bull, hintStr]

window = Tk()
window.title("Bull and Cow guessing game")
window.geometry("360x80")

padding = list()
rowIndex = (0, 1, 1, 1)
columnIndex = (0, 0, 6, 8)

message = Label(window, text="Guessing:")
message.grid(row=1, column=1)
entry = list()

for i in range(0, 4):
    padding += [Label(window, text="  ")]
    entry += [Entry(window, width=3)]
    
    padding[i].grid(row=rowIndex[i], column=columnIndex[i])
    entry[i].grid(row=1, column=i+2)

button = Button(window, text="Submit", command=check)
button.grid(row=1, column=7)

res = Label(window, text="", justify='center')
hint = Label(window, text="", justify='center')

res.grid(row=1, column=9)
hint.grid(row=2, column=9)

window.mainloop()