from EditorState import EditorState

class Editor():

    __content = ""

    def __init__(self):
        self._attr = 0


    def createState(self):
        return EditorState(self.__content)

    def restore(self,state):
        self.__content = state.getContent()

    def getContent(self):
        return self.__content

    def setContent(self, content):
        self.__content = content
        
        