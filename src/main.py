from PySide2 import QtWidgets
import app.gui as gui

app = QtWidgets.QApplication([])
window = gui.MainWindow()
window.show()
app.exec_()