import redis
from RedisConnector import * 
class Book(RedisConnector): 
    def __init__(self, bookID, userID, bookName, bookEdition="NA"): 
        RedisConnector.__init__(self)
        self._bookID = bookID
        self._bookName = bookName
        self._bookEdition = bookEdition 
        self._userID = userID
        self._book = self.connect() 
    
    def addBook(self): 

    def updateBook(self): 
        pass 

    def deleteBook(self): 
        pass 

def main(): 
    b = Book(1, 3, "hello")

if __name__ == "__main__": 
    main() 
