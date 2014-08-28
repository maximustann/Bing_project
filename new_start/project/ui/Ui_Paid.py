# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Paid.ui'
#
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
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(312, 172)
        Dialog.setStyleSheet(_fromUtf8("#Dialog {\n"
"   background-color: rgb(255, 255, 204);\n"
"   color: #cccccc;\n"
"}\n"
"QComboBox {\n"
"    background-color:rgb(153, 204, 255);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(0, 153, 255);\n"
"    border-width: 2px;\n"
"    border-color: rgb(117, 156, 195);\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"    alternate-background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgb(122, 163, 204);\n"
"}\n"
"QTreeView {\n"
"   background-color: #666666;\n"
"   color: #cccccc;\n"
"   alternate-background-color: #333333;\n"
"} \n"
"QListView {\n"
"   background-color: #333333;\n"
"   color: #cccccc;\n"
"}\n"
"QTextEdit {\n"
"   background-color: rgb(244, 246, 255);\n"
"   color: #cccccc;\n"
"}\n"
"QScrollBar:horizontal {\n"
"   height: 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
"   width: 20px;\n"
"}\n"
"QTabWidget::pane {\n"
"   border-top: 2px solid #cccccc;\n"
"}\n"
"QLabel {\n"
"   color: rgb(102, 102, 102); \n"
"}\n"
"\n"
"QCheckBox {\n"
"   color: white; \n"
"}\n"
"\n"
"QRadioButton{\n"
"   color:white;\n"
"}"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-130, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 40, 211, 62))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Amount Paid:  $", None))
        self.label_2.setText(_translate("Dialog", "Amount Deduct: -$", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

