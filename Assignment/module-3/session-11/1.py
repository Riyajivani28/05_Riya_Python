import pymysql

try:
    connection = pymysql.connect(host="localhost",user="root",password="",database="student")
    print("Connection successful")
    connection.close()

except Exception as e:
    print(e)