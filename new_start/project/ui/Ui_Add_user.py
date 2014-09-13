# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_user.ui'
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
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(_fromUtf8("#Dialog {\n"
"   background-color: rgb(255, 255, 204);\n"
"   color: #cccccc;\n"
"}\n"
"QComboBox {\n"
"    background-color:rgb(153, 204, 255);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(34, 185, 255);\n"
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
"   color: rgb(0, 0, 0);\n"
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
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 50, 291, 161))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEdit_Name = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        self.lineEdit_Name.setFont(font)
        self.lineEdit_Name.setObjectName(_fromUtf8("lineEdit_Name"))
        self.verticalLayout_2.addWidget(self.lineEdit_Name)
        self.lineEdit_Tel = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        self.lineEdit_Tel.setFont(font)
        self.lineEdit_Tel.setObjectName(_fromUtf8("lineEdit_Tel"))
        self.verticalLayout_2.addWidget(self.lineEdit_Tel)
        self.lineEdit_Address = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        self.lineEdit_Address.setFont(font)
        self.lineEdit_Address.setObjectName(_fromUtf8("lineEdit_Address"))
        self.verticalLayout_2.addWidget(self.lineEdit_Address)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Name:", None))
        self.label_2.setText(_translate("Dialog", "Phone:", None))
        self.label_3.setText(_translate("Dialog", "Address:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

