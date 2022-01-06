from abc import  ABC , abstractmethod
class Handler(ABC):
    
    def __init__(self,next):
        self.next = next

    def handle(self,request):
        if self.doHandle(request):
            return
        if self.next is not None:
            self.next.handle(request)

    @abstractmethod
    def doHandle(self,request):pass
