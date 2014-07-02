#!/usr/bin/env python

from PyQt4 import QtCore, QtGui;
from ui import Ui_Add as ui_add;
import sqlite3 as lite

class Add_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Add_Dialog, self).__init__()
        self.ui = ui_add.Ui_Dialog()
        self.ui.setupUi(self)
        self.conn = None
        self.cur = None
        self.connect()
        self.cur = self.conn.cursor()
        self.setMake()


    def connect(self):
        try:
            self.conn = lite.connect("../Database/garage")
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

    def setMake(self):
        self.cur.execute("SELECT name from make")
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            self.ui.comboBox.addItem(row[0])

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Add_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
