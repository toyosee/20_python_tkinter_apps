import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Quiz Game")
root.geometry("500x300")

# Questions and answers
questions = [
    ("What is the capital of France?", "Paris", ["Paris", "London", "Berlin", "Madrid"]),
    ("What is the largest planet in our solar system?", "Jupiter", ["Mars", "Earth", "Jupiter", "Saturn"]),
    ("What element does 'O' represent on the periodic table?", "Oxygen", ["Gold", "Oxygen", "Silver", "Hydrogen"]),
    ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee", ["J.K. Rowling", "Ernest Hemingway", "Harper Lee", "Jane Austen"])
]

random.shuffle(questions)  # Shuffle the questions randomly
question_index = 0
score = 0

def next_question():
    global question_index
    if question_index < len(questions):
        question_label.config(text=questions[question_index][0])
        for i, option in enumerate(options):
            option.config(text=questions[question_index][2][i])
    else:
        show_score()

def check_answer(selected_option):
    global question_index, score
    if selected_option == questions[question_index][1]:
        score += 1
    question_index += 1
    next_question()

def show_score():
    response = messagebox.askquestion("Quiz Completed", f"Your score: {score}/{len(questions)}\n\nDo you want to retake the test?", icon='info')
    if response == 'yes':
        retake_test()
    else:
        root.quit()

def retake_test():
    global question_index, score
    random.shuffle(questions)  # Reshuffle the questions for a new attempt
    question_index = 0
    score = 0
    next_question()

# Display question
question_label = tk.Label(root, text="", font=('Helvetica', 18, 'bold'), wraplength=400)
question_label.pack(pady=20)

# Display options
options = []
for i in range(4):
    btn = tk.Button(root, text="", font=('Helvetica', 14), width=20, command=lambda i=i: check_answer(options[i].cget('text')))
    btn.pack(pady=5)
    options.append(btn)

next_question()
root.mainloop()
