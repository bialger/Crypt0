#!/usr/bin/python3
import hashlib
import random
import datetime
import os
import sys
#The Zen of Python, by Tim Peters
#
#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.
#Flat is better than nested.
#Sparse is better than dense.
#Readability counts.
#Special cases aren't special enough to break the rules.
#Although practicality beats purity.
#Errors should never pass silently.
#Unless explicitly silenced.
#In the face of ambiguity, refuse the temptation to guess.
#There should be one-- and preferably only one --obvious way to do it.
#Although that way may not be obvious at first unless you're Dutch.
#Now is better than never.
#Although never is often better than *right* now.
#If the implementation is hard to explain, it's a bad idea.
#If the implementation is easy to explain, it may be a good idea.
#Namespaces are one honking great idea -- let's do more of those!
print('Crypt0, version 4.0 . ', str(datetime.datetime.now()))  #Пользователь должен знать, что и когда он юзает!
print('Programm is written by Alexander Bigulov aka bialger. Github: https://github.com/bialger/Crypt0')  #Как же себя любимого не показать!
en = ['q','w','e','r','t','y','u','i','o','p','[',']',
      'a','s','d','f','g','h','j','k','l',';',
      'z','x','c','v','b','n','m',',','.','/',  
      '1','2','3','4','5','6','7','8','9','0','=',
      '~','!','(',')','+',
      'Q','W','E','R','T','Y','U','I','O','P',
      'A','S','D','F','G','H','J','K','L',':',
      'Z','X','C','V','B','N','M',]
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
def tui():  #Text User Interface
    omega = input('Шифровать или расшифровать(e/d): ')  #Выбор того, какой метод юзать
    if omega == 'e':  #Если нужно зашифровать
        password = input('Пароль(оставте пустым для генерации надёжного пароля): ')  #Принимает или ничего, или строку, которая будет паролем.
        if password == '':  #Если ничего не ввёл юзер, захотел, чтоб мы сгенерировали пасс
            password = ''.join(random.sample(en, 12))
        print('Ваш пароль: '+password)  #Чтобы юзер уверился
        print('Не забудьте его!')  #Напоминание
        file = input('Файл для шифрования: ')  #Что шифровать, сударь?
        file1 = input('Зашифрованный файл(оставте пустым для имени по умолчанию):  ')  #Куда зашифровать? 
        if file1 == '':  #Дефолтное значение - имя_исходного_файла.crypt0
            file1 = file  # Приравниваем
        file1 += '.crypt0'  #Показываем отличия
        try:  #Ловим исключение, абсолютно любое!
            encfile(file, file1, password)  #Пытаемя вызвать метод шифрования
        except Exception:  #Смотрит на любое исключение
            print('Что-то пошло не так. Возможно, имя файла неправильное. Попробуйте перезапустить программу. Код ошибки 0b000011')  #Сообщение об ошибке
        c = input('Удалить изначальный файл(yes/no)? ')  #Вдруг юзер захотел супер-секурности
        if 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c:
            desfile(file)  #Запускаем затирание этого файла
    else:  #Если же нужно расшифровать
        password = input('Пароль: ')  #Просим пароль
        file1 = input('Зашифрованный файл: ')  #Спрашиваем про зашифрованный файл - куда без этого
        file3 = input('Расшифрованный файл(оставте пустым для имени по умолчанию): ')  #Расшифрованный файл(возможен варисант "по умолчанию")
        try:  #Ловим любое исключение, так проще
            if file3 == '':  #Если ввод это ничего, то ....
                file3 = file1[:-7]
            decfile(file1, file3, password)  #Вызываем метод расшифровки
        except Exception:  #Ловим любое исключение на этом участке
            print('Что-то пошло не так. Возможно, пароль неправильный или имя файла. Попробуйте перезапустить программу. Код ошибки 0b00000010')  #Сообщение об ошибке
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
        encfile(infile, outfile, password)
        if dd == True:
            desfile(infile)
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
        decfile(infile, outfile, password)
        if dd == True:
            desfile(infile)
    else:
        print('Ошибка! Неверные значения параметров!')
        help()
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
try:  #Ловим прерывания от клавиатуры и любое другое
    if len(sys.argv) == 1:
        tui()
    else:
        cui()
except KeyboardInterrupt:
    print('\nПрограмма принудительно остановлена пользователем.', str(datetime.datetime.now()), 'Код ошибки 0b00000001')  #Если вызвано прерывание клавиатуры - это пользователь остановил программу! Надо ему об этом сказать! И повыпендриваться с временем не забыть!
except Exception:
    print('Что-то пошло не так. Попробуйте перезапустить программу. Код ошибки 0b00000000')
