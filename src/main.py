from PySide2 import QtWidgets, QtGui
import app.gui as gui

app = QtWidgets.QApplication([])
window = gui.MainWindow()

screen = app.primaryScreen()
screen_size = screen.size()
x = (screen_size.width() - window.width()) / 2
y = (screen_size.height() - window.height()) / 2
window.move(x, y)

window.show()
app.exec_()