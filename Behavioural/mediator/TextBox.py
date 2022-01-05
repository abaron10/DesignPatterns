
from UIControl import UIControl
class TextBox(UIControl):
    def __init__(self,dialogOwner):
        self.__content = ""
        super().__init__(dialogOwner)

    def getContent(self):
        return self.__content
    def setContent(self,content):
        self.__content = content
        self._owner.changed(self)
