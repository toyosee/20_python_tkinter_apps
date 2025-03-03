import tkinter as tk
from tkinter import colorchooser, messagebox
from PIL import ImageGrab

root = tk.Tk()
root.title("Digital Art Board")
root.geometry("600x400")

# Default brush settings
brush_color = "black"
brush_size = 2

def change_color():
    global brush_color
    color = colorchooser.askcolor()[1]
    if color:
        brush_color = color

def change_size(new_size):
    global brush_size
    brush_size = new_size

def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)

def save_as_png():
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    ImageGrab.grab().crop((x, y, x1, y1)).save("sketch.png")
    messagebox.showinfo("Export", "Sketch saved as sketch.png")

def exit_app():
    root.quit()

# Create canvas
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)
canvas.bind("<B1-Motion>", paint)

# Create control frame
control_frame = tk.Frame(root, padx=5, pady=5)
control_frame.pack(side=tk.TOP, fill=tk.X)

# Color button
color_button = tk.Button(control_frame, text="Change Color", command=change_color)
color_button.pack(side=tk.LEFT, padx=5, pady=5)

# Brush size buttons
size_label = tk.Label(control_frame, text="Brush Size")
size_label.pack(side=tk.LEFT, padx=5)

sizes = [2, 4, 6, 8, 10]
for size in sizes:
    size_button = tk.Button(control_frame, text=str(size), command=lambda size=size: change_size(size))
    size_button.pack(side=tk.LEFT, padx=5)

# Exit button
exit_button = tk.Button(control_frame, text="Exit", command=exit_app)
exit_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Export button
export_button = tk.Button(control_frame, text="Export as PNG", command=save_as_png)
export_button.pack(side=tk.RIGHT, padx=5, pady=5)

root.mainloop()
