

class HttpRequest():

    def __init__(self,username,password):
        self.__username = username
        self.__password = password

    def getUserName(self):
        return self.__username
    def getPassword(self):
        return self.__password
