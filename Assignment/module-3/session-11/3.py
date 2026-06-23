import pymysql

connection = pymysql.connect(host="localhost",user="root",password="",database="student")
cursor = connection.cursor()

cursor.execute("select name, song_count FROM playlists WHERE song_count > 10")
data = cursor.fetchall()
print("Name\t\t\tSong Count")
print("-" * 30)

for row in data:
    print(row[0], "\t\t", row[1])

