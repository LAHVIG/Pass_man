def update_password(cursor, table, user, password, chategory):
    cursor.execute("UPDATE " + table + " SET " + user + " = " + "'" + password + "'" + " WHERE Chategory = " + "'" + chategory + "'")
    #print("UPDATE " + table + " SET " + user + " = " + "'" + password + "'" + " WHERE Chategory = " + "'" + chategory + "'")

#update_password(2, "Passwords", "Lovro", "unicycle", "Netflix")