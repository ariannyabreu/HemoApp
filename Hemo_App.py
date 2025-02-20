import tkinter as tk
from tkinter import messagebox
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
root.configure(bg="white")
root.title("HemoApp - Blood Compatibility & Blood Type Prediction")

window_width = 450
window_height = 450
root.geometry(f"{window_width}x{window_height}")

# Load image
image_path = "blood_drop.png"
image = Image.open(image_path)

size = 150
image = image.resize((size, size), Image.LANCZOS)

mask = Image.new("L", (size, size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, size, size), fill=255)

circle_image = Image.new("RGBA", (size, size))
circle_image.paste(image, (0, 0), mask)

# Convert to tkinter compatible format
photo = ImageTk.PhotoImage(circle_image)

# Create a label to display the round image
label = tk.Label(root, image=photo, bg="white")
label.place(x=5, y=280)

# Blood type compatibility section
tk.Label(root, text="Check Blood Compatibility", font=("Arial", 16, "bold"), bg="white", fg="black").pack(pady=10)

user_blood = tk.StringVar()
user_blood.set("O-")

# Option menu for blood type
user_blood_option = tk.OptionMenu(root, user_blood, *compatibility.keys())
user_blood_option.config(bg="white", fg="black", relief="solid", highlightthickness=0)
user_blood_option.pack(pady=5)

# Button to check compatibility
#check_compatibility_button = tk.Button(root, text="Check Compatibility", command=compatibility_blood_type, bg="lightgray", fg="black", relief="solid")
#check_compatibility_button.pack(pady=5)

check_compatibility_button = tk.Button(
    root,
    text="Check Compatibility",
    command=compatibility_blood_type,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 14, "bold"),
    relief="raised",
    bd=5,
    width=15,
    height=2,
    highlightthickness=0,
    activebackground="#45a049",
    activeforeground="white",
)
check_compatibility_button.pack(pady=10)


# Blood type inheritance section
tk.Label(root, text="Predict Child’s Blood Type", font=("Arial", 16, "bold"), bg="white", fg="black").pack(pady=10)

father_blood = tk.StringVar()
mother_blood = tk.StringVar()
rh_father_var = tk.StringVar()
rh_mother_var = tk.StringVar()

father_blood.set("A")
mother_blood.set("O")
rh_father_var.set("+")
rh_mother_var.set("-")

# Father blood type label and Option menu
tk.Label(root, text="Father's Blood Type", bg="white", fg="black").pack()
father_blood_option = tk.OptionMenu(root, father_blood, *["A", "B", "AB", "O"])
father_blood_option.config(bg="white", fg="black", relief="solid", highlightthickness=0)
father_blood_option.pack(pady=5)

# Father Rh factor label and Option menu
tk.Label(root, text="Father's Rh Factor", bg="white", fg="black").pack()
rh_father_option = tk.OptionMenu(root, rh_father_var, "+", "-")
rh_father_option.config(bg="white", fg="black", relief="solid", highlightthickness=0)
rh_father_option.pack(pady=5)

# Mother Blood type Label and Option menu
tk.Label(root, text="Mother's Blood Type", bg="white", fg="black").pack()
mother_blood_option = tk.OptionMenu(root, mother_blood, *["A", "B", "AB", "O"])
mother_blood_option.config(bg="white", fg="black", relief="solid", highlightthickness=0)
mother_blood_option.pack(pady=5)

# Mother Rh factor label and Option menu
tk.Label(root, text="Mother's Rh Factor", bg="white", fg="black").pack()
rh_mother_option = tk.OptionMenu(root, rh_mother_var, "+", "-")
rh_mother_option.config(bg="white", fg="black", relief="solid", highlightthickness=0)
rh_mother_option.pack(pady=5)

# Button to predict blood type
#predict_button = tk.Button(root, text="Predict Blood Type", command=predict_blood_type, bg="lightgray", fg="black", bd=0, relief="flat")
#predict_button.pack(padx=20, pady=20)

predict_button = tk.Button(
    root,
    text="Predict Blood Type",
    command=predict_blood_type,
    bg="black",
    fg="white",
    font=("Arial", 14, "bold"),
    relief="raised",
    bd=5,
    width=15,
    height=2,
    highlightthickness=0,
    activebackground="#45a049",
    activeforeground="white",
)
predict_button.pack(pady=10)


root.mainloop()







