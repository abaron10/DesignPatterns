from ImageStorage import ImageStorage
from JpegCompressor import JpegCompressor
from BlackAndWhiteFilter import  BlackAndWhiteFilter

# Strategy . Se clasifica como patrón de comportamiento porque determina cómo se 
# debe realizar el intercambio de mensajes entre diferentes objetos para resolver 
# una tarea.
#La diferencia entre state  y strategy es que el state puede tener un solo estado interno , mientras
#que el strategy puede interacturar con varios stados que se comunican con varias estrategias
#Usa el principio de POLIMORFISMO

if __name__ == '__main__':
    imgs = ImageStorage(JpegCompressor(),BlackAndWhiteFilter())    
    imgs.store("a")