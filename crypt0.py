#!/usr/bin/python3
import hashlib
import random
import datetime
import os
print('Crypt0, version 3.0.1 ', str(datetime.datetime.now()))  #Пользователь должен знать, что и когда он юзает!
print('Programm is written by Alexander Bigulov(a. k. a. bialger). \nGithub: https://github.com/bialger/Crypt0')  #Как же себя любимого не показать!
en = ['q','w','e','r','t','y','u','i','o','p','[',']',
      'a','s','d','f','g','h','j','k','l',';',"'",
      'z','x','c','v','b','n','m',',','.','/',  
      '`','1','2','3','4','5','6','7','8','9','0','-','=',
      '~','!','@','#','$','%','^','&','*','(',')','_','+',
      'Q','W','E','R','T','Y','U','I','O','P','{','}',
      'A','S','D','F','G','H','J','K','L',':','"',
      'Z','X','C','V','B','N','M','<','>','?',]
def hash (password):
    sha = hashlib.sha512(password.encode('utf-8')).hexdigest()
    return int(sha, 16)
def encfile (file, file1, password):
    print('Начинается шифрование...')
    start = datetime.datetime.now()
    print('Время начала шифрования', str(start))
    handle = open(file, "rb")
    data = handle.readlines()
    handle.close()
    if list(data[0])[0] == 0:
    	print('Извините. Этот файл не может быть зашифрован по техническим причинам.')
    	exit()
    handle1 = open(file1, "wb")
    shaint = hash(password)
    beta = b''.join(data)
    bet = len(beta)
    print('Файл имеет размер', bet/1000, 'KiB')
    if bet > 25000000:
        print('!!!ВНИМАНИЕ!!!')
        print('Размер вашего файла превышет 25 мегабайт.')
        print('Его зашифровка займет довольно большое время.')
        c = input('Вы точно хотите продолжить?(yes/no): ')
        cb = 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c
        if cb == False: 
            exit()
    aleph = int.from_bytes(beta, byteorder='big')
    l = aleph*shaint
    gamma = l.to_bytes((len(bin(l))// 8) + 1, byteorder='big')
    handle1.write(gamma)
    handle1.close()
    print('Шифрование окончено! Ваши данные в безопасности!')
    end = datetime.datetime.now()
    time = end - start
    print('Программа закончила выполнение в', str(end))
    print('Программа работала', str(time), 'времени')
def decfile (file2, file3, password):
    print('Начинаем расшифровку...')
    print('!!!ПРИМЕЧАНИЕ!!! ')
    print('В случае большого размера файла расшифровка может длиться долго.')
    start = datetime.datetime.now()
    print('Время начала шифрования', str(start))
    handle = open(file2, "rb")
    data = handle.readlines()
    handle.close()
    handle1 = open(file3, "wb")
    shaint = hash(password)
    beta= b''.join(data)
    bet = len(b''.join(data))
    print('Файл имеет размер', bet/1000, 'KiB')
    aleph = int.from_bytes(beta, byteorder='big')
    l = aleph // shaint
    gamma = l.to_bytes((len(bin(l)) // 8) + 1, byteorder='big')[1:]
    handle1.write(gamma)
    handle1.close()
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
try:  #Ловим прерывания от клавиатуры
    o = input('Зашифровать или расшифровать? (encr/decr): ')  #Выбор того, какой метод юзать
    if o == 'e' or o == 'enc' or o =='encr' or o == 'encrypt':  #Если нужно зашифровать
        password = input('Пароль(оставте пустым для генерации надёжного пароля): ')  #Принимает или ничего, или строку, которая будет паролем.
        if password == '':  #Если ничего не ввёл юзер, захотел, чтоб мы сгенерировали пасс
            for i in range(12):  #12 символьный пароль
                password = ''.join(random.sample(en, 12)) #Генерируем случайную строку из массива en - букв, знаков препинания и цифр
        print('Ваш пароль: '+password)  #Чтобы юзер уверился
        file = input('Файл для шифрования: ')  #Что шифровать, сударь?
        file1 = input('Зашифрованный файл(оставте пустым для имени по умолчанию):  ')  #Куда зашифровать? 
        if file1 == '':  #Дефолтное значение - имя_исходного_файла.crypt0
            file1 = file  # Приравниваем
        file1 += '.crypt0'  #Показываем отличия
        try:  #Ловим исключение, абсолютно любое!
            encfile(file, file1, password)  #Пытаемя вызвать метод шифрования
        except Exception:  #Смотрит на любое исключение
            print('Что-то пошло не так. Возможно, пароль неправильный или имя файла. Попробуйте перезапустить программу.')  #Сообщение об ошибке
        xi = input('Удалить изначальный файл? (yes/no): ')  #Вдруг юзер захотел супер-секурности
        if xi == 'yes' or xi == 'y':  #Если 0, то
        	try:
        		desfile(file)  #Запускаем затирание этого файла
        	except Exception:
        		print('Что-то случилось с именем файла. Попробуйте перезапустить программу и указать имя файла по другому')
    else:  #Если же нужно расшифровать
        password = input('Пароль: ')  #Просим пароль
        file1 = input('Зашифрованный файл: ')  #Спрашиваем про зашифрованный файл - куда без этого
        file3 = input('Расшифрованный файл(оставте пустым для имени по умолчанию): ')  #Расшифрованный файл(возможен варисант "по умолчанию")
        try:  #Ловим любое исключение, так проще
            if file3 == '':  #Если ввод это ничего, то ....
                file3 = file1[:-7]  #Делаем из массива строку
            decfile(file1, file3, password)  #Вызываем метод расшифровки
        except Exception:  #Ловим любое исключение на этом участке
            print('Что-то пошло не так. Возможно, пароль неправильный или имя файла. Попробуйте перезапустить программу.')  #Сообщение об ошибке
except KeyboardInterrupt:
    print('\nПрограмма принудительно остановлена пользователем.', str(datetime.datetime.now()))  #Если вызвано прерывание клавиатуры - это пользователь остановил программу! Надо ему об этом сказать! И повыпендриваться с временем не забыть!
except Exception:
	print('Что-то пошло не так. Попрубуйте перезапустить программу')
