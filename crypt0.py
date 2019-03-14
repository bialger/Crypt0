#!/usr/bin/python3
# -*- coding: utf-8 -*-
import hashlib
import random
import datetime
import os
import sys
from PyQt5 import (QtWidgets, QtGui)
from PyQt5.QtWidgets import (QWidget, QLineEdit, QTextEdit, QGridLayout,  QDesktopWidget, QMainWindow, QLabel, QToolTip, QComboBox, QPushButton, QMessageBox, QApplication)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import (QFont, QIcon)
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('Times New Roman', 11))
        self.setToolTip('Это моя гениальная программа')
        grid = QGridLayout()
        grid.setSpacing(5)
        self.setLayout(grid)
        lbl1 = QLabel('Выберите опцию', self)
        lbl2 = QLabel('Обязательно выберите одну из опций', self)
        self.lne = QComboBox(self)
        self.lne.addItems(["Зашифровать", "Расшифровать"])
        x = 'Вы ничего не выбрали'
        self.lbl3 = QLabel(x, self)
        lbl11 = QLabel('Введите пароль', self)
        lbl21 = QLabel('Не стирайте "2)" если хотите корректной работы программы', self)
        lne1 = QLineEdit('2) ', self)
        x1 = 'Вы ничего не выбрали'
        self.lbl31 = QLineEdit(x1, self)
        lbl12 = QLabel('Введите полный путь до файла для зашифровки/дешифровки', self)
        lbl22 = QLabel('Не стирайте "3)" если хотите корректной работы программы', self)
        lne2 = QLineEdit('3) ', self)
        x2 = 'Вы ничего не выбрали'
        self.lbl32 = QLabel(x2, self)
        lbl13 = QLabel('Введите полный путь до файла назначения', self)
        lbl23 = QLabel('Не стирайте "4)" если хотите корректной работы программы', self)
        lne3 = QLineEdit('4) ', self)
        x3 = 'Вы ничего не выбрали'
        self.lbl33 = QLabel(x3, self)
        lbl14 = QLabel('Удалить исходный файл?(да/нет)', self)
        lbl24 = QLabel('Обязательно выберите опцию', self)
        self.lne4 = QComboBox(self)
        self.lne4.addItems(["Да  ", "Нет "])
        x4 = 'Вы ничего не выбрали'
        self.lbl34 = QLabel(x4, self)
        defin = QLabel('Перед тем, как запускать процесс шифрования, введите ВСЕ данные.', self)
        defin1 = QLabel('Если у Вас возникли какие-то вопросы, пишите на электронный адрес artur.bigulov@yandex.ru', self)
        btn = QPushButton("Шифровать!", self)
        btn.clicked.connect(self.buttonClicked)
        btn1 = QPushButton("Случайный пароль", self)
        btn1.clicked.connect(self.buttonClicked)
        btn2 = QPushButton("По умолчанию", self)
        btn2.clicked.connect(self.buttonClicked)
        self.lne.activated[str].connect(self.onActivated)
        lne1.textChanged[str].connect(self.onChanged)
        lne2.textChanged[str].connect(self.onChanged)
        lne3.textChanged[str].connect(self.onChanged)
        self.lne4.activated[str].connect(self.onActivated)
        self.pal = self.lbl3.palette()
        self.pal1 = self.lbl31.palette()
        self.pal2 = self.lbl32.palette()
        self.pal3 = self.lbl33.palette()
        self.pal4 = self.lbl34.palette()
        self.pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"))
        self.pal1.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"))
        self.pal2.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"))
        self.pal3.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"))
        self.pal4.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"))
        self.lbl3.setPalette(self.pal)
        self.lbl31.setPalette(self.pal1)
        self.lbl32.setPalette(self.pal2)
        self.lbl33.setPalette(self.pal3)
        self.lbl34.setPalette(self.pal4)
        grid.addWidget(lbl1, 1, 1)
        grid.addWidget(lbl2, 2, 1)
        grid.addWidget(self.lne, 3, 1)
        grid.addWidget(self.lbl3, 4, 1)
        grid.addWidget(lbl11, 5, 1)
        grid.addWidget(lbl21, 6, 1)
        grid.addWidget(lne1, 7, 1)
        grid.addWidget(self.lbl31, 9, 1)
        grid.addWidget(lbl12, 10, 1)
        grid.addWidget(lbl22, 11, 1)
        grid.addWidget(lne2, 12, 1)
        grid.addWidget(self.lbl32, 13, 1)
        grid.addWidget(lbl13, 14, 1)
        grid.addWidget(lbl23, 15, 1)
        grid.addWidget(lne3, 16, 1)
        grid.addWidget(self.lbl33, 18, 1)
        grid.addWidget(lbl14, 19, 1)
        grid.addWidget(lbl24, 20, 1)
        grid.addWidget(self.lne4, 21, 1)
        grid.addWidget(self.lbl34, 22, 1)
        grid.addWidget(defin, 23, 1)
        grid.addWidget(defin1, 24, 1)
        grid.addWidget(btn, 25, 1)
        grid.addWidget(btn1, 8, 1)
        grid.addWidget(btn2, 17, 1)
        self.resize(500, 500)
        self.center()
        self.setWindowTitle('Crypt0 4.9.9 beta')
        self.setWindowIcon(QIcon('zamok.jpg'))
        self.show()
        self.en = ['q','w','e','r','t','y','u','i','o','p','[',']',
          'a','s','d','f','g','h','j','k','l',';',
          'z','x','c','v','b','n','m',',','.','/',  
          '1','2','3','4','5','6','7','8','9','0','=',
          '~','!','(',')','+',
          'Q','W','E','R','T','Y','U','I','O','P',
          'A','S','D','F','G','H','J','K','L',':',
          'Z','X','C','V','B','N','M',]
        self.de = ''
        self.password = ''
        self.infile = ''
        self.outfile = ''
        self.df = ''
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def onActivated(self, text):
        def errmsg(name, num):
            hexnum1 = hex(num)
            zero = ''
            for i in range(11-len(hexnum1[2:])):
                zero += '0'
            hexnum = hexnum1[:1]+zero+hexnum1[2:]
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage('Error! \nError number: '+hexnum+'. \nError name: '+name+'.')
        if len(text) > 4:
    	    n = 0
        else:
            n = 4
        if n == 0:
            self.pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"))
            self.lbl3.setPalette(self.pal)
            self.lbl3.setText('Вы выбрали: '+text)
            if text == 'Зашифровать':
                self.de = 'en'
            else:
                self.de = 'decr'
        else:
            self.pal4.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"))
            self.lbl34.setPalette(self.pal4)
            self.lbl34.setText('Вы выбрали: '+text)
            if text == 'Да  ':
                self.df = 'Yes'
            else:
                self.df = 'no'
    def buttonClicked(self):
        def errmsg(name, num):
            hexnum1 = hex(num)
            zero = ''
            for i in range(11-len(hexnum1[2:])):
                zero += '0'
            hexnum = hexnum1[:1]+zero+hexnum1[2:]
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage('Error! \nError number: '+hexnum+'. \nError name: '+name+'.')
        def sha512(password):
            return int(hashlib.sha512(password.encode('utf-8')).hexdigest(), 16)
        def encfile (password, infile, outfile):
            start = datetime.datetime.now()
            with open(infile, "rb") as handle:
                data = handle.readlines()
                bet = len(b''.join(data))
            if bet > 10000000:
                reply = QMessageBox.question(self, 'Предупреждение', "Размер вашего файла превышает 10 МБайт. Вы точно хотите продолжить?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    pass
                else:
                    exit()
            shaint = sha512(password)
            beta = b''.join(data)
            aleph = int.from_bytes(beta, byteorder='big')
            l = aleph*shaint
            gamma = l.to_bytes((len(bin(l))// 8) + 1, byteorder='big')
            ac = b''
            for i in data[0]:
                if 0 == i:
                    ac += b'\x00'
                else:
                    break
            ab = len(ac)
            c = ab.to_bytes(len(bin(ab))//8 +1, byteorder='big')    
            c += b'\n'
            c += gamma
            with open(outfile, "wb") as handle1:
                handle1.write(c)
            end = datetime.datetime.now()
            time = end - start
            reply = QMessageBox.question(self, 'Зашифровано', "Программа работала "+str(time)+'времени.', QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass
            else:
                pass
        def decfile (password, infile, outfile):
            start = datetime.datetime.now()
            with open(infile, "rb") as handle:
                data = handle.readlines()
                bet = len(b''.join(data))
            shaint = sha512(password)
            a = list(data[0]).copy()
            a.pop()
            ac = b''
            for i in range(a[0]):
                ac += b'\x00'
            neid = b''.join(data[1:])
            aleph = int.from_bytes(neid, byteorder='big')
            l = aleph // shaint
            gamma = l.to_bytes((len(bin(l)) // 8) + 1, byteorder='big')[1:]
            ac += gamma
            with open(outfile, "wb") as handle1:
                handle1.write(ac)
            end = datetime.datetime.now()
            time = end - start
            reply = QMessageBox.question(self, 'Расшифровано', "Программа работала "+str(time)+'времени.', QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass
            else:
                pass
        def desfile(file):
            with open(file, 'rb') as f0:
                    data = f0.readlines()
                    b = 0
                    for i in data:
                        b += len(list(i))
            for i in range(10):
                with open(file, 'wb') as f1:
                    f1.write(os.urandom(b))
            os.remove(file)
        sender = self.sender().text()
        if sender == 'Шифровать!':
            reply = QMessageBox.question(self, 'Encryption', "Вы уверены, что ввели все правильно?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                if 'en' in self.de:
                    if self.outfile == 'def':
                        c = self.df
                        if 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c:
                            try:
                                encfile(self.password, self.infile, self.infile+'.crypt0')
                                desfile(self.infile)
                            except Exception:
                                errmsg(1000, 'Unknown error')
                        else:
                            try:
                                encfile(self.password, self.infile, self.infile+'.crypt0')
                            except Exception:
                                errmsg(1010, 'Unknown error')
                    else:
                        c = self.df
                        if 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c:
                            try:
                                encfile(self.password, self.infile, self.outfile)
                                desfile(self.infile)
                            except Exception:
                                errmsg(1020, 'Unknown error')
                        else:
                            try:
                                encfile(self.password, self.infile, self.outfile)
                            except Exception:
                                errmsg(1030, 'Unknown error')
                else:
                    if self.outfile == 'def':
                        c = self.df
                        if 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c:
                            try:
                                decfile(self.password, self.infile, self.infile[:-7])
                                desfile(self.infile)
                            except Exception:
                                errmsg(1040, 'Unknown error')
                        else:
                            try:
                                decfile(self.password, self.infile, self.infile[:-7])
                            except Exception:
                                errmsg(1050, 'Unknown error')
                    else:
                        c = self.df
                        if 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c:
                            try:
                                decfile(self.password, self.infile, self.outfile)
                                desfile(self.infile)
                            except Exception:
                                errmsg(1060, 'Unknown error')
                        else:
                            try:                         
                                decfile(self.password, self.infile, self.outfile)
                            except Exception:
                                errmsg(1070, 'Unknown error')
            else:
                pass
        elif sender == 'Случайный пароль':
            self.password = ''.join(random.sample(self.en, 12))
            self.lbl31.setText('Ваш пароль(не забудьте скопировать!): '+self.password)
        else:
            self.outfile = 'def'
            self.pal3.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"))
            self.lbl33.setPalette(self.pal3)
            self.lbl33.setText('Итоговый файл: по умолчанию')
    def onChanged(self, text):
        def errmsg(name, num):
            hexnum1 = hex(num)
            zero = ''
            for i in range(11-len(hexnum1[2:])):
                zero += '0'
            hexnum = hexnum1[:1]+zero+hexnum1[2:]
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage('Error! \nError number: '+hexnum+'. \nError name: '+name+'.')
        sender = self.sender().text()[:2]
        if sender == '2)':
            self.password = text[2:]
            if self.password != '':
                if self.password[0] == ' ':
                    self.password = self.password[1:]
                    self.pal1.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"))
                    self.lbl31.setPalette(self.pal1)
                    self.lbl31.setText('Ваш пароль: '+text[2:])
                else:
                    self.pal1.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"))
                    self.lbl31.setPalette(self.pal1)
                    self.lbl31.setText('Ваш пароль: '+text[2:])
        if sender == '3)':
            self.pal2.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"))
            self.lbl32.setPalette(self.pal2)
            self.lbl32.setText('Исходный файл: '+text[2:])
            self.infile = text[2:]
            if self.infile != '':
                if self.infile[0] == ' ':
                    self.infile = self.infile[1:]
        if sender == '4)':
            self.pal3.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"))
            self.lbl33.setPalette(self.pal3)
            self.lbl33.setText('Итоговый файл: '+text[2:])
            self.outfile = text[2:]
            if self.outfile != '':
                if self.outfile[0] == ' ':
                    self.outfile = self.outfile[1:]
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', "Вы точно хотите выйти?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
def help():
    if 0 == 0:
        print('Использование:')
        print('  crypt0 <опции1> <опции2>')
        print('Опции1:')
        print('  Зашифровка:')
        print('    "-e" или "-en" или "--encr" или "--encrypt"')
        print('  Расшифровка:')
        print('    "-d" или "-de" или "--decr" или "--decrypt"')
        print('  Справка:')
        print('    "--help"')
        print('Опции2:')
        print('  "-rp" - случайный пароль(только при зашифровке)')
        print('  "-p" - следующий аргумент - пароль')
        print('  "-if" - следующий аргумент - путь к исходному файлу')
        print('  "-of" - следующий аргумент - путь к конечному файлу')
        print('  "-df" - путь к конечному файлу по умолчанию')
        print('  "-dd" - уничтожить исходный файл')
def sha512(password):
    return int(hashlib.sha512(password.encode('utf-8')).hexdigest(), 16)
def encfile (infile, outfile, password):
    print('Начинается шифрование...')
    start = datetime.datetime.now()
    print('Время начала шифрования', str(start))
    with open(infile, "rb") as handle:
        data = handle.readlines()
        bet = len(b''.join(data))
    print('Файл имеет размер', bet/1000, 'KiB')
    if bet > 10000000:
        print('!!!ВНИМАНИЕ!!!')
        print('Размер вашего файла превышет 10 мегабайт.')
        c = input('Вы точно хотите продолжить?(yes/no): ')
        cb = 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c
        if cb == False: 
            exit()
    shaint = sha512(password)
    beta = b''.join(data)
    aleph = int.from_bytes(beta, byteorder='big')
    l = aleph*shaint
    gamma = l.to_bytes((len(bin(l))// 8) + 1, byteorder='big')
    ac = b''
    for i in data[0]:
        if 0 == i:
            ac += b'\x00'
        else:
            break
    ab = len(ac)
    c = ab.to_bytes(len(bin(ab))//8 +1, byteorder='big')    
    c += b'\n'
    c += gamma
    with open(outfile, "wb") as handle1:
        handle1.write(c)
    print('Шифрование окончено! Ваши данные в безопасности!')
    end = datetime.datetime.now()
    time = end - start
    print('Программа закончила выполнение в', str(end))
    print('Программа работала', str(time), 'времени')
def decfile (infile, outfile, password):
    print('Начинаем расшифровку...')
    start = datetime.datetime.now()
    print('Время начала шифрования', str(start))
    with open(infile, "rb") as handle:
        data = handle.readlines()
        bet = len(b''.join(data))
    print('Файл имеет размер', bet/1000, 'KiB')
    shaint = sha512(password)
    a = list(data[0]).copy()
    a.pop()
    ac = b''
    for i in range(a[0]):
        ac += b'\x00'
    neid = b''.join(data[1:])
    aleph = int.from_bytes(neid, byteorder='big')
    l = aleph // shaint
    gamma = l.to_bytes((len(bin(l)) // 8) + 1, byteorder='big')[1:]
    ac += gamma
    with open(outfile, "wb") as handle1:
        handle1.write(ac)
    print('')
    print('Файл расшифрован.')
    end = datetime.datetime.now()
    time = end - start
    print('Программа закончила выполнение в', str(end))
    print('Программа работала', str(time), 'времени')
def desfile(file):
    with open(file, 'rb') as f0:
            data = f0.readlines()
            b = 0
            for i in data:
                b += len(list(i))
    for i in range(10):
        with open(file, 'wb') as f1:
            f1.write(os.urandom(b))
    os.remove(file)
def encr(args):
    password = ' '
    infile = ' '
    outfile = ' '
    dd = False
    for i in range(len(args)):
        a = args[i]
        if i != (len(args) - 1):
            b = args[i+1]
            if a == '-rp':
                password = ''.join(random.sample(en, 12))
                print('Ваш пароль:', password)
            if a == '-p':
                password = b
            if a == '-if':
                infile = b
            if a == '-of':
                outfile = b
            if a == '-df':
                outfile = infile + '.crypt0'
            if a == '-dd':
                dd = True
        else:
            if a == '-dd':
                dd = True
            if a == '-rp':
                password = ''.join(random.sample(en, 12))
                print('Ваш пароль:', password)
            if a == '-df':
                outfile = infile + '.crypt0'
    if outfile != ' ' and infile != ' ' and password != ' ':
        try:
           encfile(infile, outfile, password)
           if dd == True:
                desfile(infile)
        except Exception:
           print('Unknown error')
    else:
        print('Ошибка! Неверные значения параметров!')
        help()
def decr(args):
    password = ' '
    infile = ' '
    outfile = ' '
    dd = False
    for i in range(len(args)):
        a = args[i]
        if i != (len(args) - 1):
            b = args[i+1]
            if a == '-rp':
                password = ''.join(random.sample(en, 12))
                print('Ваш пароль:', password)
            if a == '-p':
                password = b
            if a == '-if':
                infile = b
            if a == '-of':
                outfile = b
            if a == '-df':
                outfile = infile[:-7]
            if a == '-dd':
                dd = True
        else:
            if a == '-dd':
                dd = True
            if a == '-df':
                outfile = infile[:-7]
    if outfile != ' ' and infile != ' ' and password != ' ':
        try:
            decfile(infile, outfile, password)
            if dd == True:
                desfile(infile)
        except Exception:
            print('Unknown error')
    else:
        print('Ошибка! Неверные значения параметров!')
        help()
if __name__ == '__main__':
    def cui():  #Console User Interface
        arg = sys.argv[1:].copy()
        if arg[0] == '-e' or arg[0] == '-en' or arg[0] == '--encr' or arg[0] == '--encrypt':
            encr(arg[1:])
        elif arg[0] == '-d':
            decr(arg[1:])
        elif arg[0] == '--help':
            print('Справка.')
            help()
        else:
            print('Неправильный первый аргумент!')
            help()
    def errmsg(name, num):
        hexnum1 = hex(num)
        zero = ''
        for i in range(11-len(hexnum1[2:])):
            zero += '0'
        hexnum = hexnum1[:1]+zero+hexnum1[2:]
        error_dialog = QtWidgets.QErrorMessage(self)
        error_dialog.showMessage('Error! \nError number: '+hexnum+'. \nError name: '+name+'.')
    try:
        app = QApplication(sys.argv)
        ex = Example()
        if len(sys.argv) != 1:
            cui()
        else:
            sys.exit(app.exec_())
    except Exception:
        errmsg(1111, 'Unknown error')
