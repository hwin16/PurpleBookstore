import redis
from const import *
from RedisConnector import * 

class User(RedisConnector): 
    def __init__(self, dbname, username): 
        RedisConnector.__init__(self, dbname)
        # ._user is redis instance
        self._user = self.connect(dbname)
        self._username = username
    
    def getUserID(self, username):
        self._user.incr(self._username) 
        return self._user.get(username)

def main(): 
    usr = User(0, hello)
    print "%d" % usr.getUserID()

if __name__ == "__main__": 
    main()
