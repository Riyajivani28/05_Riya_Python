import random

songs = []
n = int(input("How many songs do you want to enter? "))

for i in range(n):
    song = input("Enter song name: ")
    songs.append(song)
random.shuffle(songs)
print("\nShuffled Playlist:")
for s in songs:
    print(s)