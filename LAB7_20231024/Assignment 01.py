from tkinter import *
from random import sample

ans = ''.join(sample('1234567890', 4))

def check():
    hintStr = hintGenerate()
    if(hintStr[0] != 4):
        print(ans)
        res = Label(window, text="Hint:", padx=2, justify='center')
        res.grid(row=1, column=9)

    else:
        res = Label(window, text="*** CORRECT ***", padx=2, justify='center')
        res.grid(row=1, column=9)
        hintStr[1] = ""

    hint = Label(window, text=hintStr[1], padx=2, justify='center')
    hint.grid(row=2, column=9)
    
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

padding = Label(window, text=" ")
buttonPadding = Label(window, text="  ")

padding.grid(row=0, column=0)

message = Label(window, text="Guessing:")
message.grid(row=1, column=0)
entry = list()

for i in range(0, 4):
    entry += [Entry(window, width=3)]
    entry[i].grid(row=1, column=i+1)

buttonPadding.grid(row=1, column=6)

button = Button(window, text="Submit", padx=2, command=check)
button.grid(row=1, column=7)

buttonPadding.grid(row=1, column=8)

padding.grid(row=3, column=0)

window.mainloop()