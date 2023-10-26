from tkinter import *
from random import sample

window = Tk()
window.title("Bull and Cow guessing game")
window.geometry("480x80")

message = [Label(window, text="Guessing")]
entry = [Entry(window, width=3)]
entry = entry*4

window.mainloop()