
from Subject import Subject
class DataSource(Subject):


    def __init__(self):
        super().__init__()
        self.value = 0.0
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
        self.notifyObservers(value)
