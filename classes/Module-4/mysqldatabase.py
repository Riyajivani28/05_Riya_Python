import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='python_demo')
    print("Database connected...")
except Exception as e:
    print(e)
    
cr=db.cursor()

#Table Create
create="create table studentinfo(id integer primary key auto_increment,name varchar(20),city varchar(20))"

try:
    cr.execute(create)
    print("Table created....")
except Exception as e:
    print(e)

#Insert Data
'''insert="insert into studentinfo(name,city)values('Riya','rajkot'),('Gatu','surat'),('Datiii','bhavnagar')"

try:
    cr.execute(insert)
    db.commit()
    print("Record inserted....")
except Exception as e:
    print(e)'''

#Update Data
'''update="update studentinfo set city='ahmedabad' where id=1"
try:
    cr.execute(update)
    db.commit()
    print("Record updated.....")
except Exception as e:
    print(e)'''

#Delete_Data
'''delete="delete from studentinfo where id=3"
try:
    cr.execute(delete)
    db.commit()
    print("Record deleted....")
except Exception as e:
    print(e)'''

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