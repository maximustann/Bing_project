#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

class Bing_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Bing_MainWindow, self).__init__()


if __name__ == "__main__":
    app = QtGui.QApplication([])
    bing_p = Bing_MainWindow()
    bing_p.show()
    app.exec_()
