from tkinter import *

root = Tk()
root.title("Music Controls")
root.geometry("300x250")
root.config(bg="#1e1e2f")

def action(name):
    status.config(text=name)

btn1 = Button(root, text="Like", width=12, bg="#ff4d6d", fg="white",
              command=lambda: action("Liked"))
btn1.grid(row=0, column=0, padx=10, pady=10)

btn2 = Button(root, text="Share", width=12, bg="#4cc9f0", fg="white",
              command=lambda: action("Shared"))
btn2.grid(row=0, column=1, padx=10, pady=10)

btn3 = Button(root, text="Download", width=12, bg="#80ed99",
              command=lambda: action("Downloading"))
btn3.grid(row=1, column=0, padx=10, pady=10)

btn4 = Button(root, text="Add to Queue", width=12, bg="#f9c74f",
              command=lambda: action("Added to Queue"))
btn4.grid(row=1, column=1, padx=10, pady=10)

status = Label(root, text="Select Action", font=("Arial", 12, "bold"),
               bg="#1e1e2f", fg="white")
status.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()