
from DialogBox import DialogBox
from ListBox import ListBox
from TextBox import TextBox
from Button import Button
class ArticlesDialogBox(DialogBox):
    def __init__(self):
        self.articlesListBox = ListBox(self)
        self.titleTextBox = TextBox(self)
        self.saveButton = Button(self)

    def simulateUserInteraction(self):
        self.articlesListBox.setSelection("Article 1")
        print(f"Textbox:{self.titleTextBox.getContent()}")
        print(f"Button:{self.saveButton.isEnabled()}")

    def changed(self,uicontrol):
        if uicontrol is self.articlesListBox:
            self.articleSelected()
        elif uicontrol is self.titleTextBox:
            self.titleChanged()

    def titleChanged(self):
        content = self.titleTextBox.getContent()
        isEmpty = content is None
        self.saveButton.setEnabled(not isEmpty)

    def articleSelected(self):
        self.titleTextBox.setContent(self.articlesListBox.getSelection())
        self.saveButton.setEnabled(True)