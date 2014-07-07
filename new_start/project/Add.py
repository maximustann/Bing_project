#!/usr/bin/env python

from PyQt4 import QtCore, QtGui;
from ui import Ui_Add as ui_add;
import sqlite3 as lite;
import Tyres as tyres;
import Calender as calender;
import Labour as labour;
import time;
import os;

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
        self.ui.comboBox_5.currentIndexChanged.connect(self.changeService)
        self.ui.pushButton_7.clicked.connect(self.clicked_bt_Tyres)
        self.ui.pushButton_5.clicked.connect(self.clicked_bt_Calender)
        self.ui.pushButton_9.clicked.connect(self.clicked_bt_Labour)
        self.ui.pushButton_12.clicked.connect(self.clicked_bt_addLine)
        self.ui.pushButton_13.clicked.connect(self.clicked_bt_delLine)
        self.ui.tableWidget.itemChanged.connect(self.changed_table)
        self.ui.comboBox_3.currentIndexChanged.connect(self.wof_comboBox)
    def connect(self):
        try:
            self.conn = lite.connect("../Database/garage")
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
    def wof_comboBox(self):
        if self.ui.comboBox_3.currentIndex() == 1:
            self.ui.tableWidget.insertRow(0)
            item = QtGui.QTableWidgetItem("Warrant of Fitness Check")
            self.ui.tableWidget.setItem(0,0, item)
            item = QtGui.QTableWidgetItem("1")
            self.ui.tableWidget.setItem(0,1, item)
            item = QtGui.QTableWidgetItem("26.09")
            self.ui.tableWidget.setItem(0,3, item)

        elif self.ui.comboBox_3.currentIndex() == 2:
            self.ui.tableWidget.insertRow(0)
            item = QtGui.QTableWidgetItem("Warrant of Fitness Check")
            self.ui.tableWidget.setItem(0,0, item)
            item = QtGui.QTableWidgetItem("1")
            self.ui.tableWidget.setItem(0,1, item)
            item = QtGui.QTableWidgetItem("39.10")
            self.ui.tableWidget.setItem(0,3, item)
    def write_log(self, string):
        my_time = None
        fd = open("../Database/log/log.txt", "a")
        my_time = str(time.strftime("%Y-%m-%d-%I:%M", time.localtime(time.time())))
        fd.write(string + "\t" + my_time + "\n")
        fd.close()

    def changeService(self):
        self.ui.textEdit_2.clear()
        chosen_name = self.ui.comboBox_5.currentText()
        if chosen_name == 'Express':
            try:
                fd = open("../Database/text/express.txt", 'r')
            except IOError,e:
                self.write_log(e)
            self.ui.textEdit_2.setPlainText(fd.read())
            fd.close()
        elif chosen_name == 'Extensive':
            try:
                fd = open("../Database/text/extensive.txt", 'r')
            except IOError, e:
                self.write_log(e)
            self.ui.textEdit_2.setPlainText(fd.read())
            fd.close()
        elif chosen_name == 'Euro_Car':
            try:
                fd = open("../Database/text/euro.txt", 'r')
            except IOError, e:
                self.write_log(str(e))
            self.ui.textEdit_2.setPlainText(fd.read())
            fd.close()
        else:
            try:
                fd = open("../Database/text/van_4wd.txt", 'r')
            except IOError, e:
                self.write_log(e)
            self.ui.textEdit_2.setPlainText(fd.read())
            fd.close()



    def clicked_bt_addLine(self):
        self.ui.tableWidget.insertRow(0)
    def clicked_bt_delLine(self):
        gst = 0
        amount_value = 0
        gst_amount = 0
        current_row = self.ui.tableWidget.currentRow()
        try:
            amount_value = float(self.ui.tableWidget.item(current_row, 3).text())
        except AttributeError:
            amount_value = 0
        sub_value = float(self.ui.label_15.text())
        sub_value -= amount_value

        try:
            self.ui.label_15.setText(str("%.2f" % sub_value))
        except RuntimeError:
            pass

        try:
            gst_amount = float(self.ui.tableWidget.item(current_row, 4).text())
        except AttributeError:
            gst_amount = 0
        total = float(self.ui.label_17.text())
        total -= gst_amount

        gst = total - sub_value
        try:
            self.ui.label_16.setText(str("%.2f" % gst))
            self.ui.label_17.setText(str("%.2f" % total))
        except RuntimeError:
            pass



        self.ui.tableWidget.removeRow(current_row)

    def changed_table(self):
        sub_total = 0
        gst = 0
        total = 0
        value = 0
        current_row = self.ui.tableWidget.currentRow()
        current_column = self.ui.tableWidget.currentColumn()
        #Need to calculate Amount
        if current_column == 3:
            try:
                value = float(self.ui.tableWidget.currentItem().text()) * 1.15
                str_value = repr("%.2f" % value)[1:-1]
                item = QtGui.QTableWidgetItem(str_value)
                self.ui.tableWidget.setItem(current_row, 4, item)
            except RuntimeError:
                pass

            total_row = self.ui.tableWidget.rowCount()
            for i in range(total_row):
                try:
                    value = float(self.ui.tableWidget.item(i, 3).text())
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

            for i in range(total_row):
                try:
                    value = float(self.ui.tableWidget.item(i, 4).text())
                except AttributeError:
                    value = 0
                except RuntimeError:
                    pass
                total += value
                gst = total - sub_total
                value = 0
            try:
                self.ui.label_16.setText(str("%.2f" % gst))
                self.ui.label_17.setText(str("%.2f" % total))
            except RuntimeError:
                pass
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
        if result == 1:
            self.setLabourText(Dialog)

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
        self.ui.textEdit_3.setPlainText("Check: %s \n\nFix/Repair: %s \n\nReplace: %s" %(checkText, fixText, replaceText))


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
