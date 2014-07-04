# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calender.ui'
#
# Created: Fri Jul  4 16:05:33 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Calender):
        Calender.setObjectName(_fromUtf8("Calender"))
        Calender.resize(400, 300)
        self.calendarWidget = QtGui.QCalendarWidget(Calender)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))

        self.retranslateUi(Calender)
        QtCore.QMetaObject.connectSlotsByName(Calender)

    def retranslateUi(self, Calender):
        Calender.setWindowTitle(_translate("Calender", "Dialog", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Calender = QtGui.QDialog()
    ui = Ui_Calender()
    ui.setupUi(Calender)
    Calender.show()
    sys.exit(app.exec_())

