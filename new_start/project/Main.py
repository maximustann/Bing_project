#!/user/bin/env python

from PyQt4 import QtCore, QtGui
from ui import Ui_Main as ui_main
import Add as add;

class Main_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Main_Dialog, self).__init__()
        self.ui = ui_main.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.clicked_bt_Add)
    def clicked_bt_Add(self):
        Dialog = add.Add_Dialog()
        Dialog.show()
        result = Dialog.exec_()
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Main_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
