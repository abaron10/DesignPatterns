from Canvas import Canvas
from SelectionTool import SelectionTool
from BrushTool import  BrushTool

# State es un patrón de diseño de comportamiento que permite a un objeto alterar su 
# comportamiento cuando su estado interno cambia. Parece como si el objeto cambiara
# su clase.

if __name__ == '__main__':
    canvas = Canvas()
    canvas.setCurrentTool(BrushTool())
    canvas.mouseDown()
    canvas.mouseUp()



