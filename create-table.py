import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="swap")
mycursor = mydb.cursor()
mycursor.execute("Create table address(street varchar(50),pincode int(20),country varchar(50),Phone_num int(13)")
mycursor.execute("show tables")

for tb in mycursor:
	print(tb)