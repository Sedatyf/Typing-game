from PySide2 import QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Typing Game")

        self.layout = QtWidgets.QGridLayout(self)

        self.create_display_text(self.layout)
        self.create_text_input(self.layout)


    def create_display_text(self, layout_variable):
        self.textEdit_display = QtWidgets.QTextEdit()
        self.textEdit_display.setReadOnly(True)

        layout_variable.addWidget(self.textEdit_display)


    def create_text_input(self, layout_variable):
        self.lineEdit_text = QtWidgets.QLineEdit()
        self.lineEdit_text.setPlaceholderText("Type here")

        layout_variable.addWidget(self.lineEdit_text)