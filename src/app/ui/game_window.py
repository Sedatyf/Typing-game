from PySide2 import QtGui, QtWidgets, QtCore
import app.tools as tools

class GameWindow(QtWidgets.QDialog):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.chosen_text = tools.pick_text()

        self.layout = QtWidgets.QGridLayout(self)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)

        self.create_buttons(self.layout)
        self.create_progress_bar(self.layout)
        self.create_display_text(self.layout)
        self.create_text_input(self.layout)

        self.highlight_next_character()
        self.connect_widgets()


    def create_buttons(self, layout_variable):
        self.button_back = QtWidgets.QPushButton("<")
        self.button_back.setFixedWidth(30)
        self.button_back.setFocusPolicy(QtCore.Qt.NoFocus)

        layout_variable.addWidget(self.button_back, 0, 0, 1, 1)


    def create_display_text(self, layout_variable):
        self.label_display = QtWidgets.QLabel()
        self.label_display.setTextFormat(QtCore.Qt.RichText) # accept html text
        self.label_display.setWordWrap(True) # Multiline label
        self.label_display.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        self.label_display.setMaximumWidth(800)

        current_width = self.label_display.width()
        self.label_display.setFixedWidth(current_width + 20)

        self.label_display.setText(self.chosen_text)
        
        layout_variable.addWidget(self.label_display, 2, 0, 1, 5)


    def create_text_input(self, layout_variable):
        self.lineEdit_user_input = QtWidgets.QLineEdit()
        self.lineEdit_user_input.setPlaceholderText("Type here")
        self.lineEdit_user_input.setFocusPolicy(QtCore.Qt.StrongFocus)

        layout_variable.addWidget(self.lineEdit_user_input, 3, 0 , 1, 5)


    def create_progress_bar(self, layout_variable):
        self.max_value = len(list(self.chosen_text))

        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(self.max_value)

        layout_variable.addWidget(self.progress_bar, 1, 0, 1, 5)


    def connect_widgets(self):
        self.lineEdit_user_input.textChanged.connect(self.check_input)
        self.lineEdit_user_input.textChanged.connect(self.highlight_next_character)
        self.lineEdit_user_input.textChanged.connect(self.update_progress_bar)
        self.button_back.clicked.connect(self.reset_game)


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
            self.label_display.setText(f"<html><body><p><b style=\"color: green\">{separator.join(list_character[0])}</b>{separator.join(list_character[char_index:])}</p></body></html>")
        else:    
            self.label_display.setText(f"<html><body><p>{first_part}{bold_char}{end_part}</p></body></html>")
 

    def update_progress_bar(self, input):
        current_progress = len(list(input))
        self.progress_bar.setValue(current_progress)


    def back_main_menu(self, widget):
         widget.setCurrentIndex(0)


    def go_to_end(self, widget, input):
        if input == self.chosen_text:
            widget.setCurrentIndex(3)


    def reset_game(self):
        self.lineEdit_user_input.clear()
        self.chosen_text = tools.pick_text()
        self.max_value = len(list(self.chosen_text))
        self.progress_bar.setMaximum(self.max_value)

        self.label_display.setText(self.chosen_text)

        lines = round(len(self.chosen_text) / 72)
        self.label_display.setFixedHeight(lines * 20)
        
