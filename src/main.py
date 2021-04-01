from PySide2 import QtWidgets, QtGui
from functools import partial

import app.ui.game_window as gw
import app.ui.start_menu as sm
import app.ui.options_window as ow


app = QtWidgets.QApplication([])
app.setApplicationName("Typing Game")
app.setWindowIcon(QtGui.QIcon("img/icon.png"))

stack_widget = QtWidgets.QStackedWidget()

menu_window = sm.MenuWindow()
game_window = gw.GameWindow()
options_window = ow.OptionsWindow()

stack_widget.addWidget(menu_window)
stack_widget.addWidget(game_window)
stack_widget.addWidget(options_window)

menu_window.button_start.clicked.connect(partial(menu_window.goto_game_window, stack_widget))
menu_window.button_options.clicked.connect(partial(menu_window.goto_options_window, stack_widget))
options_window.button_back.clicked.connect(partial(options_window.back_main_menu, stack_widget))
game_window.button_back.clicked.connect(partial(game_window.back_main_menu, stack_widget))

stack_widget.show()

screen = app.primaryScreen()
screen_size = screen.size()
x = (screen_size.width() - menu_window.width()) / 2
y = (screen_size.height() - menu_window.height()) / 2
menu_window.move(x, y)

menu_window.show()
app.exec_()