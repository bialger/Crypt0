#!/usr/bin/python3
#Эта программа шифрует текстовые файлы надежнее многих других
#В основе программы лежит мой собственный алгоритм шифррвания
# Выберите надежный пароль
#Чем больше файл, тем сложнее его расшифровать
#Программа написана Александром Бигуловым
import hashlib
def hash (password):
    sha = hashlib.sha512(password.encode('utf-8')).hexdigest()
    return int(sha, 16)
def encfile (file, file1):
    print('Начинается шифрование...')
    print('')
    handle = open(file, "r")
    data = handle.readlines()
    handle.close()
    handle1 = open(file1, "w")
    shaint = hash(password)
    array = list()
    for promt in data:
        cp = list(promt)
        a1 = []
        cp.pop()
        for bt in cp:
            l = str(ord(bt)*shaint) + "'"
            a1.append(l)
        neid = ''
        for alpha1 in a1:
            neid += alpha1
        array.append(neid)
        array.append('\n')
    handle1.writelines(array)
    handle1.close()
    print('Шифрование окончено! Ваши данные в безопасности!')
def decfile (file2, file3):
    print('Начинаем расшифровку...')
    print('!!!ПРИМЕЧАНИЕ!!! ')
    print('В случае большого размера файла расшифровка может длиться долго.')
    handle = open(file2, "r")
    data = handle.readlines()
    handle.close()
    handle1 = open(file3, "w")
    shaint = hash(password)
    array = []
    for promt in data:
        cp = list(promt)
        a1 = []
        bts = ''
        for bt in cp:
            if bt != "'":
                bts += bt
            else:
                hailfish = chr(int(int(bts)/ shaint))
                a1.append(hailfish)
                bts = ''
        neid = ''
        for alpha1 in a1:
            neid += alpha1
        lifad = neid + '\n'
        array.append(lifad)
    handle1.writelines(array)
    handle1.close()
    print('')
    print('Файл расшифрован.')
def desfile(file):
    handle = open(file, "w")
    weisses_fleisch = []
    handle.writelines(weisses_fleisch)
    handle.close()
omega = input('Введите опцию. Для зашифровки - 0, для расшифровки - 1: ')
if omega == '0':
    password = input('Пароль: ')
    file = input('!!!ТЕКСТОВЫЙ!!! файл для шифрования: ')
    file1 = input('Зашифрованный файл: ')
    file1 += '_crypt0'
    encfile(file, file1)
    xi = input('Удалить изначальный файл?. Для удаления - 0, для завершения скрипта - 1: ')
    if xi == '0':
        desfile(file)
else:
    password = input('Пароль: ')
    file1 = input('Зашифрованный файл: ')
    file3 = input('Расшифрованный файл: ')
    decfile(file1, file3)
