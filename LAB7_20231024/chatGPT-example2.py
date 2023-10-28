import random
import tkinter as tk
from tkinter import messagebox

class BullsAndCowsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Bulls and Cows Game")
        self.secret_number = ''
        self.attempts_left = 8

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.entry = tk.Entry(self.frame, width=10)
        self.entry.grid(row=0, column=0, padx=5)

        self.guess_button = tk.Button(self.frame, text="Guess", command=self.make_guess)
        self.guess_button.grid(row=0, column=1, padx=5)

        self.status_label = tk.Label(self.root, text="Guess the 4-digit number")
        self.status_label.pack()

        self.attempts_label = tk.Label(self.root, text=f"Attempts left: {self.attempts_left}")
        self.attempts_label.pack()

        self.start_game()

    def check_bulls_cows(self, secret_num, guess):
        bulls = cows = 0
        for i in range(len(secret_num)):
            if guess[i] == secret_num[i]:
                bulls += 1
            elif guess[i] in secret_num:
                cows += 1
        return bulls, cows

    def start_game(self):
        self.secret_number = ''.join(random.sample('0123456789', 4))
        self.attempts_left = 8
        self.status_label.config(text="Guess the 4-digit number")
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")

    def make_guess(self):
        if self.attempts_left > 0:
            guess = self.entry.get()
            if len(guess) != 4 or not guess.isdigit():
                messagebox.showerror("Error", "Please enter a 4-digit number")
                self.entry.delete(0, 'end')
                return

            bulls, cows = self.check_bulls_cows(self.secret_number, guess)
            result = f"{bulls} Bulls, {cows} Cows"
            self.status_label.config(text=result)
            self.attempts_left -= 1
            self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")

            if bulls == 4:
                messagebox.showinfo("Congratulations", "You guessed the number!")
                self.start_game()

            self.entry.delete(0, 'end')
        else:
            messagebox.showinfo("Game Over", f"The number was {self.secret_number}")
            self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = BullsAndCowsGame(root)
    root.mainloop()
