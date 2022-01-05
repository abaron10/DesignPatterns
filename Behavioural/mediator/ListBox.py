
from UIControl import UIControl
class ListBox(UIControl):
    def __init__(self,dialogOwner):
        self.__selection = ""
        super().__init__(dialogOwner)

    def getSelection(self):
        return self.__selection

    def setSelection(self,selection):
        self.__selection = selection
        #private members are not inherited by subclasses so they should be protected        
        self._owner.changed(self)
