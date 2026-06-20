def read_next_line(filename):
    f = open(filename, "r")
    f.seek(20)          
    print(f.readline()) 
read_next_line("lyrics.txt")