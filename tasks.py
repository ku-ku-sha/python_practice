from typing import Union


# Встроенные функции python
def delete_a(n: str) -> Union[tuple, int]:
    '''В строке удалить все буквы "а"  и подсчитать количество удаленных символов
    Функция удаляет строчные и заглавные буквы а английского и русского алфавита, результатом является кортеж (<строка, которая не содержит а>, <количество удаленных символов>)'''
    try:
        len_n = len(n)
        for i in 'aAаА':
            n = n.replace(i, '')
        return n, len_n - len(n)
    except TypeError:
        print('Invalid input type')
        return -1


def phone_number(n: str) -> Union[bool, int]:
    '''Проверить, что номера телефонов состоят только из цифр. Они могут начинаться с «+», цифры могут быть разделены пробелами и дефисами «-»
    Например: 8-999-777-1111, +7 999 333 2222, +7 999-555-11-11'''
    from re import fullmatch
    num = '0123456789+- '
    try:
        if len(n) == 0 or n.strip(
                num) != 0:  # проверка того, что ввод непустой и не содержит символов, кроме цифр, пробелов, символов "+" и "-" - блок удовлетворяет условию задания
            print('Invalid phone number')
            return False
        else:  # проверка соответствия номера формату (используются регулярные выражения)
            phone_format = r'[+]?([7|8])[ -]([0-9]{3})[- ]([0-9]{3})[- ]([0-9]{2})(-)?([0-9]{2})' #подходит для всех вариантов номера, перечисленных в примере
            if fullmatch(phone_format, n) == n:
                return True
            else:
                return False
    except TypeError:
        print('Invalid input type')
        return -1


def get_file_name(n: str) -> Union[str, int]:
    '''Дана строка, содержащая полное имя файла (например, C:\development\inside\test-project_management\inside\myfile.txt'). Выделите из этой строки имя файла без расширения
    Полное имя файла указывается в формате ОС Windows'''
    try:
        if '\\' not in n:
            print('Invalid full file name')  # при отсутствии слешей полный путь к файлу считается некорректным
            return ''
        else:
            result = n.split('\\')
            if '.' not in result[-1]:  # при отсутствии точки, последнее значение является именем папки
                print('File name not found')
                return ''
            else:
                return result[-1].split('.')[0]

    except TypeError:
        print('Invalid input type')
        return -1


def swap_min_max(n: list) -> Union[list, int]:
    '''Поменять местами самый большой и самый маленький элементы списка
    Функция позволяет обрабатывать списки строк и списки чисел'''
    if isinstance(n, list):
        type_n = type(n[0])
        match str(type_n):
            case 'str':
                check_all = list(map(lambda x: type(x) == str, n))#проверка: все элементы можно сравнить с начальным (вариант с циклом менее затратный тк прерывается при нахождении 1го эл-та, не соответствующего условию, представлен в ветке ---)
                if all(check_all):
                    min_el = min(n)
                    max_el = max(n)
                    n[n.index(min_el)], n[n.index(max_el)] = n[n.index(max_el)], n[n.index(min_el)] #меняем местами мин и макс
                    return n
                else:
                    print('List elements cannot be compared')
                    return -1
            case 'int' | 'float':
                check_all = list(map(lambda x: type(x) in (int, float)), n)
                if all(check_all):
                    min_el = min(n)
                    max_el = max(n)
                    n[n.index(min_el)], n[n.index(max_el)] = n[n.index(max_el)], n[n.index(min_el)] #меняем местами мин и макс
                    return n
                else:
                    print('List elements cannot be compared')
                    return -1
            case _:
                print('List elements cannot be compared')
                return -1

    else:
        print('Invalid input type (List required)')
        return -1

def most_expensive_product(n: dict):
    '''Дан список словарей:
# [{“наименование”: “Спички”, “цена”: 1},  {“наименование”: “Лук”, “цена”: 37},  … , {“наименование”: str, “цена”: int}]
# Найти ТОП-2 самых дорогих товаров и вывести в том же формате.'''
    if len(n) <= 2:
        return n
    while len(n) > 2:
        pass

def count_lucky_tickets() -> int:
    '''Напишите функцию, которая подсчитывает количество счастливых шестизначных билетов'''
    sums = [i for i in range(0, 28)] # варианты сумм 3х чисел 0-9


def func_time(func):
    start_time =
    func
    end_time =
    return end_time - start_time


1) Получить список файлов в папке

2) Получить текущую директорию

3) Создать папку

4) Склеить путь из папки и файла

5) Посчитать сколько в каталоге установки python:•папок•файлов с расширением ".py"•файлов с расширением ".exe"•всего файлов•Записать результаты в файл

1) Получить текущую дату +5 дней в формате ДД.ММ.ГГ
2) Получить текущую дату в формате ДД.ММ.ГГГГ
3) На входе есть строка '03.05.13' надо к этой дате прибавить 10 дней и вывести в формате ДД.ММ.ГГГГ
4) Вывести дату в формате ДД.ММ.ГГ, эта дата должна быть первым днем месяца
5) Вывести дату в формате ДД.ММ.ГГ, эта дата должна быть последним днем месяца
6) Прибавить к любой дате 1 месяц и вывести в формате ДД.ММ.ГГГГ
7) Написать функцию change_month, которая к переданной дате прибавляет/вычитает переданное кол-во месяцев.Например:
change_month(’12.12.12’, 7) -> ’12.07.13’ change_month(’01.11.10’, -5) -> ’01.06.10’