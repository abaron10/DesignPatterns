from Observer import Observer

class SpreadSheet(Observer):
    def update(self,value):
        print(f"Spradsheet got notified: {value}")

