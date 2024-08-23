# https://stackoverflow.com/a/67306226

from tkinter import *

root = Tk()


def clear():
    label.config(text='')


def change():
    label.config(text='changed text')


label = Label(text='default text')
buttonA = Button(root, text='clear text', command=clear)
buttonB = Button(root, text='change text', command=change)

label.pack()
buttonA.pack()
buttonB.pack()

root.mainloop()