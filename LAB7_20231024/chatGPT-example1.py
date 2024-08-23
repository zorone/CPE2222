import random
import tkinter as tk
from tkinter import messagebox

# Function to check Bulls and Cows
def check_bulls_cows(secret_num, guess):
    bulls = cows = 0
    for i in range(len(secret_num)):
        if guess[i] == secret_num[i]:
            bulls += 1
        elif guess[i] in secret_num:
            cows += 1
    return bulls, cows

# Initialize the game
def start_game():
    global secret_number, attempts_left
    secret_number = ''.join(random.sample('0123456789', 4))
    attempts_left = 8
    status_label.config(text="Guess the 4-digit number")
    attempts_label.config(text=f"Attempts left: {attempts_left}")

# Function to handle the guess
def make_guess():
    global attempts_left
    if attempts_left > 0:
        guess = entry.get()
        if len(guess) != 4 or not guess.isdigit():
            messagebox.showerror("Error", "Please enter a 4-digit number")
            entry.delete(0, 'end')
            return

        bulls, cows = check_bulls_cows(secret_number, guess)
        result = f"{bulls} Bulls, {cows} Cows"
        status_label.config(text=result)
        attempts_left -= 1
        attempts_label.config(text=f"Attempts left: {attempts_left}")

        if bulls == 4:
            messagebox.showinfo("Congratulations", "You guessed the number!")
            start_game()

        entry.delete(0, 'end')
    else:
        messagebox.showinfo("Game Over", f"The number was {secret_number}")
        start_game()

# GUI setup
root = tk.Tk()
root.title("Bulls and Cows Game")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

entry = tk.Entry(frame, width=10)
entry.grid(row=0, column=0, padx=5)

guess_button = tk.Button(frame, text="Guess", command=make_guess)
guess_button.grid(row=0, column=1, padx=5)

status_label = tk.Label(root, text="Guess the 4-digit number")
status_label.pack()

attempts_label = tk.Label(root, text="Attempts left: 8")
attempts_label.pack()

start_game()

root.mainloop()