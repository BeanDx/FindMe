import time
import os
from urllib import request
import webbrowser as wb

def main():
    print("====░=====░=====░==░=░======░=░=====░=====░==░=====░=====░==░=░======░")
    print("Made by: BeanD        FindMe            TG: https://t.me/BeanD_TM")
    print("====░=====░=====░==░=░======░=░=====░=====░==░=====░=====░==░=░======░")
    print("                             |                             ")
    print("                             |                             ")
    print("                             V                             ")

    print("1 - Да")
    print("2 - Нет")
    quest = int(input("Вы желаете продолжить? "))

    if quest == 1:
        loading()

    elif quest == 2:
        exit()

    else:
        main()



def loading():
    if os.sys.platform == "win32":
                os.system("cls")
    else:
                os.system("clear")
    
    print('             ПОДОЖДИТЕ ПОЖАЛУЙСТА! ЗАГРУЗКА!             ')
    print('')

    print('==', end=' 5% ')
    time.sleep(.50)
    print('==', end=' 10% ')
    time.sleep(.75)
    print('==', end=' 15% ')
    time.sleep(1)
    print('====', end=' 20% ')
    time.sleep(1.50)
    print('========', end=' 43% ')
    time.sleep(1.50)
    print('======', end=' 64% ')
    time.sleep(1.50)
    print('=====', end=' 75% ')
    time.sleep(1.75)
    print('=======', end=' 95% ')
    time.sleep(1)
    print('=======', end=' 99% ')
    time.sleep(.25)
    print('== 100% ')
    print('')

    print("             ЗАГРУЗКА УСПЕШНО ЗАВЕРШЕНА!             ")

    time.sleep(2)
    if os.sys.platform == "win32":
                os.system("cls")
    else:
                os.system("clear")

    logic()

def logic():
    print('1 - Google')
    print('2 - Yahoo')
    print('3 - Bing')
    print('4 - Yandex')
    print('5 - DuckDuckGo')
    print('6 - Вернутся в меню')
    whos = int(input('Какую поисковую систему Вы хотите использовать? '))

    if whos == 1:
        request = input("Введите ваш запрос: ")
        wb.open("https://www.google.com/search?q=" + request)

    elif whos == 2:
        request = input('Введите ваш запрос: ')
        wb.open("https://search.yahoo.com/search?p=" + request)

    if whos == 3:
        request = input('Введите ваш запрос: ')
        wb.open("https://www.bing.com/search?q=" + request)

    elif whos == 4:
        request = input('Введите ваш запрос: ')
        wb.open("https://www.yandex.ru/search/?text=" + request)

    if whos == 4:
        request = input('Введите ваш запрос: ')
        wb.open("https://duckduckgo.com/?q=" + request)

    elif whos == 6:
        main()

    else:
        logic()


main()