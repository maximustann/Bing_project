#!/usr/bin/env python

from PyQt4 import QtCore, QtGui;
from ui import Ui_Add as ui_add;
import sqlite3 as lite;
import Tyres as tyres;
import Calender as calender;
import Labour as labour;
import time;

class Add_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Add_Dialog, self).__init__()
        self.ui = ui_add.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_12.setText("Add")
        self.ui.pushButton_13.setText("Delete")
        self.conn = None
        self.cur = None
        self.connect()
        self.setTime()
        self.cur = self.conn.cursor()
        self.setMake()
        self.ui.comboBox.currentIndexChanged.connect(self.changeModel)
        self.ui.pushButton_7.clicked.connect(self.clicked_bt_Tyres)
        self.ui.pushButton_5.clicked.connect(self.clicked_bt_Calender)
        self.ui.pushButton_9.clicked.connect(self.clicked_bt_Labour)
        self.ui.pushButton_12.clicked.connect(self.clicked_bt_addLine)
        self.ui.pushButton_13.clicked.connect(self.clicked_bt_delLine)
        self.ui.tableWidget.itemChanged.connect(self.changed_table)
    def connect(self):
        try:
            self.conn = lite.connect("../Database/garage")
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

    def clicked_bt_addLine(self):
        self.ui.tableWidget.insertRow(0)
    def clicked_bt_delLine(self):
        current_row = self.ui.tableWidget.currentRow()
        self.ui.tableWidget.removeRow(current_row)

    def changed_table(self):
        current_row = self.ui.tableWidget.currentRow()
        current_column = self.ui.tableWidget.currentColumn()
        #Need to calculate Amount
        if current_column == 3:
            value = float(self.ui.tableWidget.currentItem().text()) * 1.15
            str_value = repr("%.2f" % value)[1:-1]
            item = QtGui.QTableWidgetItem(str_value)
            self.ui.tableWidget.setItem(current_row, 4, item)
            '''
            total_row = self.ui.tableWidget.rowCount()
            for i in range(total_row):
                value = float(self.ui.tableWidget.takeItem(i, 3).text())
                sub_total += value
            self.ui.label_15.setText(str(sub_total)[1:-1])
            '''
    def clicked_bt_Tyres(self):
        Dialog = tyres.Tyres_Dialog()
        Dialog.show()
        result = Dialog.exec_()

    def clicked_bt_Calender(self):
        Dialog = calender.Calender_Dialog()
        Dialog.show()
        if Dialog.exec_() == 1:
            date = Dialog.getDate()
            self.ui.pushButton_5.setText(date)

    def clicked_bt_Labour(self):
        Dialog = labour.Labour_Dialog()
        Dialog.show()
        result = Dialog.exec_()

    def setMake(self):
        self.cur.execute("SELECT name from make")
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            self.ui.comboBox.addItem(row[0])
        self.ui.comboBox.setCurrentIndex(-1)

    def changeModel(self):
        self.ui.comboBox_2.clear()
        chosen_name = self.ui.comboBox.currentText()
        self.cur.execute("SELECT name from model WHERE make_name='%s'" % chosen_name)
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            self.ui.comboBox_2.addItem(row[0])

    def setTime(self):
        self.ui.pushButton_5.setText(time.strftime("%Y-%m-%d", time.localtime(time.time())))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Add_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
