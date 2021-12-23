from Constants import ToolType
from Tool import Tool

class Canvas():

    def mouseDown(self):
        self.currentTool.mouseDown()
       
    def mouseUp(self):
        self.currentTool.mouseUp()

    def getCurrentTool(self):
        return self.currentTool
    
    def setCurrentTool(self, currentTool):
        self.currentTool = currentTool
