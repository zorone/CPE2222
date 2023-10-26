from tkinter import *
from random import sample

ans = ''.join(sample('1234567890', 4))

def check():
    hintStr = hintGenerate()
    hint.config(text=hintStr[1])
    if(hintStr[0] != 4):
        print(ans)
        res.config(text="Hint:")

    else:
        res.config(text="*** CORRECT ***")
        hint.config(text=" "*20)

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
frame.pack(anchor='center', side='bottom', fill='both')

message = Label(frame, text="Guessing:")
message.pack(side='left')
entry = list()

for i in range(0, 4):
    entry += [Entry(frame, width=3)]
    entry[i].pack(side='left')

button = Button(frame, text="Submit", padx=2, command=check)
button.pack(anchor='center', side='left', fill='x')

res = Label(frame, text="", padx=2, justify='center')
hint = Label(frame, text="", padx=2, justify='center')
res.pack(anchor='center', side='left')
hint.pack(anchor='e', side='bottom', fill='x')

window.mainloop()