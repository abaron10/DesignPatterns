
from Handler import Handler

class Logger(Handler):

    def doHandle(self, request):
        print("Logger")
        return False
