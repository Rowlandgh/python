import sys 
from PyQt5 import QtWidgets, QtCore
app = QtWidgets.QApplication(sys.argv) 
widget = QtWidgets.QWidget()
widget.resize(360,360)
widget.setWindowTitle("hello,pyqt5")

from PyQt5.QtWidgets import QWidget
print(help(QWidget))

''' widget.show()
sys.exit(app.exec_())
 '''