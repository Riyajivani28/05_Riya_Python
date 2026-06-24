
import random
from songs import song_list

def generate_playlist():
    playlist = song_list.copy()   
    random.shuffle(playlist)
    return playlist

if __name__ == "__main__":
    shuffled = generate_playlist()

    print("Your Random Playlist:\n")
    for i, song in enumerate(shuffled, start=1):
        print(f"{i}. {song}")