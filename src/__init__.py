from __future__ import print_function
from User import *

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
        else: 
            print("Username or password is incorrect")
            print("1> Try again 2> Create account 3> Forgot Password", end="") 
if __name__ == "__main__":
    main() 
