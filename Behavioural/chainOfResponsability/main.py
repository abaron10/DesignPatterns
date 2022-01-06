from Compressor import Compressor
from Authenticator import Authenticator
from Logger import Logger
from WebServer import WebServer
from HttpRequest import HttpRequest

if __name__ == '__main__':
    #auth -> logger -> Compressor
    compressor = Compressor(None)
    logger = Logger(compressor)
    authenticator = Authenticator(Logger)
    server = WebServer(authenticator)
    server.handler(HttpRequest("admin","1234"))
     