#!/bin/env python

from PyQt4 import QtCore, QtGui
from ui import Ui_Add_user as ui_add_user
from random import randint
import log_keeper
import sqlite3 as lite
class Add_user_Dialog(QtGui.QDialog):
    def __init__(self, package):
        super(Add_user_Dialog, self) .__init__()
        self.ui = ui_add_user.Ui_Dialog()
        self.ui.setupUi(self)
        self.conn = None
        self.cur = None
        self.old_tel = None
        self.connect()
        self.cur = self.conn.cursor()
        self.ui.lineEdit_Tel.setText(self.random_Tel_Num())
        if package != None:
            self.initialize(package)
    def initialize(self, package):
        name = package[0] #name
        self.old_tel = package[1] #tel
        addr = package[2] #address
        self.ui.lineEdit_Name.setText(name)
        self.ui.lineEdit_Tel.setText(self.old_tel)
        self.ui.lineEdit_Address.setText(addr)

    def connect(self):
        try:
            self.conn = lite.connect("../Database/garage")
        except lite.Error, e:
            log_keeper.write_log(e.args[0], log_keeper.lineno())
            sys.exit(1)

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

    def accept(self):
        result = self.save()
        if result != False:
            super(Add_user_Dialog, self).accept()

    def save(self):
        name, tel, addr = self.gather_data()
        if self.old_tel == None:
            try:
                self.cur.execute("INSERT INTO customer(tel, name, Address) VALUES('%s', '%s', '%s')" % (tel, name, addr))
                print "Donw"
            except lite.IntegrityError:
                self.error_window("Telephone number")
                return False
        elif self.old_tel == tel:
            self.cur.execute("UPDATE customer SET name='%s',Address='%s' where tel='%s'" % (name, addr, tel))
        else:
            try:
                self.cur.execute("UPDATE customer SET tel='%s',\
                                name='%s', Address='%s' where tel='%s'"\
                                % (tel, name, addr, self.old_tel))
            except lite.IntegrityError:
                self.error_window("Telephone number")
                return False
        self.conn.commit()

    def error_window(self, errorMessage):
        reply = QtGui.QMessageBox.question(self, 'Message',
                                        "%s existed, Please Check it." % errorMessage, 
                                        QtGui.QMessageBox.Yes)

    def gather_data(self):
        name = self.ui.lineEdit_Name.text()
        tel = self.ui.lineEdit_Tel.text()
        addr = self.ui.lineEdit_Address.text()
        return name, tel, addr

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Add_user_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
