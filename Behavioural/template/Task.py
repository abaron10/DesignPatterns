from abc import ABC , abstractmethod
from  AuditTrail import  AuditTrail


class Task(ABC):
    def __init__(self, auditTrail=AuditTrail()):
        self.__auditTrail = auditTrail

    def execute(self):
        self.__auditTrail.record()
        self._doExecute()

    @abstractmethod
    #Oculta el metodo en esta clase(lo hace privado) pero lo hace visible para las subclases
    def _doExecute(self):pass
    
