from Editor import Editor
from History import History
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
