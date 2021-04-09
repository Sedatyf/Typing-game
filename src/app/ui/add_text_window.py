from PySide2 import QtGui, QtWidgets, QtCore
import app.tools as tools


class AddTextWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AddTextWindow, self).__init__()

        self.layout = QtWidgets.QGridLayout(self)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)

        self.create_inputs(self.layout)
        self.create_buttons(self.layout)

        self.connect_widgets()

    
    def create_inputs(self, layout_variable):
        self.label_title = QtWidgets.QLabel("Title")
        self.le_title = QtWidgets.QLineEdit()

        self.label_author = QtWidgets.QLabel("Author")
        self.le_author = QtWidgets.QLineEdit()

        self.label_text = QtWidgets.QLabel("Text")
        self.le_text = QtWidgets.QLineEdit()

        self.label_type = QtWidgets.QLabel("Type")
        self.cb_type = QtWidgets.QComboBox()

        self.cb_type.addItems(["", "book", "game", "movie", "song", "other"])

        layout_variable.addWidget(self.label_title, 0, 0, 1, 5)
        layout_variable.addWidget(self.le_title, 1, 0, 1, 5)
        layout_variable.addWidget(self.label_author, 2, 0, 1, 5)
        layout_variable.addWidget(self.le_author, 3, 0, 1, 5)
        layout_variable.addWidget(self.label_text, 4, 0, 1, 5)
        layout_variable.addWidget(self.le_text, 5, 0, 1, 5)
        layout_variable.addWidget(self.label_type, 6, 0, 1, 5)
        layout_variable.addWidget(self.cb_type, 7, 0, 1, 5)


    def create_buttons(self, layout_variable):
        self.button_back = QtWidgets.QPushButton("Back")
        self.button_save = QtWidgets.QPushButton("Save")

        layout_variable.addWidget(self.button_back, 8, 3, 1, 1)
        layout_variable.addWidget(self.button_save, 8, 4, 1, 1)


    def connect_widgets(self):
        self.button_save.clicked.connect(self.save_text)


    def save_text(self):
        saved_title = self.le_title.text()
        saved_author = self.le_author.text()
        saved_text = self.le_text.text()
        saved_type = self.cb_type.currentText()

        if saved_title == "" or saved_author == "" or saved_text == "" or saved_type == "":
            self.show_error_message()
            return

        tools.write_to_sources(saved_title, saved_author, saved_text, saved_type)
        self.show_success_message()
        self.clear_fields()


    def show_success_message(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)

        msgBox.setText("Your submission has been saved!")
        msgBox.setWindowTitle("Success!")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()


    def show_error_message(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)

        msgBox.setText("All the fields have to be filled!")
        msgBox.setWindowTitle("Error!")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()


    def clear_fields(self):
        self.le_title.clear()
        self.le_author.clear()
        self.le_text.clear()
        self.cb_type.setCurrentText("")

    def goto_main_window(self, widget):
        widget.setCurrentIndex(0)
