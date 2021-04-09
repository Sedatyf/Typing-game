from PySide2 import QtWidgets, QtGui
from functools import partial

import app.ui.game_window as gw
import app.ui.start_menu as sm
import app.ui.options_window as ow
import app.ui.end_window as ew
import app.ui.add_text_window as atw


def add_widget():
    stack_widget.addWidget(menu_window)
    stack_widget.addWidget(game_window)
    stack_widget.addWidget(options_window)
    stack_widget.addWidget(end_window)
    stack_widget.addWidget(add_text_window)


def connect_object():
    menu_window.button_start.clicked.connect(partial(menu_window.goto_game_window, stack_widget))
    menu_window.button_text.clicked.connect(partial(menu_window.goto_add_text_window, stack_widget))
    menu_window.button_options.clicked.connect(partial(menu_window.goto_options_window, stack_widget))

    add_text_window.button_back.clicked.connect(partial(add_text_window.goto_main_window, stack_widget))

    options_window.button_back.clicked.connect(partial(options_window.back_main_menu, stack_widget))

    game_window.button_back.clicked.connect(partial(game_window.back_main_menu, stack_widget))
    game_window.lineEdit_user_input.textChanged.connect(partial(game_window.go_to_end, stack_widget))

    end_window.button_restart.clicked.connect(partial(end_window.restart_game, game_window, stack_widget))


def set_window_pos():
    screen = app.primaryScreen()
    screen_size = screen.size()
    x = (screen_size.width() - menu_window.width()) / 2
    y = (screen_size.height() - menu_window.height()) / 2
    menu_window.move(x, y)


app = QtWidgets.QApplication([])
app.setApplicationName("Typing Game")
app.setWindowIcon(QtGui.QIcon("img/icon.png"))

stack_widget = QtWidgets.QStackedWidget()

menu_window = sm.MenuWindow()
game_window = gw.GameWindow()
options_window = ow.OptionsWindow()
end_window = ew.EndWindow()
add_text_window = atw.AddTextWindow()

add_widget()

connect_object()

stack_widget.show()

set_window_pos()

menu_window.show()
app.exec_()