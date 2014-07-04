#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from ui import Ui_Tyres as ui_tyres

class Tyres_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Tyres_Dialog, self).__init__()
        self.ui = ui_tyres.Ui_Dialog()
        self.ui.setupUi(self)
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Tyres_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
