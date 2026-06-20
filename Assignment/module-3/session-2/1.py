f = open("lyrics.txt", "r")
print(f.tell())   # Position before reading
f.read(10)        # Read 10 characters
print(f.tell())   # Position after reading
