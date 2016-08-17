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
        user.authenticate() 
        print("Welcome..." + username)
        print("Authentication Unsuccessful!")
if __name__ == "__main__":
    main() 
