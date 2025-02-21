import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk, ImageDraw

compatibility = {
    "O-": ["O-"],
    "O+": ["O-", "O+"],
    "A-": ["O-", "A-"],
    "A+": ["O-", "O+", "A-", "A+"],
    "B-": ["O-", "B-"],
    "B+": ["O-", "O+", "B-", "B+"],
    "AB-": ["O-", "A-", "B-", "AB-"],
    "AB+": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"]
}

inheritance_abo = {
    ("A", "A"): ["A", "A"],
    ("A", "O"): ["A", "O"],
    ("A", "B"): ["A", "B", "AB", "O"],
    ("B", "B"): ["B", "B"],
    ("B", "O"): ["B", "O"],
    ("O", "O"): ["O"],
    ("AB", "A"): ["A", "AB", "B"],
    ("AB", "B"): ["B", "AB", "A"],
    ("AB", "O"): ["A", "B"],
    ("AB", "AB"): ["A", "B", "AB"]
}

inheritance_rh = {
    ("+", "+"): ["+"],
    ("+", "-"): ["+", "-"],
    ("-", "-"): ["-"]
}

# Function to predict blood type inheritance
def predict_blood_type():
    father = father_blood.get()
    mother = mother_blood.get()
    rh_father = rh_father_var.get()
    rh_mother = rh_mother_var.get()

    if not father or not mother or not rh_father or not rh_mother:
        messagebox.showwarning("Warning", "Please select all options.")
        return

    possible_blood_types = inheritance_abo.get((father, mother), inheritance_abo.get((mother, father)))
    possible_rh = inheritance_rh.get((rh_father, rh_mother), inheritance_rh.get((rh_mother, rh_father)))

    messagebox.showinfo("Prediction",
                        f"Possible blood types for children: {set(possible_blood_types)}\nPossible Rh factors: {set(possible_rh)}")

# Function to check blood compatibility
def compatibility_blood_type():
    user_type = user_blood.get()

    if not user_type:
        messagebox.showwarning("Warning", "Please select a blood type.")
        return

    donors = ", ".join(compatibility[user_type])
    messagebox.showinfo("Compatibility", f"You can receive blood from: {donors}")


# GUI
root = tk.Tk()
root.configure(bg="#f0f0f0")  # Light gray background
root.title("HemoApp - Blood Compatibility & Blood Type Prediction")

window_width = 600
window_height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create main frames
header_frame = tk.Frame(root, bg="#f0f0f0")
header_frame.pack(fill="x", pady=20)

compatibility_frame = tk.Frame(root, bg="white", relief="solid", bd=1)
compatibility_frame.pack(fill="x", padx=40, pady=10)

inheritance_frame = tk.Frame(root, bg="white", relief="solid", bd=1)
inheritance_frame.pack(fill="x", padx=40, pady=10)

# Load and display the picture logo
image_path = "blood_drop.png"
image = Image.open(image_path)
size = 110
image = image.resize((size, size), Image.LANCZOS)
mask = Image.new("L", (size, size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, size, size), fill=255)
circle_image = Image.new("RGBA", (size, size))
circle_image.paste(image, (0, 0), mask)
photo = ImageTk.PhotoImage(circle_image)

# Logo and title in header
logo_label = tk.Label(header_frame, image=photo, bg="#f0f0f0")
logo_label.pack(side="left", padx=20)

title_label = tk.Label(
    header_frame,
    text="HemoApp",
    font=("Arial", 24, "bold"),
    bg="#f0f0f0",
    fg="#ff4d4d"
)
title_label.pack(side="left", padx=10)

# Blood type compatibility section
tk.Label(
    compatibility_frame,
    text="Check Blood Compatibility",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#ff4d4d"
).pack(pady=15)

user_blood = tk.StringVar()
user_blood.set("O-")

# Styled option menu for blood type
style = ttk.Style()
style.configure("Custom.TMenubutton", background="white", padding=5)
user_blood_option = ttk.OptionMenu(
    compatibility_frame,
    user_blood,
    "O-",
    *compatibility.keys(),
    style="Custom.TMenubutton"
)
user_blood_option.pack(pady=10)

check_compatibility_button = tk.Button(
    compatibility_frame,
    text="Check Compatibility",
    command=compatibility_blood_type,
    bg="#e6e6e6",  # Light gray background
    fg="black",    # Black text
    activebackground="#ff4d4d",
    activeforeground="white",
    relief="raised",
    font=("Arial", 11, "bold"),
    width=20,
    height=1
)
check_compatibility_button.pack(pady=15)

# Blood type inheritance section
tk.Label(
    inheritance_frame,
    text="Predict Child's Blood Type",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#ff4d4d"
).pack(pady=15)

# Create two columns for parents
parents_frame = tk.Frame(inheritance_frame, bg="white")
parents_frame.pack(fill="x", padx=20)

father_frame = tk.Frame(parents_frame, bg="white")
father_frame.pack(side="left", expand=True)

mother_frame = tk.Frame(parents_frame, bg="white")
mother_frame.pack(side="right", expand=True)

# Father's inputs
tk.Label(
    father_frame,
    text="Father's Blood Type",
    bg="white",
    fg="#333333",
    font=("Arial", 10, "bold")
).pack(pady=5)

father_blood = tk.StringVar(value="A")
ttk.OptionMenu(
    father_frame,
    father_blood,
    "A",
    *["A", "B", "AB", "O"]
).pack(pady=5)

tk.Label(
    father_frame,
    text="Father's Rh Factor",
    bg="white",
    fg="#333333",
    font=("Arial", 10, "bold")
).pack(pady=5)

rh_father_var = tk.StringVar(value="+")
ttk.OptionMenu(
    father_frame,
    rh_father_var,
    "+",
    "+", "-"
).pack(pady=5)

# Mother's inputs
tk.Label(
    mother_frame,
    text="Mother's Blood Type",
    bg="white",
    fg="#333333",
    font=("Arial", 10, "bold")
).pack(pady=5)

mother_blood = tk.StringVar(value="O")
ttk.OptionMenu(
    mother_frame,
    mother_blood,
    "O",
    *["A", "B", "AB", "O"]
).pack(pady=5)

tk.Label(
    mother_frame,
    text="Mother's Rh Factor",
    bg="white",
    fg="#333333",
    font=("Arial", 10, "bold")
).pack(pady=5)

rh_mother_var = tk.StringVar(value="-")
ttk.OptionMenu(
    mother_frame,
    rh_mother_var,
    "-",
    "+", "-"
).pack(pady=5)

predict_button = tk.Button(
    inheritance_frame,
    text="Predict Blood Type",
    command=predict_blood_type,
    bg="#e6e6e6",
    fg="black",
    activebackground="#ff4d4d",
    activeforeground="white",
    relief="raised",
    font=("Arial", 11, "bold"),
    width=20,
    height=1
)
predict_button.pack(pady=20)

# Footer
footer_frame = tk.Frame(root, bg="#f0f0f0")
footer_frame.pack(fill="x", pady=20)
footer_text = tk.Label(
    footer_frame,
    text="© 2024 HemoApp - Blood Type Analysis Tool",
    font=("Arial", 8),
    bg="#f0f0f0",
    fg="#666666"
)
footer_text.pack()

root.mainloop()







