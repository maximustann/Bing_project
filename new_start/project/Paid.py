#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from ui import Ui_Paid as ui_paid

class Paid_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Paid_Dialog, self).__init__()
        self.ui = ui_paid.Ui_Dialog()
        self.ui.setupUi(self)
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Paid_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
