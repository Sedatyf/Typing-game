from PySide2 import QtWidgets, QtGui
from functools import partial

import app.game_window as gw
import app.start_menu as sm


app = QtWidgets.QApplication([])
app.setApplicationName("Typing Game")
app.setWindowIcon(QtGui.QIcon("img/icon.png"))

stack_widget = QtWidgets.QStackedWidget()

menu_window = sm.MenuWindow()
main_window = gw.GameWindow()

stack_widget.addWidget(menu_window)
stack_widget.addWidget(main_window)

menu_window.button.clicked.connect(partial(menu_window.goto_main_window, stack_widget))

stack_widget.show()

screen = app.primaryScreen()
screen_size = screen.size()
x = (screen_size.width() - menu_window.width()) / 2
y = (screen_size.height() - menu_window.height()) / 2
menu_window.move(x, y)

menu_window.show()
app.exec_()