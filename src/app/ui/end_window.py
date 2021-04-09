import sys
from PySide2 import QtWidgets, QtGui

import app.ui.game_window as gw

class EndWindow(QtWidgets.QDialog):
    def __init__(self):
        super(EndWindow, self).__init__()

        self.layout = QtWidgets.QGridLayout(self)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)

        self.create_buttons(self.layout)
        self.connect_widgets()
    
    def create_buttons(self, layout_variable):
        self.button_restart = QtWidgets.QPushButton("Restart")
        self.button_quit = QtWidgets.QPushButton("Quit")
        
        self.button_restart.setFixedWidth(100)
        self.button_quit.setFixedWidth(100)

        layout_variable.addWidget(self.button_restart, 0, 0)
        layout_variable.addWidget(self.button_quit, 1, 0)
    
    
    def connect_widgets(self):
        self.button_quit.clicked.connect(self.quit_game)


    def restart_game(self, game_window, widget):
        game_window.reset_game()
        widget.setCurrentIndex(1)


    def quit_game(self):
        sys.exit(0)