import sqlite3

def connect_to_db(i):
  connection = sqlite3.connect(i)
  return connection

def disconnect_from_db(i):
  i.commit()
  i.close()