class People(RedisConnector): 
    # usrID
    # FirstName
    # LastName
    def __init__(self, username): 
        RedisConnector.__init__(self)
        self._user = self.connect()
        self._username = username

    def setFirstName(self): 
        pass

    def getFirstName(self): 
        pass 

    def setLastName(self): 
        pass

    def getLastName(self): 
        pass

    def setEmail(self): 
        pass 

    def getEmail(self): 
        pass

    def setZipcode(self): 
        pass

    def getZipcode(self):
        pass

    def printAll(self): 
        self._user.hgetall(
