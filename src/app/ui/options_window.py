from PySide2 import QtGui, QtWidgets, QtCore

class OptionsWindow(QtWidgets.QDialog):
    def __init__(self):
        super(OptionsWindow, self).__init__()

        self.layout = QtWidgets.QGridLayout(self)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)

        self.create_buttons(self.layout)

    
    def create_buttons(self, layout_variable):
        self.button_back = QtWidgets.QPushButton("<")
        self.button_back.setFixedWidth(30)

        layout_variable.addWidget(self.button_back, 0, 0)
    

    def back_main_menu(self, widget):
         widget.setCurrentIndex(0)