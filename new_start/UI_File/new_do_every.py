#!/usr/bin/env python
import os,sys


def filelist():
    namelist = []
    names = os.listdir(os.getcwd())
    for name in names:
        if name[-2:] == 'ui':
            pos = name.index('.')
            name = name[0:pos]
            namelist.append(name)
    return namelist

def pyqt(namelist):
    for name in namelist:
        os.system('pyuic4 -x %s.ui -o %s.py' % (name, name))

def usesed(namelist):
    for name in namelist:
        os.system('sed -i "5d" %s.py' % name)

def detectexist(namelist):
    ui_dir = '../project/ui'
    for name in namelist:
        if not os.path.exists("%s/Ui_%s.py" % (ui_dir, name)):
            os.system('cp %s.py %s/Ui_%s.py' % (name, ui_dir, name))

def checkdiff(namelist):
    ui_dir = '../project/ui'
    for name in namelist:
        diff = os.system('diff -q %s.py %s/Ui_%s.py' % (name, ui_dir, name))
        if diff != 0:
            os.system('cp %s.py %s/Ui_%s.py' % (name, ui_dir, name))

def rm(namelist):
    for name in namelist:
        os.system('rm %s.py' % name)

if __name__ == "__main__":
    namelist = filelist()
    pyqt(namelist)
    usesed(namelist)
    detectexist(namelist)
    checkdiff(namelist)
    rm(namelist)
