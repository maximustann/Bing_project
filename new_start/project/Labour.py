#!/user/bin/env python

from PyQt4 import QtCore, QtGui
from ui import Ui_Labour as ui_labour

class Labour_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Labour_Dialog, self) .__init__()
        self.ui = ui_labour.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.plainTextEdit.textChanged.connect(self.setCheckText)
        self.ui.plainTextEdit_2.textChanged.connect(self.setFixText)
        self.ui.plainTextEdit_3.textChanged.connect(self.setReplaceText)
    def setCheckText(self):
        text = self.ui.plainTextEdit.toPlainText()
        if text != "":
            self.check_text = text
        else:
            self.check_text = " "
    def setFixText(self):
        self.fix_text = self.ui.plainTextEdit_2.toPlainText()

    def setReplaceText(self):
        self.replace_text = self.ui.plainTextEdit_3.toPlainText()

    def getCheckText(self):
        return self.check_text

    def getFixText(self):
        return self.fix_text

    def getReplaceText(self):
        return self.replace_text

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Labour_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
