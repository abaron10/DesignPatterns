
class EditorState():

    __content = ""
    def __init__(self,content):
        self.__content = content

    def getContent(self):
        return self.__content

    def setContent(self, content):
        self.__content = content
        
        