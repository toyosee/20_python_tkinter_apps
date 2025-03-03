# Need an interface to enter text
# Need a button to trigger display
# Label to show text

# A simple Helloworld Tkinter program

import tkinter as tk

# display function
def display():
    entry = myEntry.get().strip()
    myLabel.config(text=entry)

    myEntry.delete(0, tk.END)

root = tk.Tk()
root.title("Hello World Program")
root.geometry("400x400")


description = tk.Label(root, text="Enter a message")
description.pack(pady=10)
# Create an input widget
myEntry = tk.Entry(root)
myEntry.pack(pady=5)

# Create a button widget
myButton = tk.Button(root, text="Display", command = display)
myButton.pack(pady=10)
# Create a label widget
myLabel = tk.Label(root, text="", font=30, foreground="green")
myLabel.pack(pady=10)

root.mainloop()