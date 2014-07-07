#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from ui import Ui_Discount as ui_discount

class Discount_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Discount_Dialog, self).__init__()
        self.ui = ui_discount.Ui_Dialog()
        self.ui.setupUi(self)
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Discount_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
