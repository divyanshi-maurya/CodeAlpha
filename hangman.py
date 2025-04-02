import tkinter as tk
import random
from tkinter import messagebox

# Word list
WORDS = ["PYTHON", "JAVA", "HANGMAN", "PROGRAM", "DEVELOPER", "CODING", "COMPUTER"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("400x400")
        self.root.configure(bg="#F5F5DC")  # Light Beige Background
        
        self.word = random.choice(WORDS)
        self.word_display = ["_" for _ in self.word]
        self.guessed_letters = set()
        self.remaining_attempts = 6
        
        self.label_word = tk.Label(root, text=" ".join(self.word_display), font=("Arial", 24), bg="#F5F5DC", fg="#2E4053")
        self.label_word.pack(pady=20)
        
        self.label_attempts = tk.Label(root, text=f"Attempts left: {self.remaining_attempts}", font=("Arial", 14), bg="#F5F5DC", fg="#B22222")
        self.label_attempts.pack()
        
        self.entry_letter = tk.Entry(root, font=("Arial", 14), width=5, justify='center')
        self.entry_letter.pack(pady=10)
        self.entry_letter.bind("<Return>", self.check_letter)
        
        self.button_guess = tk.Button(root, text="Guess", font=("Arial", 14), bg="#008CBA", fg="white", command=self.check_letter)
        self.button_guess.pack(pady=5)
        
        self.label_message = tk.Label(root, text="", font=("Arial", 12), bg="#F5F5DC", fg="#2E4053")
        self.label_message.pack()
    
    def check_letter(self, event=None):
        letter = self.entry_letter.get().upper()
        self.entry_letter.delete(0, tk.END)
        
        if not letter.isalpha() or len(letter) != 1:
            self.label_message.config(text="Invalid input! Enter a single letter.", fg="#FF5733")
            return
        
        if letter in self.guessed_letters:
            self.label_message.config(text="You already guessed this letter!", fg="#FF8C00")
            return
        
        self.guessed_letters.add(letter)
        
        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.word_display[i] = letter
            self.label_word.config(text=" ".join(self.word_display))
        else:
            self.remaining_attempts -= 1
            self.label_attempts.config(text=f"Attempts left: {self.remaining_attempts}")
        
        if "_" not in self.word_display:
            messagebox.showinfo("Hangman", "Congratulations! You guessed the word!")
            self.root.quit()
        elif self.remaining_attempts == 0:
            messagebox.showerror("Hangman", f"Game Over! The word was: {self.word}")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()