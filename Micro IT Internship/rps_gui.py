import tkinter as tk
import random

# Game logic
def play(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")

# Setup main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x300")
window.resizable(False, False)

# Title label
title = tk.Label(window, text="Rock-Paper-Scissors", font=("Arial", 20, "bold"))
title.pack(pady=10)

# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play('rock'))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play('paper'))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play('scissors'))
scissors_btn.grid(row=0, column=2, padx=10)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=20)

# Run the GUI
window.mainloop()
