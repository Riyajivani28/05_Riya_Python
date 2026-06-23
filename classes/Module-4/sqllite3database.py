import sqlite3

try:
    db=sqlite3.connect('student.db')
    print("Database connected!")
except Exception as e:
    print(e)

#Table Create
create="create table studentinfo(id integer primary key autoincrement,name text,city text)"

try:
    db.execute(create)
    print("Table created....")
except Exception as e:
    print(e)
    
'''#Insert Data
insert="insert into studentinfo(name,city)values('Riya','rajkot'),('Gatu','surat'),('Datiii','bhavnagar')"

try:
    db.execute(insert)
    db.commit()
    print("Record inserted....")
except Exception as e:
    print(e)'''
    
#Update Data
'''update="update studentinfo set city='ahmedabad' where id=1"
try:
    db.execute(update)
    db.commit()
    print("Record updated.....")
except Exception as e:
    print(e)'''

#Delete_Data
'''delete="delete from studentinfo where id=3"
try:
    db.execute(delete)
    db.commit()
    print("Record deleted....")
except Exception as e:
    print(e)'''

cr=db.cursor()

#Select Data
select="select * from studentinfo"
try:
    cr.execute(select)
    data=cr.fetchall()
    #data=cr.fetchmany(2)
    #data=cr.fetchone()
    #print(data)
    for i in data:
        print(i)
except Exception as e:
    print(e)
   