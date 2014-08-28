# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Discount.ui'
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
        Dialog.resize(365, 295)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(24)
        Dialog.setFont(font)
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
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(170, 70, 24, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 160, 191, 20))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 200, 188, 72))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.buttonBox = QtGui.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.layoutWidget1 = QtGui.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(120, 100, 171, 30))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.layoutWidget2 = QtGui.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(61, 41, 245, 30))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Discount", None))
        self.label_3.setText(_translate("Dialog", "OR", None))
        self.pushButton.setText(_translate("Dialog", "Delete Discount", None))
        self.label_4.setText(_translate("Dialog", "-$:", None))
        self.label.setText(_translate("Dialog", "Discount:", None))
        self.label_2.setText(_translate("Dialog", "%", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

