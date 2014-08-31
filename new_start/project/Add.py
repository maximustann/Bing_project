#!/bin/env python

from PyQt4 import QtCore, QtGui, QtWebKit;
from ui import Ui_Add as ui_add;
import sqlite3 as lite;
import Tyres as tyres;
import Calender as calender;
import Labour as labour;
import Discount as discount;
import Paid as paid_file;
import Cash as cash;
import time;
import log_keeper
import os;
import edit_file
from random import randint;


class Add_Dialog(QtGui.QDialog):
    def __init__(self, package):
        super(Add_Dialog, self).__init__()
        self.ui = ui_add.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_12.setText("Add")
        self.ui.pushButton_13.setText("Delete")
        self.ui.label_11.setText("0")
        self.ui.label_15.setText("0")
        self.ui.label_16.setText("0")
        self.ui.label_17.setText("0")
        self.ui.lineEdit_8.setText("0.00")
        self.ui.lineEdit_9.setText("0.00")
        self.init_data()
        self.conn = None
        self.cur = None
        self.connect()
        self.setTime()
        self.cur = self.conn.cursor()
        self.setMake()
        self.init_invoice()
        self.ui.lineEdit_3.setText(self.random_Tel_Num())
        self.ui.comboBox.currentIndexChanged.connect(self.changeModel)
        self.ui.comboBox_5.currentIndexChanged.connect(self.changeService)
        self.ui.pushButton_2.clicked.connect(self.clicked_bt_print)
        self.ui.pushButton_7.clicked.connect(self.clicked_bt_Tyres)
        self.ui.pushButton_5.clicked.connect(self.clicked_bt_Calender)
        self.ui.pushButton_9.clicked.connect(self.clicked_bt_Labour)
        self.ui.pushButton_17.clicked.connect(self.clicked_bt_Discount)
        self.ui.pushButton_14.clicked.connect(self.clicked_bt_fullPayment)
        self.ui.pushButton_15.clicked.connect(self.clicked_bt_Paid)
        self.ui.pushButton_16.clicked.connect(self.clicked_bt_Cash)
        self.ui.pushButton_12.clicked.connect(self.clicked_bt_addLine)
        self.ui.pushButton_13.clicked.connect(self.clicked_bt_delLine)
        self.ui.pushButton_3.clicked.connect(self.clicked_bt_preview)
        self.ui.lineEdit_8.textChanged.connect(self.autoChangeText)
        self.ui.lineEdit_8.cursorPositionChanged.connect(self.autoChangeText)

        self.ui.tableWidget.itemChanged.connect(self.changed_table)
        self.ui.comboBox_3.currentIndexChanged.connect(self.wof_comboBox)
        self.ui.tableWidget.setColumnWidth(1, 300)
        if package != None:
            self.initialize(package)

    def random_Tel_Num(self):
        while True:
            num = str (randint(0, 99999))
            self.cur.execute('SELECT tel FROM customer WHERE tel = "%s"' % num )
            while True:
                telNum = self.cur.fetchone()
                if telNum == None:
                    return num
                else:
                    break

    def init_data(self):
        self.before_gst_dis = "26.09"
        self.before_gst = "39.13"
        self.express = "99.00"
        self.extensive = "120.00"
        self.euroCars = "160.00"
        self.van = "160.00"
        self.labour = "60.00"
        self.no = 0
        self.des = 1
        self.pri = 2
        self.qty = 3
        self.unit = 4
        self.amount = 5
        self.gst_amount = 6
        self.old_tel = None

    def initialize(self, package):
        #amount paid & amount due 2 decimal point
        amount_paid = str(package[4])
        amount_paid = float(amount_paid)
        amount_paid = '%0.2f' % amount_paid
        amount_due = str(package[5])
        amount_due = float(amount_due)
        amount_due = '%0.2f' % amount_due
        #dan dou sui le

        self.ui.lineEdit_7.setText(package[0])      #invoice_no
        self.ui.lineEdit.setText(package[1])        #customer name
        self.ui.lineEdit_4.setText(package[3])      #rego
        self.ui.pushButton_5.setText(package[6])    #Date
        self.ui.lineEdit_8.setText(str(amount_paid))      #amount paid
        self.ui.lineEdit_9.setText(str(amount_due))      #amount due
        self.old_tel = package[8][0][2]

        self.ui.lineEdit_3.setText(self.old_tel)   #old tel
        self.ui.comboBox.setCurrentIndex(self.ui.comboBox.findText(package[8][0][12]))#make
        self.ui.comboBox_2.setCurrentIndex(self.ui.comboBox_2.findText(package[8][0][11])) #model
        self.restore_table(package[7]) #center table restore

        #looking for address and set back
        self.cur.execute("SELECT Address FROM customer WHERE tel = '%s'" % self.old_tel)
        addr = self.cur.fetchone()[0]
        if addr != None:
            self.ui.lineEdit_2.setText(addr)

        #looking for oddometer and set back
        self.cur.execute("SELECT odo FROM vehicle WHERE tel='%s'" % self.old_tel)
        odo = self.cur.fetchone()[0]
        if odo != None:
            self.ui.lineEdit_6.setText(odo)

        #looking for note and service and labour
        self.cur.execute("SELECT note, service, labour FROM invoice WHERE tel='%s'" % self.old_tel)
        row = self.cur.fetchone()
        note = row[0]
        service = row[1]
        labour = row[2]

        if note != None:
            self.ui.textEdit.setText(note)
        if service != None:
            self.ui.textEdit_2.setText(service)
        if labour != None:
            self.ui.textEdit_3.setText(labour)

    def restore_table(self, table):
        for record in table:
            self.ui.tableWidget.insertRow(0)
            for item in record:
                if item == '':
                    item = 'None'
            lis = [item for no, item in enumerate(record) if no != 1]
            for idx, item in enumerate(lis):
                if idx == 0:
                    it = QtGui.QTableWidgetItem(str(item))
                    it.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.ui.tableWidget.setItem(0, idx, it)
                    continue
                if not isinstance(item, unicode):
                    it = QtGui.QTableWidgetItem(('%.2f') % item)
                else:
                    it = QtGui.QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(0, idx, it)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', 
                'Do you want to save this page?', QtGui.QMessageBox.Yes,
                QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            if self.clicked_bt_save() != False:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
    def clicked_bt_print(self):
        invoice_no, date, name, tel,\
        addr, make, model, rego, odo,\
        sub_total, gst, total, service,\
        labour, note, amount_paid,\
        amount_due, table = self.gather_data()

        self.editFile(invoice_no, date, name, tel, addr, make,\
                model, rego, odo, sub_total, gst, total, service,\
                labour, note, table)

        self.generate_pdf()
        dialog = QtGui.QPrintDialog()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.web.print_(dialog.printer())

    def init_invoice(self):
        self.cur.execute("SELECT invoice_no FROM INVOICE ORDER BY invoice_no DESC;")
        try:
            row = self.cur.fetchone()[0]
        except TypeError:
            row = 10000
        row += 1
        self.ui.lineEdit_7.setText(str(row))
    def convert(self):
        self.web.print_(self.printer)

    def clicked_bt_preview(self):
        invoice_no, date, name, tel, addr, make, model, rego,\
                odo, sub_total, gst, total, service, labour,\
                note, amount_paid, amount_due, table = self.gather_data()

        self.editFile(invoice_no, date, name, tel, addr, make, model,\
                rego, odo, sub_total, gst, total, service, labour, note, table)

        self.web = QtWebKit.QWebView()
        self.web.load(QtCore.QUrl("../Database/invoice/invoice.html"))
        self.web.loadFinished.connect(self.display_pdf)
    def display_pdf(self, web):
        dialog = QtGui.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.web.print_)
        dialog.exec_()

    def generate_pdf(self):
        self.web = QtWebKit.QWebView()
        self.web.load(QtCore.QUrl("../Database/invoice/invoice.html"))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName("../Database/invoice/invoice.pdf")
        self.web.loadFinished.connect(self.convert)

    def connect(self):
        try:
            self.conn = lite.connect("../Database/garage")
        except lite.Error, e:
            log_keeper.write_log(e.args[0], log_keeper.lineno())
            sys.exit(1)
    def wof_comboBox(self):
        if self.ui.comboBox_3.currentIndex() == 1:
            self.ui.tableWidget.insertRow(0)
            item = QtGui.QTableWidgetItem("Warrant of Fitness Check")
            self.ui.tableWidget.setItem(0, self.des, item)
            item = QtGui.QTableWidgetItem("1")
            self.ui.tableWidget.setItem(0, self.qty, item)
            item = QtGui.QTableWidgetItem(self.before_gst_dis)
            self.ui.tableWidget.setItem(0, self.pri, item)

        elif self.ui.comboBox_3.currentIndex() == 2:
            self.ui.tableWidget.insertRow(0)
            item = QtGui.QTableWidgetItem("Warrant of Fitness Check")
            self.ui.tableWidget.setItem(0, self.des, item)
            item = QtGui.QTableWidgetItem("1")
            self.ui.tableWidget.setItem(0, self.qty, item)
            item = QtGui.QTableWidgetItem(self.before_gst)
            self.ui.tableWidget.setItem(0, self.pri, item)
        self.add_no()

    def changeService(self):
        self.ui.textEdit_2.clear()
        chosen_name = self.ui.comboBox_5.currentText()
        if chosen_name == 'Express':
            self.ui.tableWidget.insertRow(0)
            item = QtGui.QTableWidgetItem("Express Service")
            self.ui.tableWidget.setItem(0, self.des, item)
            item = QtGui.QTableWidgetItem("1")
            self.ui.tableWidget.setItem(0, self.qty, item)
            item = QtGui.QTableWidgetItem(self.express)
            self.ui.tableWidget.setItem(0, self.pri, item)
            try:
                fd = open("../Database/text/express.txt", 'r')
            except IOError,e:
                log_keeper.write_log(e, log_keeper.lineno())
            try:
                self.ui.textEdit_2.setPlainText(fd.read())
            except UnboundLocalError, e:
                log_keeper.write_log(e, log_keeper.lineno())
            try:
                fd.close()
            except UnboundLocalError, e:
                pass
        elif chosen_name == 'Extensive':
            self.ui.tableWidget.insertRow(0)
            item = QtGui.QTableWidgetItem("Extensive Service")
            self.ui.tableWidget.setItem(0, self.des, item)
            item = QtGui.QTableWidgetItem("1")
            self.ui.tableWidget.setItem(0, self.qty, item)
            item = QtGui.QTableWidgetItem(self.extensive)
            self.ui.tableWidget.setItem(0, self.pri, item)
            try:
                fd = open("../Database/text/extensive.txt", 'r')
            except IOError, e:
                log_keeper.write_log(e, log_keeper.lineno())
            try:
                self.ui.textEdit_2.setPlainText(fd.read())
            except UnboundLocalError, e:
                log_keeper.write_log(e, log_keeper.lineno())
            try:
                fd.close()
            except UnboundLocalError, e:
                pass
        elif chosen_name == 'Euro_Car':
            self.ui.tableWidget.insertRow(0)
            item = QtGui.QTableWidgetItem("EuroCars Service")
            self.ui.tableWidget.setItem(0, self.des, item)
            item = QtGui.QTableWidgetItem("1")
            self.ui.tableWidget.setItem(0, self.qty, item)
            item = QtGui.QTableWidgetItem(self.euroCars)
            self.ui.tableWidget.setItem(0, self.pri, item)
            try:
                fd = open("../Database/text/euro.txt", 'r')
            except IOError, e:
                log_keeper.write_log(str(e), log_keeper.lineno())
            try:
                self.ui.textEdit_2.setPlainText(fd.read())
            except UnboundLocalError, e:
                log_keeper.write_log(e, log_keeper.lineno())
            try:
                fd.close()
            except UnboundLocalError, e:
                pass
        elif chosen_name == 'Van_4WD':
            self.ui.tableWidget.insertRow(0)
            item = QtGui.QTableWidgetItem("Van 4wd Service")
            self.ui.tableWidget.setItem(0, self.des, item)
            item = QtGui.QTableWidgetItem("1")
            self.ui.tableWidget.setItem(0, self.qty, item)
            item = QtGui.QTableWidgetItem(self.van)
            self.ui.tableWidget.setItem(0, self.pri, item)
            try:
                fd = open("../Database/text/van_4wd.txt", 'r')
            except IOError, e:
                log_keeper.write_log(e, log_keeper.lineno())
            try:
                self.ui.textEdit_2.setPlainText(fd.read())
            except UnboundLocalError, e:
                log_keeper.write_log(e, log_keeper.lineno())
            try:
                fd.close()
            except UnboundLocalError, e:
                pass
        else:
            return
        self.add_no()
    def calculate_amount(self, row):
        price_item = self.ui.tableWidget.item(row, self.pri)
        qty_item = self.ui.tableWidget.item(row, self.qty)
        if price_item == None or qty_item == None:
            return -1
        price = float(price_item.text())
        qty = float(qty_item.text())
        amount = str(price * qty)
        item = QtGui.QTableWidgetItem(amount)
        self.ui.tableWidget.setItem(row, self.amount, item)
        return 0

    def clicked_bt_fullPayment(self):
        text = str(self.ui.label_11.text()).split("(")[0]
        self.ui.lineEdit_8.setText(text)
        self.ui.lineEdit_9.setText("0")
    def clicked_bt_addLine(self):
        self.ui.tableWidget.insertRow(0)
        self.add_no()

    def add_no(self):
        no = self.ui.tableWidget.rowCount()
        if no == 1:
            item = QtGui.QTableWidgetItem(str(no))
        else:
            item_value = int(self.ui.tableWidget.item(1, 0).text()) + 1
            item = QtGui.QTableWidgetItem(str(item_value))

        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.ui.tableWidget.setItem(0, self.no, item)


    def clicked_bt_delLine(self):
        gst = 0
        amount_value = 0
        gst_amount = 0
        invoice_no = self.ui.lineEdit_7.text()
        current_row = self.ui.tableWidget.currentRow()
        if current_row == -1:
            current_row = 0
        try:
            amount_value = float(self.ui.tableWidget.item(current_row, self.amount).text())
        except AttributeError:
            amount_value = 0
        sub_value = float(self.ui.label_15.text())
        sub_value -= amount_value

        try:
            self.ui.label_15.setText(str("%.2f" % sub_value))
        except RuntimeError:
            pass

        try:
            gst_amount = float(self.ui.tableWidget.item(current_row, self.gst_amount).text())
        except AttributeError:
            gst_amount = 0
        total = float(self.ui.label_17.text())
        total -= gst_amount

        gst = total - sub_value
        try:
            self.ui.label_16.setText(str("%.2f" % gst))
            self.ui.label_17.setText(str("%.2f" % total))
            self.ui.label_11.setText(str("%.2f" % total))
        except RuntimeError:
            pass
        try:
            no = self.ui.tableWidget.item(current_row, self.no).text()
            self.cur.execute("DELETE FROM items WHERE invoice_no='%s' AND ID='%s'" % (invoice_no, no))
            self.conn.commit()
        except:
            pass
        self.ui.tableWidget.removeRow(current_row)

    def set_amount_gst(self, current_row, current_column):
        try:
            value = 0
            value = float(self.ui.tableWidget.item(current_row, self.amount).text()) * 1.15
            str_value = repr("%.2f" % value)[1:-1]
            item = QtGui.QTableWidgetItem(str_value)
            self.ui.tableWidget.setItem(current_row, self.gst_amount, item)
        except RuntimeError:
            pass
        except ValueError, e:
            self.ui.tableWidget.takeItem(current_row, current_column)
            self.ui.tableWidget.takeItem(current_row, current_column + 1)

    def set_sub_label(self):
        total_row = self.ui.tableWidget.rowCount()
        sub_total = 0
        value = 0

        for i in range(total_row):
            try:
                value = float(self.ui.tableWidget.item(i, self.amount).text())
            except AttributeError:
                value = 0
            except RuntimeError:
                pass
            sub_total += value
            value = 0
        try:
            self.ui.label_15.setText(str("%.2f" % sub_total))
        except RuntimeError:
            pass
        return sub_total

    def set_total_label(self):
        total = 0
        total_row = self.ui.tableWidget.rowCount()
        for i in range(total_row):
            try:
                value = float(self.ui.tableWidget.item(i, self.gst_amount).text())
            except AttributeError:
                value = 0
            except RuntimeError:
                pass
            total += value
            value = 0
            try:
                self.ui.label_17.setText(str("%.2f" % total))
                text = self.ui.lineEdit_8.text()
                if text != "":
                    self.ui.lineEdit_8.setText(text)
                else:
                    self.ui.lineEdit_8.setText("0.00")
                self.ui.label_11.setText(str("%.2f" % total))
            except RuntimeError:
                pass
        return total
    def set_gst_label(self, total, sub_total):
        gst = total - sub_total
        self.ui.label_16.setText(str("%.2f" % gst))

    def set_labels_and_gst(self, current_row, current_column):
        self.set_amount_gst(current_row, current_column)
        sub_total = self.set_sub_label()
        total = self.set_total_label()
        self.set_gst_label(total, sub_total)

    def set_amount(self, current_row, current_column):
        try:
            value = float(self.ui.tableWidget.item(current_row, current_column).text()) / 1.15
            str_value = repr("%.2f" % value)[1:-1]
            item = QtGui.QTableWidgetItem(str_value)
            self.ui.tableWidget.setItem(current_row, current_column - 1, item)
        except RuntimeError:
            pass
        except ValueError, e:
            self.ui.tableWidget.takeItem(current_row, current_column)
            self.ui.tableWidget.takeItem(current_row, current_column - 1)

    def set_labels_and_amount(self, current_row, current_column):
        self.set_amount(current_row, current_column)
        sub_total = self.set_sub_label()
        total = self.set_total_label()
        self.set_gst_label(total, sub_total)
    def changed_table(self, data):
        sub_total = 0
        gst = 0
        total = 0
        current_column = data.column()
        current_row = data.row()
        #Need to calculate Amount
        if current_column == self.pri or current_column == self.qty:
            try:
                if self.calculate_amount(current_row) != -1:
                    self.set_labels_and_gst(current_row, current_column)
            except RuntimeError:
                pass
        elif current_column == self.gst_amount:
            try:
                self.set_labels_and_amount(current_row, current_column)
            except RuntimeError:
                pass

    def clicked_bt_Tyres(self):
        Dialog = tyres.Tyres_Dialog()
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.show()
        result = Dialog.exec_()

    def clicked_bt_Calender(self):
        Dialog = calender.Calender_Dialog()
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.show()
        if Dialog.exec_() == 1:
            date = Dialog.getDate()
            self.ui.pushButton_5.setText(date)

    def clicked_bt_Labour(self):
        Dialog = labour.Labour_Dialog(self)
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.show()
        result = Dialog.exec_()
        if result == 1:
            self.setLabourText(Dialog)
            self.ui.tableWidget.insertRow(0)
            item = QtGui.QTableWidgetItem("Labour")
            self.ui.tableWidget.setItem(0, self.des, item)
            item = QtGui.QTableWidgetItem(self.labour)
            self.ui.tableWidget.setItem(0, self.pri, item)
            labourPrice = float(self.labour)
            amount = labourPrice * Dialog.getHours()
            item = QtGui.QTableWidgetItem(str("%.2f" % amount))
            self.ui.tableWidget.setItem(0, self.amount, item)
            item = QtGui.QTableWidgetItem(str(Dialog.getHours()))
            self.ui.tableWidget.setItem(0, self.qty, item)
            item = QtGui.QTableWidgetItem("Hrs")
            self.ui.tableWidget.setItem(0, self.unit, item)
        self.add_no()
    def error_window(self, errorMessage):
        reply = QtGui.QMessageBox.question(self, 'Message', 
                "%s existed in Database, Please Check it." % errorMessage, QtGui.QMessageBox.Yes)
    def clicked_bt_save(self):
        invoice_no, date, name, tel, addr, make, model, rego,\
                odo, sub_total, gst, total, service, labour,\
                note,amount_paid, amount_due, table = self.gather_data()
        try:
            self.cur.execute("INSERT INTO invoice(invoice_no,\
                    date_in, tel, name, rego, money_in,\
                    amount_paid,amount_due, model, make,\
                    service, note, labour) VALUES('%s',\
                    '%s', '%s', '%s','%s', '%s', '%s',\
                    '%s', '%s', '%s', '%s','%s','%s')" %\
                    (invoice_no,date, tel, name, rego,\
                    sub_total, amount_paid,amount_due,\
                    model, make, service, note, labour))

        except lite.IntegrityError:
            self.cur.execute('UPDATE invoice SET date_in="%s",\
                    tel="%s", name="%s", rego="%s", money_in="%s",\
                    amount_paid="%s",amount_due="%s", model="%s",\
                    make="%s", service="%s", note="%s",\
                    labour="%s" where invoice_no="%s"' %\
                    (date, tel, name, rego, sub_total,\
                    amount_paid, amount_due, model, make,\
                    service, note, labour, invoice_no))

        if self.old_tel == None:
            try:
                self.cur.execute("INSERT INTO customer(tel,\
                                name, Address) VALUES('%s', '%s', '%s')"\
                                % (tel, name, addr))
            except lite.IntegrityError:
                self.error_window("Telephone number")
                return False
        elif self.old_tel == tel:
            self.cur.execute("UPDATE customer SET name='%s',\
                    Address='%s' where tel='%s'" % (name, addr, tel))
        else:
            try:
                self.cur.execute("UPDATE customer SET tel='%s',\
                        name='%s', Address='%s' where tel='%s'"\
                        % (tel, name, addr, self.old_tel))
            except lite.IntegrityError:
                self.error_window("Telephone number")
                return False
        try:
            self.cur.execute("INSERT INTO vehicle(rego, make,\
                    model, odo, tel) VALUES('%s', '%s', '%s',\
                    '%s','%s')" % (rego, make, model, odo, tel))
        except lite.IntegrityError,e:
            self.cur.execute("UPDATE vehicle SET \
                    make='%s', model='%s', odo='%s' WHERE tel='%s' AND rego='%s'" %\
                    (rego, make, model, odo, tel))
        self.conn.commit()

        for row in table:
            no = row["no"]
            des = row["des"]
            price = row["pri"]
            qty = row["qty"]
            unit = row["unit"]
            amount = row["amount"]
            amount_gst = row['amount_gst']
            try:
                self.cur.execute("INSERT INTO items(ID, invoice_no,\
                        des, price, qty, unit, amount, amount_gst)\
                        VALUES('%s', '%s', '%s', '%s', '%s', '%s',\
                        '%s', '%s')" % (no, invoice_no, des, price,\
                        qty, unit, amount, amount_gst))
            except lite.IntegrityError:
                self.cur.execute("UPDATE items SET des='%s',\
                        price='%s', qty='%s', unit='%s',\
                        amount='%s', amount_gst='%s' where ID='%s'\
                        AND invoice_no='%s'" % (des, price, qty,\
                        unit, amount, amount_gst, no, invoice_no))
            self.conn.commit()
        return True

    def gather_data(self):
        table = []
        name = self.ui.lineEdit.text()
        tel = self.ui.lineEdit_3.text()
        addr = self.ui.lineEdit_2.text()
        invoice_no = self.ui.lineEdit_7.text()
        date = self.ui.pushButton_5.text()
        make = self.ui.comboBox.currentText()
        model = self.ui.comboBox_2.currentText()
        rego = self.ui.lineEdit_4.text()
        odo = self.ui.lineEdit_6.text()
        note = self.ui.textEdit.toPlainText()
        service = self.ui.textEdit_2.toPlainText()
        labour = self.ui.textEdit_3.toPlainText()
        sub_total = self.ui.label_15.text()
        gst = self.ui.label_16.text()
        total = self.ui.label_17.text()
        amount_paid = self.ui.lineEdit_8.text()
        amount_due = self.ui.lineEdit_9.text()


        for i in range(self.ui.tableWidget.rowCount()):
            row = {}
            if self.ui.tableWidget.item(i, self.no) != None:
                row["no"] = self.ui.tableWidget.item(i, self.no).text()
            else:
                row["no"] = ""
            if self.ui.tableWidget.item(i, self.des) != None:
                row["des"] = self.ui.tableWidget.item(i, self.des).text()
            else:
                row["des"] = ""
            if self.ui.tableWidget.item(i, self.pri) != None:
                row["pri"] = self.ui.tableWidget.item(i, self.pri).text()
            else:
                row["pri"] = ""
            if self.ui.tableWidget.item(i, self.qty) != None:
                row["qty"] = self.ui.tableWidget.item(i, self.qty).text()
            else:
                row["qty"] = ""
            if self.ui.tableWidget.item(i, self.unit) != None:
                row["unit"] = self.ui.tableWidget.item(i, self.unit).text()
            else:
                row["unit"] = ""
            if self.ui.tableWidget.item(i, self.amount) != None:
                row["amount"] = self.ui.tableWidget.item(i, self.amount).text()
            else:
                row["amount"] = ""
            if self.ui.tableWidget.item(i, self.gst_amount) != None:
                row["amount_gst"] = self.ui.tableWidget.item(i, self.gst_amount).text()
            else:
                row["amount_gst"] = ""
            table.append(row)
        return invoice_no, date, name, tel, addr, make,\
                model, rego, odo, sub_total, gst, total,\
                service, labour, note, amount_paid,\
                amount_due, table


    def editFile(self, invoice_no, date, name, tel,\
            addr, make, model, rego, odo, sub_total,\
            gst, total, service, labour, note, table):
        edit = edit_file.edit_invoice()
        edit.edit_all(invoice_no, date, name, tel,\
                addr, make, model, rego, odo,\
                sub_total, gst, total, service,\
                labour, note, table)

    def setMake(self):
        self.cur.execute("SELECT name from make")
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            self.ui.comboBox.addItem(row[0])
        self.ui.comboBox.setCurrentIndex(-1)


    def setLabourText(self, dialog):
        checkText = dialog.getCheckText()
        fixText = dialog.getFixText()
        replaceText = dialog.getReplaceText()
        self.ui.textEdit_3.setPlainText("Check: %s \n\nFix/Repair:\
                %s \n\nReplace: %s" %(checkText, fixText, replaceText))
    def clicked_bt_Discount(self):
        beforeDiscount = self.ui.label_17.text()
        Dialog = discount.Discount_Dialog(beforeDiscount)
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.show()
        result = Dialog.exec_()
        if result == 1:
            flag, discount1, beforeDiscount = Dialog.getDiscount()
            flag = float(flag)
            discount1 = float(discount1)
            total = float(self.ui.label_17.text())
            if (flag == 1):
                newTotal = total * discount1
                string_DP = str("%.0f") % (discount1 * 100)
                noteText = string_DP + "%"
                text = str("%.2f") % newTotal + "(" + noteText + ")"
                self.ui.label_11.setText(text)
            elif (flag == 2):
                newTotal = total + discount1
                percentage = str("%.2f") % ((1 - ((total - newTotal) / total)) * 100) + "%"
                text = str("%.2f") % newTotal + "(" + percentage + ")"
                self.ui.label_11.setText(text)
            elif (flag == 3):
                self.ui.label_11.setText(beforeDiscount)
        else:
            return
    def clicked_bt_Paid(self):
        Dialog = paid_file.Paid_Dialog()
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.show()
        result = Dialog.exec_()
        if result == 1:
            paid = Dialog.getPaid()
            total = float(self.ui.label_17.text())
            after_discount = str(self.ui.label_11.text())
            after_discount = float(after_discount[0:after_discount.find('(')])
            amount_paid = self.ui.lineEdit_8.text()
            if amount_paid == '0.00':
                amount_due = after_discount - paid
                amount_paid = paid
                self.ui.lineEdit_8.setText(str("%.2f") % amount_paid)
                self.ui.lineEdit_9.setText(str("%.2f") % amount_due)
            else:
                amount_paid = float(amount_paid) + paid
                amount_due = total - float(amount_paid)
                self.ui.lineEdit_8.setText(str("%.2f") % amount_paid)
                self.ui.lineEdit_9.setText(str("%.2f") % amount_due)


    def clicked_bt_Cash(self):
        Dialog = cash.Cash_Dialog()
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.show()
        result = Dialog.exec_()
    def changeModel(self):
        self.ui.comboBox_2.clear()
        chosen_name = self.ui.comboBox.currentText()
        self.cur.execute("SELECT name from model WHERE make_name='%s'" % chosen_name)
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            self.ui.comboBox_2.addItem(row[0])

    def autoChangeText(self):
        if self.ui.lineEdit_8.text() == "":
            amount_paid = 0.00
        else:
            amount_paid = float(self.ui.lineEdit_8.text())
        total = float(self.ui.label_17.text())
        amount_due = float (total) - float (amount_paid)
        self.ui.lineEdit_9.setText(str("%.2f") % amount_due)

    def setTime(self):
        self.ui.pushButton_5.setText(time.strftime("%Y-%m-%d", time.localtime(time.time())))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Add_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
