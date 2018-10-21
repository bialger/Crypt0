#!/usr/bin/python3
import hashlib
import random
import datetime
print('Crypt0, версия 3.0. ', str(datetime.datetime.now()))  #Пользователь должен знать, что и когда он юзает!
print('Программа написана Александром Бигуловым. Github: https://github.com/bialger/Crypt0')  #Как же себя любимого не показать!
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
    handle1 = open(file1, "wb")
    shaint = hash(password)
    beta = data[0]
    for bet in data[1:]:
    	beta +=bet
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
    neid = data[0]
    for nein in data[1:]:
    	neid += nein
    aleph = int.from_bytes(neid, byteorder='big')
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
    handle = open(file, "w")
    weisses_fleisch = []
    handle.writelines(weisses_fleisch)
    handle.close()
try:  #Ловим прерывания от клавиатуры
    omega = input('Введите опцию. Для зашифровки - 0, для расшифровки - любые символы: ')  #Выбор того, какой метод юзать
    if omega == '0':  #Если нужно зашифровать
        password = input('Пароль(оставте пустым для генерации надёжного пароля): ')  #Принимает или ничего, или строку, которая будет паролем.
        if password == '':  #Если ничего не ввёл юзер, захотел, чтоб мы сгенерировали пасс
            for i in range(12):  #12 символьный пароль
                a = random.randint(0, (len(en) - 1))  #Генерируем случайное число по длине массива en - букв, знаков препинания и цифр
                alpha = en[a]  #Берем элемент со случайным индексом
                password += alpha  #Добавляем ЭТО в строку пароля
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
            print('Что-то пошло не так. Возможно, пароль неправильный или имя файла. Попробуйте перезапустить программу.')  #Сообщение об ошибке
        xi = input('Удалить изначальный файл?. Для удаления - 0, для завершения скрипта - любые символы: ')  #Вдруг юзер захотел супер-секурности
        if xi == '0':  #Если 0, то
            desfile(file)  #Запускаем затирание этого файла
    else:  #Если же нужно расшифровать
        password = input('Пароль: ')  #Просим пароль
        file1 = input('Зашифрованный файл: ')  #Спрашиваем про зашифрованный файл - куда без этого
        file3 = input('Расшифрованный файл(оставте пустым для имени по умолчанию): ')  #Расшифрованный файл(возможен варисант "по умолчанию")
        try:  #Ловим любое исключение, так проще
            if file3 == '':  #Если ввод это ничего, то ....
                afile3 = list(file1)  #Разделяем имя зашифрованного файла на символы
                for i in range(7):  #Семь символов...  на этом моменте может случиться exception
                    afile3.pop()  #Убираем с конца (.crypt0)
                file3 = ''.join(afile3)  #Делаем из массива строку
            decfile(file1, file3, password)  #Вызываем метод расшифровки
        except Exception:  #Ловим любое исключение на этом участке
            print('Что-то пошло не так. Возможно, пароль неправильный или имя файла. Попробуйте перезапустить программу.')  #Сообщение об ошибке
except KeyboardInterrupt:
    print('\nПрограмма принудительно остановлена пользователем.', str(datetime.datetime.now()))  #Если вызвано прерывание клавиатуры - это пользователь остановил программу! Надо ему об этом сказать! И повыпендриваться с временем не забыть!
