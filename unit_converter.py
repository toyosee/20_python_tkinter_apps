import tkinter as tk
from tkinter import ttk

def convert_units():
    try:
        input_value = float(entry_value.get())
        if conversion_type.get() == "Meters to Kilometers":
            result = input_value / 1000
            label_result.config(text=f"{result:.4f} Kilometers")
        elif conversion_type.get() == "Kilometers to Meters":
            result = input_value * 1000
            label_result.config(text=f"{result:.2f} Meters")
        elif conversion_type.get() == "Celsius to Fahrenheit":
            result = (input_value * 9/5) + 32
            label_result.config(text=f"{result:.2f} °F")
        elif conversion_type.get() == "Fahrenheit to Celsius":
            result = (input_value - 32) * 5/9
            label_result.config(text=f"{result:.2f} °C")
        else:
            label_result.config(text="Select a valid conversion type.")
    except ValueError:
        label_result.config(text="Enter a valid numeric value!")

# Create the main tkinter window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("300x200")

# Title Label
label_title = tk.Label(root, text="Unit Converter", font=("Arial", 16, "bold"), fg="green")
label_title.grid(row=0, column=0, columnspan=2, pady=10)

# Input Field
label_value = tk.Label(root, text="Enter Value:")
label_value.grid(row=1, column=0, padx=10, pady=5)
entry_value = tk.Entry(root)
entry_value.grid(row=1, column=1, padx=10, pady=5)

# Dropdown Menu
label_conversion = tk.Label(root, text="Select Conversion:")
label_conversion.grid(row=2, column=0, padx=10, pady=5)
conversion_type = ttk.Combobox(root, state="readonly", width=22)
conversion_type['values'] = ("Meters to Kilometers", "Kilometers to Meters",
                             "Celsius to Fahrenheit", "Fahrenheit to Celsius")
conversion_type.grid(row=2, column=1, padx=10, pady=5)
conversion_type.set("Select Conversion Type")

# Convert Button
button_convert = tk.Button(root, text="Convert", command=convert_units)
button_convert.grid(row=3, column=0, columnspan=2, pady=10)

# Result Label
label_result = tk.Label(root, text="Result:", font=("Arial", 12, "bold"))
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Run the tkinter Main Loop
root.mainloop()
