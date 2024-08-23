from tkinter import *
from random import sample

window = Tk()
window.title("Bull and Cow guessing game")
window.geometry("360x80")  # กว้าง x สูง

L = Label(window, text=" ")
L1 = Label(window, text="Guessing:")
L2 = Label(window, text="   ")
L3 = Label(window, text="   ")
L4 = Label(window, text="   ")
L.grid(row=0, column=0)
L1.grid(row=1, column=1)
L2.grid(row=1, column=6)
L3.grid(row=1, column=0)
L4.grid(row=1, column=8)

e = [Entry(window, width=3)]
e += [Entry(window, width=3)]
e += [Entry(window, width=3)]
e += [Entry(window, width=3)]
e[0].grid(row=1, column=2)
e[1].grid(row=1, column=3)
e[2].grid(row=1, column=4)
e[3].grid(row=1, column=5)

b = Button(window, text="Submit")
b.grid(row=1, column=7)

secret_number = ''.join(sample('0123456789', 4))  # เลขลับที่คุณจะต้องการให้ผู้เล่นทาย
guessed_correctly = False  # สร้างตัวแปรเพื่อตรวจสอบว่าทายถูกหรือยัง

def check_guess():
    global guessed_correctly
    if guessed_correctly:
        return

    guess = e[0].get() + e[1].get() + e[2].get() + e[3].get()
    bulls = sum(1 for i in range(4) if guess[i] == secret_number[i])
    cows = sum(1 for digit in guess if digit in secret_number) - bulls
    result_label.config(text=f"Hint:")
    result_label2.config(text=f"Bulls: {bulls} and Cows: {cows}")
    if bulls == 4:
        result_label.config(text="**CORRECT**")
        result_label2.config(text="")
        guessed_correctly = True  # ทายถูกแล้ว
    
result_label = Label(window, text="")
result_label.grid(row=1, column=9)
result_label2 = Label(window, text="")
result_label2.grid(row=2, column=9)
print(secret_number)
b.config(command=check_guess)

window.mainloop()
