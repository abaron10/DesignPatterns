from abc import  ABC,abstractmethod

class Compressor():
    @abstractmethod
    def compress(self,filename):pass