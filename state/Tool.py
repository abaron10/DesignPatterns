from abc import ABC, abstractmethod

class Tool(ABC):
    @abstractmethod
    def mouseDown(self):pass
    @abstractmethod
    def mouseUp(self):pass