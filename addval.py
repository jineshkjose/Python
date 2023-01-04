import mysql.connector

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)

mycursor = connection.cursor()

Qry= "INSERT INTO class12 (sno, sname) VALUES (%s, %s)"

sno=input('enter the roll number of student ')
sname=input('enter the name of student ')


data = (sno, sname)
mycursor.execute(Qry, data)



print(mycursor.rowcount, "record inserted.")
