def get_duration_song(songs):
    song={
        "perfect":"3:14",
        "Believer":"2:30",
        "Faded":"3:20"
    }
    try:
        return song[songs]
    except KeyError:
        return "song is not found"

x = get_duration_song("abc")
print(x)