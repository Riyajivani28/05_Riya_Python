class SongAlreadyExistsError(Exception):
    pass

def add_song_to_playlist(song_name, playlist):
    if song_name in playlist:
        raise SongAlreadyExistsError("Song already exists in playlist")
    
    playlist.append(song_name)
    print("Song added successfully")

playlist = ["Shape of You", "Believer", "Perfect"]

try:
    add_song_to_playlist("Believer", playlist)
except SongAlreadyExistsError as e:
    print(e)

print(playlist)