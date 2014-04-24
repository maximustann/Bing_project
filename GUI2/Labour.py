# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'labour.ui'
#
# Created: Thu Apr 24 13:37:34 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(588, 459)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 71, 19))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 190, 91, 19))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 320, 71, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(40, 60, 331, 111))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 350, 331, 76))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(40, 220, 331, 76))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 250, 171, 81))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 350, 171, 81))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Labour", None))
        self.label.setText(_translate("Form", "Check:", None))
        self.label_2.setText(_translate("Form", "Fix/Repair:", None))
        self.label_3.setText(_translate("Form", "Replace:", None))
        self.pushButton.setText(_translate("Form", "Wheel Algiment", None))
        self.pushButton_2.setText(_translate("Form", "Parel Painting Labour", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

