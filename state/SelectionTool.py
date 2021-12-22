from Tool import Tool

class SelectionTool(Tool):
    def mouseDown(self):
        print("selection icon")
    def mouseUp(self):
        print("draw a dashed rectangle")
