from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("stud.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS information (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    mobile TEXT
)
""")
conn.commit()

root = Tk()
root.title("login page")
root.geometry("550x450")
root.config(bg="lightpink")

name_var = StringVar()
email_var = StringVar()
mobile_var = StringVar()

selected_id = None

def clear():
    name_var.set("")
    email_var.set("")
    mobile_var.set("")

def submit():
    global selected_id

    name = name_var.get()
    email = email_var.get()
    mobile = mobile_var.get()

    if name == "" or email == "" or mobile == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    if not mobile.isdigit() or len(mobile) != 10:
        messagebox.showerror("Error", "Mobile must be 10 digits!")
        return

    if "@" not in email or "." not in email:
        messagebox.showerror("Error", "Enter valid email!")
        return

    c.execute("INSERT INTO information(name,email,mobile) VALUES (?,?,?)",
              (name, email, mobile))
    conn.commit()

    selected_id = c.lastrowid

    messagebox.showinfo("Success", "Data Saved!")
    clear()

def show_data():
    global selected_id

    if selected_id is None:
        messagebox.showerror("Error", "First submit data!")
        return

    c.execute("SELECT * FROM information WHERE id=?", (selected_id,))
    row = c.fetchone()

    if row:
        name_var.set(row[1])
        email_var.set(row[2])
        mobile_var.set(row[3])

        messagebox.showinfo(
            "My Details",
            f"Name: {row[1]}\nEmail: {row[2]}\nMobile: {row[3]}"
        )

def update_data():
    global selected_id

    if selected_id is None:
        messagebox.showerror("Error", "No record selected!")
        return

    c.execute("""
        UPDATE information
        SET name=?, email=?, mobile=?
        WHERE id=?
    """, (name_var.get(), email_var.get(), mobile_var.get(), selected_id))

    conn.commit()
    messagebox.showinfo("Success", "Data Updated!")

def delete_data():
    global selected_id

    if selected_id is None:
        messagebox.showerror("Error", "No record selected!")
        return

    c.execute("DELETE FROM information WHERE id=?", (selected_id,))
    conn.commit()

    messagebox.showinfo("Success", "Data Deleted!")
    clear()



Label(root, text="login page", font=("Arial", 20, "bold"),
      bg="lightpink").grid(row=0, column=0, columnspan=2, pady=15)

Label(root, text="Name", bg="lightpink").grid(row=1, column=0, padx=10, pady=10)
Entry(root, textvariable=name_var, width=30).grid(row=1, column=1)

Label(root, text="Email", bg="lightpink").grid(row=2, column=0, padx=10, pady=10)
Entry(root, textvariable=email_var, width=30).grid(row=2, column=1)

Label(root, text="Mobile", bg="lightpink").grid(row=3, column=0, padx=10, pady=10)
Entry(root, textvariable=mobile_var, width=30).grid(row=3, column=1)

Button(root, text="Submit", command=submit,
       bg="green", fg="white", width=12).grid(row=4, column=0, pady=10)

Button(root, text="Show", command=show_data,
       bg="purple", fg="white", width=12).grid(row=4, column=1, pady=10)

Button(root, text="Update", command=update_data,
       bg="blue", fg="white", width=12).grid(row=5, column=0, pady=10)

Button(root, text="Delete", command=delete_data,
       bg="red", fg="white", width=12).grid(row=5, column=1, pady=10)

root.mainloop()