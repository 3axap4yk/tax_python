import logic
import data
import webbrowser as web

def tax():
    x = 0
    while x == 0:
        try:
            gross = int(input('Введите ГРОСС: '))
            x += 1
        except ValueError:
            print('Неверный формат!')
            logic.tire()

    y = 0
    while y == 0:
        countryCode = input('Введите код страны: ')
        countryCodeUP = countryCode.upper()
        if countryCodeUP in data.countryInfo:
            logic.loading()
            logic.calculatigTax(gross, countryCodeUP)
            y += 1
        else:
            print('Страна не найдена!')
            logic.tire()


def append():
    logic.tire()
    print('Добавить страну')

    abc = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    x = 0
    while x != 3:
        key = input('Ведите код страны: ')
        keyUP = key.upper()
        if len(keyUP) == 2:
            x = 1
            if keyUP[0] in abc and keyUP[1] in abc:
                x = 2
                if keyUP in data.countryInfo:
                    print('Эта страна уже есть в списке!')
                    logic.tire()
                else:
                    x = 3
            else:
                print('Вы используете неверные символы!')
                logic.tire()
        else:
            print('Символов должно быть 2!')
            logic.tire()

    y = 0
    while y != 1:
        try:
            value = float(input('Введите процент в десятичной форме: '))
            if value > 1.0:
                value /= 100
            y = 1
        except ValueError:
            print('Неверный формат!')
            logic.tire()

    logic.dictAppend(keyUP, value)

##ВХОД##
logic.tire()
print('Здесь Вы можете подсчитать НЕТ в разных странах')
while True:
    while True:
        logic.tire()
        print('1. Сделать рассчет\n2. Добавить страну\n3. Посмотреть таблицу кодов в браузуре\n4. Выйти')
        try:
            change = int(input())
            break
        except ValueError:
            print('Неверный формат!')
            logic.tire()

    if change == 1:
        tax()
    if change == 2:
        saveData = data.countryInfo
        append()
    if change == 3:
        web.open('https://countrycode.org')
    if change == 4:
        break
