from tkinter import *

root = Tk()
root.title("My Playlist")
root.geometry("500x300")
root.config(bg="lightgreen")

label = Label(root,text="Welcome to Your Music Playlist",bg="lightgreen",font=("Arial", 16, "bold"))
label.pack()
root.mainloop()