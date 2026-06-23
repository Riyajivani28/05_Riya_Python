from tkinter import *

root = Tk()
root.title("My Playlist")
root.geometry("600x350")
root.config(bg="#d8f3dc")

heading = Label(root,text="🎵 Welcome to Your Music Playlist 🎵",font=("Arial", 18, "bold"),bg="#d8f3dc",fg="darkgreen")
heading.pack(pady=20)

def play():
    status.config(text="Playing")

def pause():
    status.config(text="Paused")

def next_song():
    status.config(text="Next Song")

frame = Frame(root, bg="#d8f3dc")
frame.pack(pady=20)


play_btn = Button(frame,text="Play",font=("Arial", 12, "bold"),bg="lightgreen",width=10,command=play)
play_btn.grid(row=0, column=0, padx=10)

pause_btn = Button(frame,text="Pause",font=("Arial", 12, "bold"),bg="khaki",width=10,command=pause)
pause_btn.grid(row=0, column=1, padx=10)

next_btn = Button(frame,text="Next",font=("Arial", 12, "bold"),bg="lightblue",width=10,command=next_song)
next_btn.grid(row=0, column=2, padx=10)

status = Label(root,text="Select an Action",font=("Arial", 16, "bold"),bg="#d8f3dc",fg="blue")
status.pack(pady=30)

root.mainloop()