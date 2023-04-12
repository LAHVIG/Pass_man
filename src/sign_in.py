from en_de_crypter import decrypt
from db_connection import *


def sign_in():
    user_credentials = input("Enter you username: ")
    if user_exists(user_credentials):
        master_pass = input("Enter master password: ")
        connection = connect_to_db()
        if password_matches(master_pass, connection):
            ""



def user_exists(usr):
    ""
    return True


def password_matches(master_pass):
    ""
    encrypted_pass = "get password from table"
    decrypted_pass = decrypt(encrypted_pass)
    if decrypted_pass == master_pass:
        return True
    
def grant_access():
    ""
