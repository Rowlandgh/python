import sys
from PyQt5.QtWidgets import QWidget

out = sys.stdout
sys.stdout = open(r'D:\python_git\python_pyqt\QWidget.txt','w')
help(QWidget) 
sys.stdout.close() 
sys.stdout= out