import data
import time
import random
# import model

#тире
def tire(): print('--'*24)

#эммитация загрузки
def loading():
    #print('Загрузка...')
    x = 0
    while x != 25:
        time.sleep(random.random()*0.3)
        print('*', end='')
        x += 1
    print('')

#вычисление налога
def calculatigTax(gross, countryCode):
    countryTax = data.countryInfo[countryCode]
    result = gross - gross*countryTax
    wrapper(result)
    print('| НЕТ составляет:', result, '|')
    wrapper(result)

#обрамение результата
def wrapper(word):
    sWord = str(word)
    print('-'*(20+len(sWord)))

#добавление информации в словарь и базу данных
def dictAppend(key, value):
    saveData = data.countryInfo
    print(f'Ваши значения:\n{key} {value}')
    while True:
        tire()
        print('Сохранить?\n1 - да\n2 - нет')
        try:
            change = int(input())
            if change == 1:
                loading()
                print('Сохранено!')
                tire()
                data.countryInfo[key] = value
                for key, value in data.countryInfo.items():
                    print(key, value)
                break
            elif change == 2:
                print('Изменения не сохранены!')
                tire()
                data.countryInfo = saveData
                for key, value in data.countryInfo.items():
                    print(key, value)
                break
            else: continue
        except ValueError:
            print('Неверный формат!')
            logic.tire()


    with open('country_info.txt', 'a+') as file:
        file.write(key)
        file.write(f' {value}\n')
