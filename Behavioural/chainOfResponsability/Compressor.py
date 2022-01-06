
from Handler import Handler

class Compressor(Handler):

    def doHandle(self, request):
        print("Compress")
        return False
