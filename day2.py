import tkinter as tk
from time import strftime, localtime
from itertools import cycle

root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")

# Colors for gradient animation
colors = cycle(['#FF6347', '#FF4500', '#FF7F50', '#FF8C00', '#000000', '#CCCCCC', '#CCFF56'])

def update_time():
    current_time = strftime('%H:%M:%S %p', localtime())
    label.config(text=current_time)
    label.after(1000, update_time)

def change_bg():
    label.config(bg=next(colors))
    label.after(1000, change_bg)

label = tk.Label(root, font=('Helvetica', 40, 'bold'), fg='white')
label.pack(anchor='center', fill='both', expand=True)

update_time()
change_bg()
root.mainloop()
