from abc import  ABC,abstractmethod

class Filter():
    @abstractmethod
    def apply(self,filename):pass