import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
mycursor = mydb.cursor()
mycursor.execute("Create database Address")
mycursor.execute("show databases")
for db in mycursor:
	print(db)