from PySide2 import QtGui, QtWidgets, QtCore


class MenuWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MenuWindow, self).__init__()

        self.layout = QtWidgets.QGridLayout(self)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)

        self.create_buttons(self.layout)

    
    def create_buttons(self, layout_variable):
        self.button_start = QtWidgets.QPushButton("Start")
        self.button_text = QtWidgets.QPushButton("Add text")
        self.button_options = QtWidgets.QPushButton("Options")

        self.button_start.setFixedWidth(130)
        self.button_text.setFixedWidth(130)
        self.button_options.setFixedWidth(130)

        layout_variable.addWidget(self.button_start, alignment=QtCore.Qt.AlignCenter)
        layout_variable.addWidget(self.button_text, alignment=QtCore.Qt.AlignCenter)
        layout_variable.addWidget(self.button_options, alignment=QtCore.Qt.AlignCenter)


    def goto_game_window(self, widget):
        widget.setCurrentIndex(1)
        widget.adjustSize()


    def goto_add_text_window(self, widget):
        widget.setCurrentIndex(4)


    def goto_options_window(self, widget):
        widget.setCurrentIndex(2)

