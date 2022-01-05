
from abc import ABC,abstractmethod
class DialogBox(ABC):
    @abstractmethod
    def changed(self,uicontrol):pass
        

