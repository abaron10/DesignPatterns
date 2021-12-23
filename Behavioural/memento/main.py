from Editor import Editor
from History import History

# Memento es un patrón de diseño de comportamiento que te permite guardar 
# y restaurar el estado previo de un objeto sin revelar los detalles de su 
# implementación.

if __name__ == '__main__':
    editor = Editor()
    history = History()

    editor.setContent("a")
    history.push(editor.createState())
    editor.setContent("b")
    history.push(editor.createState())
    editor.setContent("c")
    editor.restore(history.pop())
    print(editor.getContent())
