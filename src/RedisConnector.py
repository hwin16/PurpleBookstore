import redis 
import yaml
from const import * 
class RedisConnector: 
    def __init__(self): 
        self._yaml = self.load_yaml()
        print "p: %s" % self._yaml
        self._host = self._yaml[END_POINT]
        self._password = self._yaml[PASSWORD]
        self._port = self._yaml[PORT]
        self._redis = self.connect()

    def connect(self): 
        pool = redis.ConnectionPool(host=self._host, 
                                    password=self._password, 
                                    port=self._port, 
                                    db=0)
        return redis.Redis(connection_pool=pool)

    def load_yaml(self): 
        f = open("Redis.yaml")
        yml = yaml.safe_load(f)
        return yml

def main(): 
    r = RedisConnector()
    # TODO close redis connection

if __name__ == "__main__": 
    main() 
