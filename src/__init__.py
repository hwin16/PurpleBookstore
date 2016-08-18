from __future__ import print_function
from User import *

def menuOptions(): 
    options = "\
    1 - Add my book\n\
    2 - Update my books\n\
    3 - List my books\n\
    4 - Find Book\n\
    5 - Explore Bookstore\n"
    return options

def main(): 
    print("-------Welcome to Bookstore--------")
    while (True): 
        print("username: ", end="")
        username = raw_input()
        print("password: ", end="")
        password = raw_input() 
        user = User(username, password) 
        if user.auth(): 
            print("Welcome...", username)
            print(menuOptions())
            x = int(raw_input())
            print("Choose option: %d", x)  
        else: 
            print("Username or password is incorrect")
            print("1> Try again 2> Create account 3> Forgot Password", end="") 
if __name__ == "__main__":
    main() 
