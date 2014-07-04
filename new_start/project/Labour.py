#!/user/bin/env python

from PyQt4 import QtCore, QtGui
from ui import Ui_Labour as ui_labour

class Labour_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Labour_Dialog, self) .__init__()
        self.ui = ui_labour.Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Labour_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
