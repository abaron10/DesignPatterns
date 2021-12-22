from enum import Enum

class ToolType(Enum):
    SELECTION = 1,
    BRUSH = 2,
    ERASER = 3

    @staticmethod
    def all():
        return [a.value for a in AudioContentType]
