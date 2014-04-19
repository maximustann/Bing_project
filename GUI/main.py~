#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

class Bing_MainWindow(QtGui.QWidget):
    def __init__(self):
        super(Bing_MainWindow, self).__init__()
        self.initUI()
    def initUI(self):

        self.plusButton = QtGui.QPushButton("", self)
        self.plusButton.setIcon(QtGui.QIcon("icons/plus.jpeg"))
        self.minButton = QtGui.QPushButton("", self)
        self.minButton.setIcon(QtGui.QIcon("icons/min.jpeg"))
        
        self.plusButton.setFixedWidth(40)
        self.minButton.setFixedWidth(40)


        vbox = QtGui.QVBoxLayout()

        hbox_1 = QtGui.QHBoxLayout()
        hbox_1.addWidget(self.plusButton)
        hbox_1.addWidget(self.minButton)

        vbox_1 = QtGui.QVBoxLayout()
        vbox_1.addLayout(hbox_1)



        self.tabwidget = QtGui.QTabWidget(self)
        vbox_2 = QtGui.QVBoxLayout()
        vbox_2.addWidget(self.tabwidget)
        

        self.pages = []
        self.add_page()

        vbox.addLayout(vbox_1)
        vbox.addLayout(vbox_2)






        self.setLayout(vbox)
        self.setGeometry(250, 250, 400, 180)



    def create_page(self, *contents):
        page = QtGui.QWidget()
        vbox = QtGui.QVBoxLayout()
        for c in contents:
            vbox.addWidget(c)
        page.setLayout(vbox)
        return page
    def create_table(self):
        rows, columns = 1, 8
        table = QtGui.QTableWidget(rows, columns)
        for r in xrange(rows):
            for c in xrange(columns):
                table.setItem(r, c, QtGui.QTableWidgetItem("ak"))
        return table
    def add_page(self):
        self.pages.append(self.create_page(self.create_table()))
        self.tabwidget.addTab(self.pages[-1], 'Customer')
        self.tabwidget.setCurrentIndex(0)



if __name__ == "__main__":
    app = QtGui.QApplication([])
    bing_p = Bing_MainWindow()
    bing_p.show()
    app.exec_()
