import os
import sqlite3
from sign_in import *
from db_connection import *
from update_password import *

def main():
    os.system("cls")

    connection = new_connect_to_db("password_database.db")
    cursor = new_cursor(connection)
    update_password(cursor, "Passwords", "Lovro", "unicycle", "Netflix")
    disconnect_from_db(connection)

    print("Hello!\n\nYou have two options now:")
    print("1: Sign in")
    print("2: Exit\n")

    start_choice = input("1/2: ")

    if start_choice == "1":
        sign_in()
        










if __name__ == "__main__":
    main()  