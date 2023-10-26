from tkinter import *
from random import sample

window = Tk()
window.title("Bull and Cow guessing game")
window.geometry("240x80")

message = [Label(window, text="Guessing")]
entry = list()

frame = Frame()

for i in range(0, 4):
    entry += [Entry(window, width=3)]
    entry[i].grid(row=0, column=i+2)

window.mainloop()