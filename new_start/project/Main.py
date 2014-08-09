#!/user/bin/env python

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
        self.ui.pushButton_2.clicked.connect(self.clicked_bt_Add)
        self.init_data()
        self.conn = None
        self.cur = None
        self.connect()
        self.cur = self.conn.cursor()
        self.ui.comboBox.currentIndexChanged.connect(self.clicked_bt_filter)
        self.ui.tableWidget.cellDoubleClicked.connect(self.clicked_table)
        self.print_table(self.convert_week(self.getday()))
    def init_data(self):
        self.invoice_no = 0
        self.customer = 1
        self.model = 2
        self.rego = 3
        self.amount_paid = 4
        self.amount_due = 5
        self.date = 6

    def clicked_table(self):
        current_row = self.ui.tableWidget.currentRow()
        package = []
        for i in xrange(7):
            package.append(self.ui.tableWidget.item(current_row, i).text())
        package.append(self.return_items(self.ui.tableWidget.item(current_row, self.invoice_no).text()))
        package.append(self.return_invoice(self.ui.tableWidget.item(current_row, self.invoice_no).text()))


        Dialog = add.Add_Dialog(package)
        Dialog.show()
        result = Dialog.exec_()
        if result == 0:
            self.clicked_bt_filter()
    def return_items(self, invoice_no):
        items = []
        self.cur.execute('select * from items where invoice_no="%s"' % invoice_no)
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            items.append(row)
        return items
    def return_invoice(self, invoice_no):
        items = []
        self.cur.execute('select * from invoice where invoice_no="%s"' % invoice_no)
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
            self.print_table(date)
        #current month
        elif self.ui.comboBox.currentIndex() == 2:
            date = self.convert_month()
            self.print_table(date)
        #all record
        elif self.ui.comboBox.currentIndex() == 3:
            self.print_table(0)
        #current week
        elif self.ui.comboBox.currentIndex() == 0:
            date = self.convert_week(self.getday())
            self.print_table(date)

    def clicked_bt_Add(self):
        Dialog = add.Add_Dialog(None)
        Dialog.show()
        result = Dialog.exec_()
        print result
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
        year = int(time.strftime("%Y", time.localtime(time.time())))
        month = int(time.strftime("%m", time.localtime(time.time())))
        day = 1
        return str(year) + '-' + str(month) + '-' + str(day)

    def print_table(self, date):
        self.delete_empty_row()
        if date == 0:
            self.cur.execute("select * from invoice")
        else:
            self.cur.execute("select * from invoice where date_in >= '%s'" % date)
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
            item = QtGui.QTableWidgetItem(str(amount_paid))
            self.ui.tableWidget.setItem(0, self.amount_paid, item)
            item = QtGui.QTableWidgetItem(str(amount_due))
            self.ui.tableWidget.setItem(0, self.amount_due, item)
            item = QtGui.QTableWidgetItem(date_in)
            self.ui.tableWidget.setItem(0, self.date, item)

    def delete_empty_row(self):
        self.ui.tableWidget.clearContents()
        for i in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.removeRow(0)

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
