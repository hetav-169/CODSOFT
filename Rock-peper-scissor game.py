from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("500x500")
root.config(bg="#1e1e1e")

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_label.config(text="Your Choice: " + user_choice)
    computer_label.config(text="Computer Choice: " + computer_choice)

    if user_choice == computer_choice:
        result_label.config(text="It's a Draw!", fg="yellow")

    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):

        user_score += 1
        result_label.config(text="You Win!", fg="#00ff99")

    else:
        computer_score += 1
        result_label.config(text="Computer Wins!", fg="#ff4d4d")

    score_label.config(
        text=f"Your Score: {user_score}    Computer Score: {computer_score}"
    )

def restart_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    user_label.config(text="")
    computer_label.config(text="")
    result_label.config(text="Game Restarted", fg="white")

    score_label.config(
        text="Your Score: 0    Computer Score: 0"
    )

title = Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="#00ff99"
)
title.pack(pady=20)

user_label = Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)
user_label.pack()

computer_label = Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)
computer_label.pack()

result_label = Label(
    root,
    text="Choose Rock, Paper or Scissors",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e",
    fg="yellow"
)
result_label.pack(pady=15)

score_label = Label(
    root,
    text="Your Score: 0    Computer Score: 0",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="#4da6ff"
)
score_label.pack(pady=10)

rock_btn = Button(
    root,
    text="Rock",
    width=20,
    bg="#ff4d4d",
    fg="white",
    font=("Arial", 11, "bold"),
    command=lambda: play("Rock")
)
rock_btn.pack(pady=5)

paper_btn = Button(
    root,
    text="Paper",
    width=20,
    bg="#4da6ff",
    fg="white",
    font=("Arial", 11, "bold"),
    command=lambda: play("Paper")
)
paper_btn.pack(pady=5)

scissors_btn = Button(
    root,
    text="Scissors",
    width=20,
    bg="#33cc33",
    fg="white",
    font=("Arial", 11, "bold"),
    command=lambda: play("Scissors")
)
scissors_btn.pack(pady=5)

restart_btn = Button(
    root,
    text="Restart Game",
    width=20,
    bg="#ffaa00",
    fg="black",
    font=("Arial", 11, "bold"),
    command=restart_game
)
restart_btn.pack(pady=15)

exit_btn = Button(
    root,
    text="Exit",
    width=20,
    bg="#cc0000",
    fg="white",
    font=("Arial", 11, "bold"),
    command=root.destroy
)
exit_btn.pack(pady=5)

root.mainloop()