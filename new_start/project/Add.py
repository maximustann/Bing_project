#!/usr/bin/env python

from PyQt4 import QtCore, QtGui;
from ui import Ui_Add as ui_add;
import sqlite3 as lite;
import Tyres as tyres;
import time;

class Add_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Add_Dialog, self).__init__()
        self.ui = ui_add.Ui_Dialog()
        self.ui.setupUi(self)
        self.conn = None
        self.cur = None
        self.connect()
        self.setTime()
        self.cur = self.conn.cursor()
        self.setMake()
        self.ui.comboBox.currentIndexChanged.connect(self.changeModel)
        self.ui.pushButton_7.clicked.connect(self.clicked_bt_Tyres)

    def connect(self):
        try:
            self.conn = lite.connect("../Database/garage")
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

    def clicked_bt_Tyres(self):
        Dialog = tyres.Tyres_Dialog()
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
