# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
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
        Dialog.resize(769, 723)
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
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.tableWidget = QtGui.QTableWidget(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.tableWidget.setFont(font)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget.setStyleSheet(_fromUtf8("#Dialog {\n"
"   background-color: beige;\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    background-color: palegoldenrod;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: khaki;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #d0d67c;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font: bold;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"   font: normal;\n"
"}\n"
"\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c; \n"
"    selection-background-color: #C19A6B;\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"    border-width: 3px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame ... */\n"
"QLabel {\n"
"    border: none;\n"
"    padding: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"/* A QToolTip is a QLabel ... */\n"
"QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    button-layout: 0;\n"
"}"))
        self.tableWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.tableWidget, 1, 0, 1, 3)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.comboBox = QtGui.QComboBox(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.comboBox.setFont(font)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_6.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_6.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_4 = QtGui.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.tableWidget_2 = QtGui.QTableWidget(self.tab_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tableWidget_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tableWidget_3 = QtGui.QTableWidget(self.tab_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.tableWidget_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.tableWidget_4 = QtGui.QTableWidget(self.tab_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.tableWidget_4.setFont(font)
        self.tableWidget_4.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.gridLayout_5.addWidget(self.tableWidget_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Garage Management", None))
        self.pushButton_2.setText(_translate("Dialog", "Add", None))
        self.pushButton.setText(_translate("Dialog", "Delete", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Invoice No.", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Customer", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Model", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Rego", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Amount Paid", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Amount Due", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Date", None))
        self.comboBox.setItemText(0, _translate("Dialog", "Current Week", None))
        self.comboBox.setItemText(1, _translate("Dialog", "Current Day", None))
        self.comboBox.setItemText(2, _translate("Dialog", "Current Month", None))
        self.comboBox.setItemText(3, _translate("Dialog", "All record", None))
        self.pushButton_3.setText(_translate("Dialog", "Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Main", None))
        self.pushButton_4.setText(_translate("Dialog", "Search", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Contact", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Address", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Customer", None))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Customer", None))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Invoice No.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Paid", None))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Customer", None))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Amount Paid", None))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Amount Due", None))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Invoice No.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Unpaid", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

