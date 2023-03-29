import os

users = []
def test_bench():
    lovro_antic = ("lovroantic","abekat123")
    users.append(lovro_antic)


def main():
    #meget dårligt kode, undskyld
    test_bench()



    os.system('cls')
    print("You have three options: \n1. Sign in \n2. Sign up\n3. Exit")
    user_input = input("What would you like to do?: ")
    if(user_input.lower() == "sign in" or "1"):
        sign_in()

def sign_in():
    os.system('cls')
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if user_exists(username, password, users):
        print(f"Login successful! Welcome back {username}")
    else:
        print("Incorrect username or password.")




def user_exists(username, password, users):
    for user in users:
        if user[0] == username and user[1] == password:
            return True
    return False


def password_matches(pass_in):
    print("")


if __name__ == "__main__":
    main()

