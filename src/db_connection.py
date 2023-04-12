import sqlite3

def new_connect_to_db(i):
  connection = sqlite3.connect(i)
  return connection

def new_cursor(i):
  cursor = i.cursor()
  return cursor

def disconnect_from_db(i):
  i.commit()
  i.close()

'''
connection = new_connect_to_db("password_database.db")
cursor = new_cursor(connection)
print(cursor)
disconnect_from_db(connection)
'''