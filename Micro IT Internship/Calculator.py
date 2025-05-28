import tkinter as tk

# -----------------------------
# 🧠 Basic Function Definitions
# -----------------------------

def add_character(char):
    """Add the clicked button character to the display."""
    current_expression = display_text.get()
    display_text.set(current_expression + str(char))

def evaluate_expression():
    """Evaluate the current expression and show the result."""
    try:
        result = eval(display_text.get())
        display_text.set(str(result))
    except Exception:
        display_text.set("Error")  # Handle errors like division by 0

def clear_display():
    """Clear the entire expression."""
    display_text.set("")

def delete_last_character():
    """Delete the last entered character."""
    current_expression = display_text.get()
    display_text.set(current_expression[:-1])

# -----------------------------
# 🖼️ GUI Setup
# -----------------------------

# Create main window
app = tk.Tk()
app.title("Simple Calculator")
app.geometry("360x520")
app.configure(bg="#1e1e1e")  # Dark background
app.resizable(False, False)  # Fixed size

# Tkinter StringVar to store input/output text
display_text = tk.StringVar()

# -----------------------------
# 🪟 Display Entry Field
# -----------------------------

entry_field = tk.Entry(
    app,
    textvariable=display_text,
    font=("Helvetica", 26),
    bg="#333",
    fg="#00FFAB",
    justify="right",
    bd=0
)
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=8, ipady=20, sticky="nsew")

# -----------------------------
# 🔘 Buttons Configuration
# -----------------------------

button_font = ("Helvetica", 18)
button_color = "#3A3A3A"
button_text_color = "white"
button_hover = "#5D5D5D"

# Buttons layout (rows of text)
button_rows = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create calculator buttons
for row_index, row in enumerate(button_rows):
    for col_index, button_char in enumerate(row):
        if button_char == '=':
            action = evaluate_expression
        else:
            action = lambda x=button_char: add_character(x)

        tk.Button(
            app,
            text=button_char,
            font=button_font,
            bg=button_color,
            fg=button_text_color,
            activebackground=button_hover,
            bd=0,
            command=action
        ).grid(row=row_index + 2, column=col_index, sticky="nsew", padx=5, pady=5, ipadx=10, ipady=15)

# -----------------------------
# 🧼 Clear Button
# -----------------------------

tk.Button(
    app,
    text="Clear",
    font=("Helvetica", 16, "bold"),
    bg="#FF5C5C",
    fg="white",
    activebackground="#FF8787",
    bd=0,
    command=clear_display
).grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5, ipady=15)

# -----------------------------
# ⌫ Delete Button
# -----------------------------

tk.Button(
    app,
    text="Delete",
    font=("Helvetica", 16, "bold"),
    bg="#FFA500",
    fg="white",
    activebackground="#FFB84C",
    bd=0,
    command=delete_last_character
).grid(row=1, column=2, columnspan=2, sticky="nsew", padx=5, pady=5, ipady=15)

# -----------------------------
# 🔳 Make Grid Responsive
# -----------------------------

for i in range(6):  # 6 total rows
    app.grid_rowconfigure(i, weight=1)

for j in range(4):  # 4 total columns
    app.grid_columnconfigure(j, weight=1)

# -----------------------------
# 🚀 Start the GUI
# -----------------------------
app.mainloop()
