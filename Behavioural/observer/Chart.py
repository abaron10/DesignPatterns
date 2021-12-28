from Observer import Observer

class Chart(Observer):
    def update(self,value):
        print(f"Chart got notified {value}")

