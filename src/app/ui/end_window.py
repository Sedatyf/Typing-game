import sys
import os
import json
from PySide2 import QtWidgets, QtGui, QtCore

import app.ui.game_window as gw
import app.tools as tools

current_path = os.path.dirname(os.path.realpath(__file__))
app_path = current_path.replace("ui", "")
sources_path = os.path.join(app_path, "sources.json")

class EndWindow(QtWidgets.QDialog):
    def __init__(self):
        super(EndWindow, self).__init__()

        self.layout = QtWidgets.QGridLayout(self)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)

        self.create_labels(self.layout)
        self.create_buttons(self.layout)
        self.connect_widgets()
    

    def create_labels(self, layout_variable):
        self.label_finish = QtWidgets.QLabel()
        self.label_finish.setTextFormat(QtCore.Qt.RichText)

        layout_variable.addWidget(self.label_finish, 0, 0, 2, 5, alignment=QtCore.Qt.AlignCenter)


    def create_buttons(self, layout_variable):
        self.button_restart = QtWidgets.QPushButton("Restart")
        self.button_quit = QtWidgets.QPushButton("Quit")
        self.button_quit.setFocusPolicy(QtCore.Qt.NoFocus)
        
        self.button_restart.setFixedWidth(100)
        self.button_quit.setFixedWidth(100)

        layout_variable.addWidget(self.button_restart, 3, 0, 1, 1)
        layout_variable.addWidget(self.button_quit, 3, 4, 1, 1)
    
    
    def connect_widgets(self):
        self.button_quit.clicked.connect(self.quit_game)


    def set_text_informations(self, text_to_retrieve):
        text_indice = tools.retrieve_text_indice(sources_path, text_to_retrieve)
       
        with open(sources_path, "r") as f:
            json_file = json.load(f)
        
        work_type = json_file["texts"][text_indice]["work_type"]
        work_title = json_file["texts"][text_indice]["title"]
        work_author = json_file["texts"][text_indice]["author"]

        self.label_finish.setText(f"<html><body><p></p>You just typed a quote from the {work_type}: <b>{work_title}</b><br/>By: {work_author}</p></body></html>")


    def restart_game(self, game_window, widget):
        game_window.reset_game()
        widget.setCurrentIndex(1)


    def quit_game(self):
        sys.exit(0)