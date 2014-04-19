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
		
		#self.plusButton.setFixedWidth(40)
		#self.minButton.setFixedWidth(40)

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
		self.add_page("Main")
		self.add_page("Customer")
		self.add_page("Paid List")
		self.add_page("Unpaid")
		
		vbox.addLayout(vbox_1)
		vbox.addLayout(vbox_2)


		self.setLayout(vbox)
		self.setGeometry(250, 250, 870, 150 + 30 * self.get_rows())
		self.setWindowTitle('Managment System')
    def create_page(self, *contents):
        page = QtGui.QWidget()
        vbox = QtGui.QVBoxLayout()
        for c in contents:
            vbox.addWidget(c)
        page.setLayout(vbox)
        return page

    def create_table(self, name):
		if name == "Main":
			table = self.M_create_table()
		elif name == "Customer":
			table = self.C_create_table()
		elif name == "Paid List":
			table = self.P_create_table()
		else:
			table = self.U_create_table()

		return table
	
	

    def get_rows(self):
        return 17
    def add_page(self, name):
        self.pages.append(self.create_page(self.create_table(name)))
        self.tabwidget.addTab(self.pages[-1], name)
        self.tabwidget.setCurrentIndex(len(self.pages) - 1)

    def M_create_table(self):
        columns = 8
        rows = self.get_rows()
        table = QtGui.QTableWidget(rows, columns)
        for r in xrange(rows):
	        table.setItem(r, 0, QtGui.QTableWidgetItem("ak"))
	        table.setItem(r, 1, QtGui.QTableWidgetItem("ak"))
	        table.setItem(r, 2, QtGui.QTableWidgetItem("ak"))
	        table.setItem(r, 3, QtGui.QTableWidgetItem("ak"))
	        table.setItem(r, 4, QtGui.QTableWidgetItem("ak"))
	        table.setItem(r, 5, QtGui.QTableWidgetItem("ak"))
	        table.setItem(r, 6, QtGui.QTableWidgetItem("ak"))
	        table.setItem(r, 7, QtGui.QTableWidgetItem("ak"))
        return table

    def P_create_table(self):
        columns = 4
        rows = self.get_rows()
        table = QtGui.QTableWidget(rows, columns)
        for r in xrange(rows):
	        table.setItem(r, 0, QtGui.QTableWidgetItem("ak"))
	        table.setItem(r, 1, QtGui.QTableWidgetItem("ak"))
	        table.setItem(r, 2, QtGui.QTableWidgetItem("ak"))
	        table.setItem(r, 3, QtGui.QTableWidgetItem("ak"))
        return table
    def U_create_table(self):
        columns = 2
        rows = self.get_rows()
        table = QtGui.QTableWidget(rows, columns)
        for r in xrange(rows):
	        table.setItem(r, 0, QtGui.QTableWidgetItem("ak"))
	        table.setItem(r, 1, QtGui.QTableWidgetItem("ak"))
        return table

    def C_create_table(self):
        columns = 1
        rows = self.get_rows()
        table = QtGui.QTableWidget(rows, columns)
        for r in xrange(rows):
	        table.setItem(r, 0, QtGui.QTableWidgetItem("ak"))
        return table

if __name__ == "__main__":
    app = QtGui.QApplication([])
    bing_p = Bing_MainWindow()
    bing_p.show()
    app.exec_()
