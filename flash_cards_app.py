import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect("flashcards.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS flashcards (
                        id INTEGER PRIMARY KEY,
                        category TEXT,
                        question TEXT,
                        answer TEXT)''')
    conn.commit()
    conn.close()

# Add Flashcard to Database
def add_flashcard():
    category = entry_category.get()
    question = entry_question.get("1.0", tk.END).strip()
    answer = entry_answer.get("1.0", tk.END).strip()

    if not category or not question or not answer:
        messagebox.showerror("Error", "All fields are required!")
        return

    conn = sqlite3.connect("flashcards.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO flashcards (category, question, answer) VALUES (?, ?, ?)", 
                   (category, question, answer))
    conn.commit()
    conn.close()

    entry_category.delete(0, tk.END)
    entry_question.delete("1.0", tk.END)
    entry_answer.delete("1.0", tk.END)
    messagebox.showinfo("Success", "Flashcard added successfully!")

# Test Flashcards Interface
def start_testing():
    conn = sqlite3.connect("flashcards.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flashcards")
    flashcards = cursor.fetchall()
    conn.close()

    if not flashcards:
        messagebox.showinfo("Info", "No flashcards available to test!")
        return

    testing_window = tk.Toplevel(root)
    testing_window.title("Flashcard Testing")
    testing_window.geometry("400x300")

    # State variables to iterate through flashcards
    flashcard_index = {"current": 0}

    def show_next_flashcard():
        if flashcard_index["current"] >= len(flashcards):
            messagebox.showinfo("Info", "You've gone through all the flashcards!")
            testing_window.destroy()
            return

        flashcard = flashcards[flashcard_index["current"]]
        question_label.config(text=f"Question: {flashcard[2]}")
        answer_label.config(text="")  # Hide the answer initially
        flashcard_index["current"] += 1

    def show_answer():
        flashcard = flashcards[flashcard_index["current"] - 1]
        answer_label.config(text=f"Answer: {flashcard[3]}")

    # Question display
    question_label = tk.Label(testing_window, text="Question:", font=("Arial", 14, "bold"))
    question_label.pack(pady=20)

    # Answer display
    answer_label = tk.Label(testing_window, text="", font=("Arial", 12))
    answer_label.pack(pady=10)

    # Buttons for actions
    button_show_answer = tk.Button(testing_window, text="Show Answer", command=show_answer)
    button_show_answer.pack(pady=5)

    button_next = tk.Button(testing_window, text="Next Flashcard", command=show_next_flashcard)
    button_next.pack(pady=5)

    # Start with the first flashcard
    show_next_flashcard()

# GUI Setup
root = tk.Tk()
root.title("Flashcard App")
root.geometry("400x400")

# Labels and Entries for Adding Flashcards
label_category = tk.Label(root, text="Category:")
label_category.grid(row=0, column=0, padx=10, pady=10)
entry_category = tk.Entry(root, width=30)
entry_category.grid(row=0, column=1, padx=10, pady=10)

label_question = tk.Label(root, text="Question:")
label_question.grid(row=1, column=0, padx=10, pady=10)
entry_question = tk.Text(root, width=30, height=5)
entry_question.grid(row=1, column=1, padx=10, pady=10)

label_answer = tk.Label(root, text="Answer:")
label_answer.grid(row=2, column=0, padx=10, pady=10)
entry_answer = tk.Text(root, width=30, height=5)
entry_answer.grid(row=2, column=1, padx=10, pady=10)

# Buttons
button_add = tk.Button(root, text="Add Flashcard", command=add_flashcard)
button_add.grid(row=3, column=0, columnspan=2, pady=10)

button_test = tk.Button(root, text="Test Flashcards", command=start_testing)
button_test.grid(row=4, column=0, columnspan=2, pady=10)

# Run Database Setup
setup_database()

# Run the GUI
root.mainloop()
