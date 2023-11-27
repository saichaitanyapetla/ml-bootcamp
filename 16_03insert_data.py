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
mycursor.execute("insert into db_01.table_01 values(3,'chaitanya','2023-11-27','ml-bootcamp')")
mydb.commit()
