import os
from sign_in import *

def main():
    os.system("cls")

    print("Hello!\n\nYou have two options now:")
    print("1: Sign in")
    print("2: Exit\n")

    start_choice = input("1/2: ")

    if start_choice == "1":
        sign_in()
        










if __name__ == "__main__":
    main()  