import redis
from const import *
from RedisConnector import * 

class User(RedisConnector): 
    ID = "user_id"
    def __init__(self, username, password): 
        RedisConnector.__init__(self)
        # ._user is redis instance
        self._user = self.connect()
        self._username = username
        self._password = password

    def _getCurrentID(self): 
        return self._user.get(self.ID)

    def addUser(self):
        self._user.incr(self.ID)
        userData = {"username": self._username, 
                    "password": self._password}
        print("ID: " + self._getCurrentID() )
        self._user.hmset("user:" + self._getCurrentID(), userData) 
        self.populateUsername() 

    def populateUsername(self): 
        user = self._getCurrentID() 
        self._user.hset("users", self._username, self._getCurrentID())

    def getUserID(self): 
        print self._user.hget("users", self._username)

    def getPwd(self): 
        print self._user.hmget("user:" + self.getUserID(), password)

    def authenticate(self): 
        # get username from user
        self.getUserID() 
        print self._password
        return self.getPwd() == self._password

def main(): 
    usr = User("htut", "htaywin")
    usr.addUser()
    usr2 = User("wint", "hnin") 
    usr2.addUser() 

if __name__ == "__main__": 
    main()
