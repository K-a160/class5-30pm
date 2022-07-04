# import mysql.connector
# #importing database
# database = mysql.connector.connect(
# host="localhost",
# user="root",
# password=""
# )
# db = database.cursor()

# db.execute("CREATE DATABASE pythons")


# import mysql.connector
# #importing database
# database = mysql.connector.connect(
# host="localhost",
# user='root',
# password='',

# database = 'pythonclass5pm'
# )
# db = database.cursor()

# {

    
# # db.execute("CREATE TABLE subject(id INT, name VARCHAR(255))")
# db.execute("SELECT * FROM STUDENT")
# result =db.fetchall()
# for x in result:
#  print(x)

# view
# db.execute("SELECT sn,Name,Total,Pre FROM STUDENT")
# result =db.fetchall()
# for x in result:
#  print(x)


# sql = '''INSERT INTO student (sn, Name, Physics, Chemistry, Math, English, Nepali, Total, Pre, Grade) 
#       VALUES (5, 'ayush', 82, 24, 14, 44, 44, 222, 25.25, 'B')'''
# db.execute(sql)
# database.commit()


# sql = "DELETE FROM STUDENT  WHERE SN = 6"
# db.execute(sql)
# database.commit()

# sql = "UPDATE   STUDENT  SET NAME  = 'John' where name = 'ram'"
# db.execute(sql)
# database.commit()

#  }

# wap to input values and in database  



