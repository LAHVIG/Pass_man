def sign_in():
    user_credentials = input("Enter you username: ")
    if user_exists(user_credentials):
        master_pass = input("Enter master password: ")
        connection = connect_to_database()



def user_exists(usr):
    ""
    return True

def connect_to_database():
    ""

def confirm_password(master_pass):
    ""
    