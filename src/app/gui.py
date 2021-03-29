from PySide2 import QtWidgets, QtCore
import app.tools as tools

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Typing Game")

        self.layout = QtWidgets.QGridLayout(self)

        self.create_display_text(self.layout)
        self.create_text_input(self.layout)

        self.highlight_next_character()
        self.connect_widgets()


    def create_display_text(self, layout_variable):
        self.textEdit_display = QtWidgets.QTextEdit()
        self.textEdit_display.setReadOnly(True)
        self.textEdit_display.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit_display.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_display.setStyleSheet("font: 12pt")

        self.chosen_text = tools.pick_text()

        self.textEdit_display.setText(self.chosen_text)

        layout_variable.addWidget(self.textEdit_display, 0, 0)


    def create_text_input(self, layout_variable):
        self.lineEdit_user_input = QtWidgets.QLineEdit()
        self.lineEdit_user_input.setPlaceholderText("Type here")
        self.lineEdit_user_input.setFocusPolicy(QtCore.Qt.StrongFocus)

        layout_variable.addWidget(self.lineEdit_user_input, 7, 0)


    def connect_widgets(self):
        self.lineEdit_user_input.textChanged.connect(self.check_input)
        self.lineEdit_user_input.textChanged.connect(self.highlight_next_character)


    def check_input(self, input):
        list_input = list(input)
        list_character = list(self.chosen_text)
        expected_char = list_character[0:len(input)]

        if list_input == expected_char:
            self.lineEdit_user_input.setStyleSheet("background-color: white; font: 12pt")
        else:
            self.lineEdit_user_input.setStyleSheet("background-color: rgba(255, 0, 0, 0.4); font: 12pt")
    

    def highlight_next_character(self, input=""):
        list_character = list(self.chosen_text)
        char_index = len(input) + 1
        next_char = list_character[len(input):char_index]
        separator = ""
        first_part = separator.join(list_character[0:len(input)])
        bold_char = f"<b style=\"color: green\">{next_char[0]}</b>".strip()
        end_part = separator.join(list_character[char_index:])

        if(input == ""):
            self.textEdit_display.setHtml(f"<html><body><p><b style=\"color: green\">{separator.join(list_character[0])}</b>{separator.join(list_character[char_index:])}</p></body></html>")
        else:    
            self.textEdit_display.setHtml(f"<html><body><p>{first_part}{bold_char}{end_part}</p></body></html>")
