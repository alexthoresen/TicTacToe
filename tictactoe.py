from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def Window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(xpos, ypos, w, h)