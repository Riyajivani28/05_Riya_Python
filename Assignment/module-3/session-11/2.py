import pymysql

try:
    connection = pymysql.connect(host="localhost",user="root",password="",database="student")
    cursor = connection.cursor()
    cursor.execute("create table playlists (id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(100),song_count INT)")
    print("Table created")

    query = "insert into playlists (name, song_count) VALUES (%s, %s)"

    data = [("Bollywood Hits", 50),("Lo-fi Chill", 120),("Workout Mix", 75)]

    cursor.executemany(query, data)
    connection.commit()

    print("Data inserted successfully")
except Exception as e:
    print(e)