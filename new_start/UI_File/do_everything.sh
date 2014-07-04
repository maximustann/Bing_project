#!/bin/sh

pyuic4 -x Add.ui -o Add.py
pyuic4 -x Tyres.ui -o Tyres.py
pyuic4 -x Calender.ui -o Calender.py

mv Add.py ../project/ui/Ui_Add.py
mv Tyres.py ../project/ui/Ui_Tyres.py
mv Calender.py ../project/ui/Ui_Calender.py

