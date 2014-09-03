#!/bin/env python

import sys
import unittest
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt
sys.path.append("../")
from project import Main

class test_nothing(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.dialog = Main.Main_Dialog()

    def test(self):
        self.dialog.ui.lineEdit_main_search.setText("ok")
        self.assertEqual(self.dialog.ui.lineEdit_main_search.text(), 'ok')
if __name__ == '__main__':
    unittest.main()
