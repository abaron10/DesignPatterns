
from UIControl import UIControl
class Button(UIControl):
    def __init__(self,dialogOwner):
        self.__isEnabled = False
        super().__init__(dialogOwner)

    def isEnabled(self):
        return self.__isEnabled
    def setEnabled(self,enabled):
        self.__isEnabled = enabled
        self._owner.changed(self)
