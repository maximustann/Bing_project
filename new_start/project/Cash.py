#!/bin/env python

from PyQt4 import QtCore, QtGui
from ui import Ui_Cash as ui_cash

class Cash_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Cash_Dialog, self).__init__()
        self.ui = ui_cash.Ui_Dialog()
        self.ui.setupUi(self)
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Cash_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
