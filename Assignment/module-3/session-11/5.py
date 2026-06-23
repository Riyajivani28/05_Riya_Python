import pymysql

db = pymysql.connect(host="localhost", user="root", password="", database="student")
cr = db.cursor()

delete_data = "delete from playlists WHERE id = 2"

try:
    cr.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)

