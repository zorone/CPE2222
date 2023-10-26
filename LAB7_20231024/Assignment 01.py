from tkinter import *
from random import sample

window = Tk()
window.title("Bull and Cow guessing game")
window.geometry("320x120")

message = [Label(window, text="Guessing")]
entry = list()

frame = Frame(window, borderwidth=5)
frame.grid(column=0, row=0, sticky=(N, W, E, S))

for i in range(0, 4):
    entry += [Entry(frame, width=3)]
    entry[i].grid(row=0, column=i+2)

window.mainloop()