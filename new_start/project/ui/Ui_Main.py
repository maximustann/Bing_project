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
        self.pushButton_Add = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        self.pushButton_Add.setFont(font)
        self.pushButton_Add.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_Add.setObjectName(_fromUtf8("pushButton_Add"))
        self.horizontalLayout.addWidget(self.pushButton_Add)
        self.pushButton_Del = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        self.pushButton_Del.setFont(font)
        self.pushButton_Del.setObjectName(_fromUtf8("pushButton_Del"))
        self.horizontalLayout.addWidget(self.pushButton_Del)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_main = QtGui.QWidget()
        self.tab_main.setObjectName(_fromUtf8("tab_main"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_main)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.tableWidget_Main = QtGui.QTableWidget(self.tab_main)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.tableWidget_Main.setFont(font)
        self.tableWidget_Main.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget_Main.setStyleSheet(_fromUtf8("#Dialog {\n"
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
        self.tableWidget_Main.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableWidget_Main.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableWidget_Main.setLineWidth(1)
        self.tableWidget_Main.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Main.setTabKeyNavigation(True)
        self.tableWidget_Main.setProperty("showDropIndicator", True)
        self.tableWidget_Main.setShowGrid(True)
        self.tableWidget_Main.setObjectName(_fromUtf8("tableWidget_Main"))
        self.tableWidget_Main.setColumnCount(7)
        self.tableWidget_Main.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Main.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Main.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Main.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Main.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Main.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Main.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Main.setHorizontalHeaderItem(6, item)
        self.tableWidget_Main.horizontalHeader().setVisible(True)
        self.tableWidget_Main.horizontalHeader().setHighlightSections(False)
        self.tableWidget_Main.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.tableWidget_Main, 1, 0, 1, 3)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.comboBox_filter = QtGui.QComboBox(self.tab_main)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.comboBox_filter.setFont(font)
        self.comboBox_filter.setObjectName(_fromUtf8("comboBox_filter"))
        self.comboBox_filter.addItem(_fromUtf8(""))
        self.comboBox_filter.addItem(_fromUtf8(""))
        self.comboBox_filter.addItem(_fromUtf8(""))
        self.comboBox_filter.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_filter, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.lineEdit_main_search = QtGui.QLineEdit(self.tab_main)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.lineEdit_main_search.setFont(font)
        self.lineEdit_main_search.setObjectName(_fromUtf8("lineEdit_main_search"))
        self.gridLayout_6.addWidget(self.lineEdit_main_search, 0, 1, 1, 1)
        self.pushButton_main_search = QtGui.QPushButton(self.tab_main)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.pushButton_main_search.setFont(font)
        self.pushButton_main_search.setObjectName(_fromUtf8("pushButton_main_search"))
        self.gridLayout_6.addWidget(self.pushButton_main_search, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab_main, _fromUtf8(""))
        self.tab_customer = QtGui.QWidget()
        self.tab_customer.setObjectName(_fromUtf8("tab_customer"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_customer)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit_cust_search = QtGui.QLineEdit(self.tab_customer)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.lineEdit_cust_search.setFont(font)
        self.lineEdit_cust_search.setObjectName(_fromUtf8("lineEdit_cust_search"))
        self.horizontalLayout_2.addWidget(self.lineEdit_cust_search)
        self.pushButton_cust_search = QtGui.QPushButton(self.tab_customer)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.pushButton_cust_search.setFont(font)
        self.pushButton_cust_search.setObjectName(_fromUtf8("pushButton_cust_search"))
        self.horizontalLayout_2.addWidget(self.pushButton_cust_search)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.tableWidget_Customer = QtGui.QTableWidget(self.tab_customer)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.tableWidget_Customer.setFont(font)
        self.tableWidget_Customer.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Customer.setObjectName(_fromUtf8("tableWidget_Customer"))
        self.tableWidget_Customer.setColumnCount(3)
        self.tableWidget_Customer.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Customer.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Customer.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Customer.setHorizontalHeaderItem(2, item)
        self.tableWidget_Customer.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_Customer.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tableWidget_Customer, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_customer, _fromUtf8(""))
        self.tab_paid = QtGui.QWidget()
        self.tab_paid.setObjectName(_fromUtf8("tab_paid"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_paid)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tableWidget_Paid = QtGui.QTableWidget(self.tab_paid)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.tableWidget_Paid.setFont(font)
        self.tableWidget_Paid.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Paid.setObjectName(_fromUtf8("tableWidget_Paid"))
        self.tableWidget_Paid.setColumnCount(2)
        self.tableWidget_Paid.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Paid.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Paid.setHorizontalHeaderItem(1, item)
        self.tableWidget_Paid.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_Paid.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.tableWidget_Paid, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_paid, _fromUtf8(""))
        self.tab_unpaid = QtGui.QWidget()
        self.tab_unpaid.setObjectName(_fromUtf8("tab_unpaid"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_unpaid)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.tableWidget_Unpaid = QtGui.QTableWidget(self.tab_unpaid)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.tableWidget_Unpaid.setFont(font)
        self.tableWidget_Unpaid.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Unpaid.setObjectName(_fromUtf8("tableWidget_Unpaid"))
        self.tableWidget_Unpaid.setColumnCount(4)
        self.tableWidget_Unpaid.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Unpaid.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Unpaid.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Unpaid.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Unpaid.setHorizontalHeaderItem(3, item)
        self.tableWidget_Unpaid.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_Unpaid.verticalHeader().setVisible(False)
        self.gridLayout_5.addWidget(self.tableWidget_Unpaid, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_unpaid, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Garage Management", None))
        self.pushButton_Add.setText(_translate("Dialog", "Add", None))
        self.pushButton_Del.setText(_translate("Dialog", "Delete", None))
        item = self.tableWidget_Main.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Invoice No.", None))
        item = self.tableWidget_Main.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Customer", None))
        item = self.tableWidget_Main.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Model", None))
        item = self.tableWidget_Main.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Rego", None))
        item = self.tableWidget_Main.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Amount Paid", None))
        item = self.tableWidget_Main.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Amount Due", None))
        item = self.tableWidget_Main.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Date", None))
        self.comboBox_filter.setItemText(0, _translate("Dialog", "Current Week", None))
        self.comboBox_filter.setItemText(1, _translate("Dialog", "Current Day", None))
        self.comboBox_filter.setItemText(2, _translate("Dialog", "Current Month", None))
        self.comboBox_filter.setItemText(3, _translate("Dialog", "All record", None))
        self.pushButton_main_search.setText(_translate("Dialog", "Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), _translate("Dialog", "Main", None))
        self.pushButton_cust_search.setText(_translate("Dialog", "Search", None))
        item = self.tableWidget_Customer.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name", None))
        item = self.tableWidget_Customer.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Contact", None))
        item = self.tableWidget_Customer.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Address", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_customer), _translate("Dialog", "Customer", None))
        item = self.tableWidget_Paid.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Customer", None))
        item = self.tableWidget_Paid.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Invoice No.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_paid), _translate("Dialog", "Paid", None))
        item = self.tableWidget_Unpaid.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Customer", None))
        item = self.tableWidget_Unpaid.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Amount Paid", None))
        item = self.tableWidget_Unpaid.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Amount Due", None))
        item = self.tableWidget_Unpaid.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Invoice No.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_unpaid), _translate("Dialog", "Unpaid", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

