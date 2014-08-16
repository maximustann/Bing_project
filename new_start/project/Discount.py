#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from ui import Ui_Discount as ui_discount

class Discount_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Discount_Dialog, self).__init__()
        self.ui = ui_discount.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lineEdit.textChanged.connect(self.setDiscount)
        self.ui.lineEdit_2.textChanged.connect(self.setDiscount)
        self.flag = -1
        self.ui.label_5.setText("")
        self.discount = 0
    def setDiscount(self):
        if ((self.ui.lineEdit.text() != "") and (self.ui.lineEdit_2.text() == "")):
                self.discount = 1 - float(self.ui.lineEdit.text())/100
                self.flag = 1
        elif ((self.ui.lineEdit_2.text() != "") and (self.ui.lineEdit.text() == "")):
                self.discount = - float(self.ui.lineEdit_2.text())
                self.flag = 2
        else:
            self.ui.label_5.setText("Please fill one and only one field")
    def getDiscount(self):
        return str(self.flag), str(self.discount)
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Discount_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
