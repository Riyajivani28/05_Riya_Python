import pymysql

try:
    connection = pymysql.connect(host="localhost",user="root",password="",database="student")

    cursor = connection.cursor()
    query = "UPDATE playlists SET name = %s WHERE name = %s"

    cursor.execute(query, ("Chill Vibes", "Lo-fi Chill"))

    connection.commit()
    if cursor.rowcount > 0:
        print("Updated successfully")
    else:
        print("Record not found")
except Exception as e:
    print(e)