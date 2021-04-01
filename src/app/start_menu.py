from PySide2 import QtGui, QtWidgets


class MenuWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MenuWindow, self).__init__()

        self.layout = QtWidgets.QGridLayout(self)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)

        self.create_start_button(self.layout)

    
    def create_start_button(self, layout_variable):
        self.button = QtWidgets.QPushButton("Start")

        layout_variable.addWidget(self.button)


    def goto_main_window(self, widget):
        widget.setCurrentIndex(widget.currentIndex()+1)

