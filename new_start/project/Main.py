#!/bin/env python

from PyQt4 import QtCore, QtGui

from ui import Ui_Main as ui_main
import sqlite3 as lite;
import sys;
import os;
import Add as add;
import datetime
import time

class Main_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Main_Dialog, self).__init__()
        self.ui = ui_main.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.clicked_bt_Main_Add)
        self.ui.pushButton.clicked.connect(self.clicked_bt_Main_Del)
        self.init_data()
        self.conn = None
        self.cur = None
        self.connect()
        self.cur = self.conn.cursor()
        self.ui.comboBox.currentIndexChanged.connect(self.clicked_bt_filter)
        self.ui.tableWidget.cellDoubleClicked.connect(self.clicked_table)
        self.print_paid_table()
        self.print_main_table(self.convert_week(self.getday()))
        self.print_customer_table()
        self.print_unpaid_table()
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tabWidget.currentChanged.connect(self.clicked_change_tab)
        self.ui.tabWidget.setCurrentIndex(self.main_tab)
    def init_data(self):
        self.customer_name = 0
        self.tel = 1
        self.address = 2
        self.invoice_no = 0
        self.customer = 1
        self.model = 2
        self.rego = 3
        self.amount_paid = 4
        self.amount_due = 5
        self.date = 6
        self.main_tab = 0
        self.customer_tab = 1
        self.paid_tab = 2
        self.unpaid_tab = 3

    def clicked_change_tab(self):
        index = self.ui.tabWidget.currentIndex()
        self.ui.pushButton.clicked.disconnect()
        self.ui.pushButton_2.clicked.disconnect()
        if index == self.main_tab:
            self.ui.pushButton.clicked.connect(self.clicked_bt_Main_Del)
            self.ui.pushButton_2.clicked.connect(self.clicked_bt_Main_Add)
        elif index == self.customer_tab:
            self.print_customer_table()
            self.ui.pushButton.clicked.connect(self.clicked_bt_Customer_Del)
            self.ui.pushButton_2.clicked.connect(self.clicked_bt_Customer_Add)
        elif index == self.paid_tab:
            self.print_paid_table()
            self.ui.pushButton.clicked.connect(self.clicked_bt_Paid_Del)
            self.ui.pushButton_2.clicked.connect(self.clicked_bt_Paid_Add)
        elif index == self.unpaid_tab:
            self.print_unpaid_table()
            self.ui.pushButton.clicked.connect(self.clicked_bt_Unpaid_Del)
            self.ui.pushButton_2.clicked.connect(self.clicked_bt_Unpaid_Add)

    def clicked_bt_Customer_Del(self):
        print "Customer Delete"
    def clicked_bt_Paid_Del(self):
        print "Paid Delete"
    def clicked_bt_Unpaid_Del(self):
        print "Unpaid Delete"
    def clicked_bt_Customer_Add(self):
        print "Customer Add"
    def clicked_bt_Paid_Add(self):
        print "Paid Add"
    def clicked_bt_Unpaid_Add(self):
        print "UnPaid Add"

    def clicked_bt_Main_Del(self):
        current_row = self.ui.tableWidget.currentRow()
        if current_row == -1:
            current_row = 0
        invoice_no_item = self.ui.tableWidget.item(current_row, self.invoice_no)
        if invoice_no_item == None:
            return
        invoice_no = invoice_no_item.text()
        self.cur.execute("DELETE FROM invoice WHERE invoice_no='%s'" % invoice_no)
        self.cur.execute("DELETE FROM items WHERE invoice_no='%s'" % invoice_no)
        self.conn.commit()
        self.ui.tableWidget.removeRow(current_row)

    def clicked_table(self):
        current_row = self.ui.tableWidget.currentRow()
        package = []
        for i in xrange(7):
            package.append(self.ui.tableWidget.item(current_row, i).text())
        package.append(self.return_items(self.ui.tableWidget.item(current_row, self.invoice_no).text()))
        package.append(self.return_invoice(self.ui.tableWidget.item(current_row, self.invoice_no).text()))


        Dialog = add.Add_Dialog(package)
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.show()
        result = Dialog.exec_()
        if result == 0:
            self.clicked_bt_filter()
    def return_items(self, invoice_no):
        items = []
        self.cur.execute('SELECT * FROM items WHERE invoice_no="%s"' % invoice_no)
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            items.append(row)
        return items
    def return_invoice(self, invoice_no):
        items = []
        self.cur.execute('SELECT * FROM invoice WHERE invoice_no="%s"' % invoice_no)
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            items.append(row)
        return items


    def clicked_bt_filter(self):
        #current day
        if self.ui.comboBox.currentIndex() == 1:
            date = self.current_day()
            self.print_main_table(date)
        #current month
        elif self.ui.comboBox.currentIndex() == 2:
            date = self.convert_month()
            self.print_main_table(date)
        #all record
        elif self.ui.comboBox.currentIndex() == 3:
            self.print_main_table(0)
        #current week
        elif self.ui.comboBox.currentIndex() == 0:
            date = self.convert_week(self.getday())
            self.print_main_table(date)

    def clicked_bt_Main_Add(self):
        Dialog = add.Add_Dialog(None)
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.show()
        result = Dialog.exec_()
        if result == 0:
            self.clicked_bt_filter()
    def connect(self):
        try:
            self.conn = lite.connect("../Database/garage")
        except lite.Error, e:
            self.write_log(e.args[0])
            sys.exit(1)

    def getday(self):
        year = int(time.strftime("%Y", time.localtime(time.time())))
        month = int(time.strftime("%m", time.localtime(time.time())))
        day = int(time.strftime("%d", time.localtime(time.time())))
        return int(datetime.date(year, month, day).weekday())

    def convert_week(self, weekday):
        day = int(time.strftime("%d", time.localtime(time.time())))
        month = int(time.strftime("%m", time.localtime(time.time())))

        if day < 10:
            day = '0' + str(day)
        if month < 10:
            month = '0' + str(month)

        if int(day) - weekday < 0:
            month = int(time.strftime("%m", time.localtime(time.time()))) - 1
            if month == 0:
                month = 12
            if month < 10:
                month = '0' + str(month)
        else:
            day = int(day)
            day -= weekday
        if day < 10:
            day = '0' + str(day)
        year = str(time.strftime("%Y", time.localtime(time.time())))
        return year + '-' + str(month) + '-' + str(day)

    def current_day(self):
        return time.strftime("%Y-%m-%d", time.localtime(time.time()))

    def convert_month(self):
        year = time.strftime("%Y", time.localtime(time.time()))
        month = time.strftime("%m", time.localtime(time.time()))
        day = '01'
        return year + '-' + month + '-' + day

    def print_unpaid_table(self):
        self.delete_empty_row(3)
        self.cur.execute("SELECT name, amount_paid, amount_due, invoice_no FROM invoice WHERE\
                amount_due != '0.0'")
        while True:
            row  = self.cur.fetchone()
            if row == None:
                break
            name = row[0]
            amount_paid = row[1]
            amount_due = row[2]
            invoice_no = row[3]
            self.ui.tableWidget_4.insertRow(0)
            item = QtGui.QTableWidgetItem(name)
            self.ui.tableWidget_4.setItem(0, self.customer_name, item)

            item = QtGui.QTableWidgetItem(str ("%.2f") % amount_paid)
            #unpaid table is different from main table
            self.ui.tableWidget_4.setItem(0, self.amount_paid - 3, item)

            item = QtGui.QTableWidgetItem(str ("%.2f") % amount_due)
            #unpaid table is different from main table
            self.ui.tableWidget_4.setItem(0, self.amount_due - 3, item)

            item = QtGui.QTableWidgetItem(str(invoice_no))
            #unpaid table is different from main table
            self.ui.tableWidget_4.setItem(0, self.invoice_no + 3, item)
    def print_customer_table(self):
        self.delete_empty_row(2)
        self.cur.execute("SELECT name, tel, Address FROM customer")
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            name = row[0]
            tel = row[1]
            addr = row[2]
            self.ui.tableWidget_2.insertRow(0)
            item = QtGui.QTableWidgetItem(name)
            self.ui.tableWidget_2.setItem(0, self.customer_name, item)
            item = QtGui.QTableWidgetItem(tel)
            self.ui.tableWidget_2.setItem(0, self.tel, item)
            item = QtGui.QTableWidgetItem(addr)
            self.ui.tableWidget_2.setItem(0, self.address, item)

    def print_main_table(self, date):
        self.delete_empty_row(0)
        if date == 0:
            self.cur.execute("SELECT * FROM invoice")
        else:
            self.cur.execute("SELECT * FROM  invoice WHERE date_in >= '%s'" % date)
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            invoice_no = row[0]
            date_in = row[1]
            tel = row[2]
            name = row[3]
            rego = row[4]
            money_in = row[5]
            amount_paid = row[6]
            amount_due = row[7]
            note = row[8]
            service = row[9]
            labour = row[10]
            model = row[11]
            self.ui.tableWidget.insertRow(0)
            item = QtGui.QTableWidgetItem(str(invoice_no))
            self.ui.tableWidget.setItem(0, self.invoice_no, item)
            item = QtGui.QTableWidgetItem(name)
            self.ui.tableWidget.setItem(0, self.customer, item)
            item = QtGui.QTableWidgetItem(model)
            self.ui.tableWidget.setItem(0, self.model, item)
            item = QtGui.QTableWidgetItem(rego)
            self.ui.tableWidget.setItem(0, self.rego, item) 
            item = QtGui.QTableWidgetItem(str("%.2f") % amount_paid)
            self.ui.tableWidget.setItem(0, self.amount_paid, item)
            item = QtGui.QTableWidgetItem(str("%.2f") % amount_due)
            self.ui.tableWidget.setItem(0, self.amount_due, item)
            item = QtGui.QTableWidgetItem(date_in)
            self.ui.tableWidget.setItem(0, self.date, item)

    def print_paid_table(self):
        self.delete_empty_row(1)
        self.cur.execute("SELECT name, invoice_no FROM invoice WHERE\
                amount_due == '0.0'")
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            name = row[0]
            invoice_no = row[1]
            self.ui.tableWidget_3.insertRow(0)
            item = QtGui.QTableWidgetItem(name)
            self.ui.tableWidget_3.setItem(0, self.customer - 1, item)
            item = QtGui.QTableWidgetItem(str(invoice_no))
            self.ui.tableWidget_3.setItem(0, self.invoice_no + 1, item)

    def delete_empty_row(self, table_number):
        if table_number == 0:
            self.ui.tableWidget.clearContents()
            for i in range(self.ui.tableWidget.rowCount()):
                self.ui.tableWidget.removeRow(0)
        elif table_number == 1:
            self.ui.tableWidget_3.clearContents()
            for i in range(self.ui.tableWidget_3.rowCount()):
                self.ui.tableWidget_3.removeRow(0)
        elif table_number == 2:
            self.ui.tableWidget_2.clearContents()
            for i in range(self.ui.tableWidget_2.rowCount()):
                self.ui.tableWidget_2.removeRow(0)
        else:
            self.ui.tableWidget_4.clearContents()
            for i in range(self.ui.tableWidget_4.rowCount()):
                self.ui.tableWidget_4.removeRow(0)

    def write_log(self, string):
        my_time = None
        fd = open("../Database/log/log.txt", "a")
        my_time = str(time.strftime("%Y-%m-%d-%I:%M", time.localtime(time.time())))
        fd.write(string + "\t" + my_time + "\n")
        fd.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Dialog = Main_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
