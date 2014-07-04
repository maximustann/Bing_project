#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from ui import Ui_Calender as ui_calender

class Calender_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Calender_Dialog, self).__init__()
        self.ui = ui_calender.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.calendarWidget.clicked.connect(self.setDate)
    def setDate(self):
        self.date = self.ui.calendarWidget.selectedDate().toString("yyyy-M-d")
        super(Calender_Dialog, self).accept()
    def getDate(self):
        return self.date
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Calender_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
