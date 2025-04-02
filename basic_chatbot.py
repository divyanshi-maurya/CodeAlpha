
# import tkinter as tk
# from tkinter import messagebox
# def validate_and_submit():
#     first_name = name1.get().strip()
#     last_name = name3.get().strip()
#     mobile = mob.get().strip()
#     email = email1.get().strip()

#     if not first_name:
#         messagebox.showerror("Error", "First Name cannot be empty!")
#         return

#     if not last_name:
#         messagebox.showerror("Error", "Last Name cannot be empty!")
#         return

#     if not mobile.isdigit() or len(mobile) != 10:
#         messagebox.showerror("Error", "Mobile number must be exactly 10 digits!")
#         return

#     if "@" not in email or "." not in email:
#         messagebox.showerror("Error", "Enter a valid Email Address!")
#         return

#     messagebox.showinfo("Success", "Successfully Entered!")
# root = tk.Tk()
# root.title("Grid Layout Example")

# tk.Label(root, text="first name:").grid(row=0, column=0, padx=10, pady=10)
# name1 = tk.Entry(root)
# name1.grid(row=0, column=1, padx=10, pady=10)

# tk.Label(root, text="last name").grid(row=1, column=0, padx=10, pady=10)
# name3 = tk.Entry(root)
# name3.grid(row=1, column=1, padx=10, pady=10)
# tk.Label(root, text="mobile").grid(row=2, column=0, padx=10, pady=10)
# mob = tk.Entry(root)
# mob.grid(row=2, column=1, padx=10, pady=10)
# tk.Label(root, text="gmail").grid(row=3, column=0, padx=10, pady=10)
# email1 = tk.Entry(root)
# email1.grid(row=3, column=1, padx=10, pady=10)


# label1 = tk.Label(root, text="")
# label1.grid(row=4, column=1, columnspan=2, pady=10)

# tk.Button(root, text="Submit", command=validate_and_submit).grid(row=4, column=0, columnspan=2, pady=20)

# root.mainloop()


# wap to perform arithmetic operation by using tkinter
import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry1.get().strip())
        num2 = float(entry2.get().strip())

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation")
            return
        
        label_result.config(text=f"Result: {result:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Arithmetic Operations")

tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root, width=20)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root, width=20)
entry2.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Add", command=lambda: calculate("Add")).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Subtract", command=lambda: calculate("Subtract")).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Multiply", command=lambda: calculate("Multiply")).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Divide", command=lambda: calculate("Divide")).grid(row=3, column=1, padx=10, pady=10)

label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, column=0, padx=10, pady=10)

root.mainloop()