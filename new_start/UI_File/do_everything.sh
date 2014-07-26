#!/bin/sh

pyuic4 -x Add.ui -o Add.py
pyuic4 -x Tyres.ui -o Tyres.py
pyuic4 -x Calender.ui -o Calender.py
pyuic4 -x Labour.ui -o Labour.py
pyuic4 -x Discount.ui -o Discount.py
pyuic4 -x Paid.ui -o Paid.py
pyuic4 -x Cash.ui -o Cash.py
pyuic4 -x Main.ui -o Main.py

mv Add.py ../project/ui/Ui_Add.py
mv Tyres.py ../project/ui/Ui_Tyres.py
mv Calender.py ../project/ui/Ui_Calender.py
mv Labour.py ../project/ui/Ui_Labour.py
mv Discount.py ../project/ui/Ui_Discount.py
mv Paid.py ../project/ui/Ui_Paid.py
mv Cash.py ../project/ui/Ui_Cash.py
mv Main.py ../project/ui/Ui_Main.py
