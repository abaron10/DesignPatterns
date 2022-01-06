
from Handler import Handler

class Authenticator(Handler):

    def __init__(self,handlernext):
        super().__init__(handlernext)

    def doHandle(self, request):
        isValid = request.getUsername() == "admin" and request.getPassword() =="1234"
        print("Authentication")
        return not isValid