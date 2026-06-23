from tkinter import *

root = Tk()
root.title("Login Form")
root.geometry("400x300")
root.config(bg="#1f1f2e")

Label(root, text="LOGIN", font=("Arial", 18, "bold"),
      bg="#1f1f2e", fg="white").pack(pady=10)

form = Frame(root, bg="#1f1f2e")
form.pack(pady=10)

Label(form, text="Username :", bg="#1f1f2e", fg="white",
      font=("Arial", 11)).grid(row=0, column=0, padx=5, pady=5, sticky="e")

username_entry = Entry(form, font=("Arial", 11), width=20)
username_entry.grid(row=0, column=1, padx=5, pady=5)


Label(form, text="Password :", bg="#1f1f2e", fg="white",
      font=("Arial", 11)).grid(row=1, column=0, padx=5, pady=5, sticky="e")

password_entry = Entry(form, font=("Arial", 11), width=20, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)


def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_btn.config(text="Hide Password")
    else:
        password_entry.config(show="*")
        show_btn.config(text="Show Password")

show_btn = Button(root, text="Show Password", command=toggle_password)
show_btn.pack(pady=5)


msg = Label(root, text="", bg="#1f1f2e", font=("Arial", 11, "bold"))
msg.pack(pady=10)


def animate_login(i=0):
    dots = "." * (i % 4)
    msg.config(text="Logging in" + dots, fg="yellow")

    if i < 10:
        root.after(200, animate_login, i+1)
    else:
        msg.config(text="Login Successful ✅", fg="lightgreen")
        username_entry.delete(0, END)
        password_entry.delete(0, END)


def login():
    u = username_entry.get()
    p = password_entry.get()

    if u != "" and p != "":
        animate_login()
    else:
        msg.config(text="Please fill all fields ❌", fg="red")


Button(root, text="Login", font=("Arial", 12, "bold"),
       bg="#4cc9f0", fg="black", width=15,
       command=login).pack(pady=10)

root.mainloop()