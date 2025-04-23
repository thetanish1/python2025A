# abstract class
# abstract class object 
# abc module ABC
# abstract class will normal
# abstract --- abstract implementation






from abc import *
# interface 

class Myclass(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass

class Oracle(Myclass):
    def connect(self):
        print("oracle connected....")
    def disconnect(self):
        print("oracle disconnected ..")

class MongoDb(Myclass):
    def connect(self):
        print("mongoDb connected....")
    def disconnect(self):
        print("mongoDb disconnected ..")

class Database:
    str = input("Enter the database name .....") # Oracle
    className = globals()[str] # Oracle
    x = className()
    x.connect()
    x.disconnect()











