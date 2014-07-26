#!/user/bin/env python

from PyQt4 import QtCore, QtGui

from ui import Ui_Main as ui_main
import sqlite3 as lite;
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
        self.conn = None
        self.cur = None
        self.connect()
        self.cur = self.conn.cursor()
        self.getday()
    def clicked_bt_Add(self):
        Dialog = add.Add_Dialog()
        Dialog.show()
        result = Dialog.exec_()
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
        return datetime.date(year, month, day).weekday()
    def print_table(self):
        pass
    def write_log(self, string):
        my_time = None
        fd = open("../Database/log/log.txt", "a")
        my_time = str(time.strftime("%Y-%m-%d-%I:%M", time.localtime(time.time())))
        fd.write(string + "\t" + my_time + "\n")
        fd.close()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Main_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
