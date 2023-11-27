import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
## mycursor.execute("select * from db_01.table_01 where studentID>2")
## mycursor.execute("select name,courseName from db_01.table_01 ")
## mycursor.execute("select name,courseName from db_01.table_01 where studentID between 1 and 5 ")
## mycursor.execute("select count(*) from db_01.table_01")


for x in mycursor:
 print(x)