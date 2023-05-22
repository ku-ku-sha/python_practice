from typing import Union
import os


#
# Встроенные функции python
#
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


def phone_number(n: str):
    '''Проверить, что номера телефонов состоят только из цифр. Они могут начинаться с «+», цифры могут быть разделены пробелами и дефисами «-»
    Например: 8-999-777-1111, +7 999 333 2222, +7 999-555-11-11'''
    from re import fullmatch
    invalid_symbols = ''.join(filter(lambda x: x not in '0123456789+- ', n))
    numbers = ''.join(filter(lambda x: x.isdigit(), n))
    if invalid_symbols != '' or len(
            numbers) != 11:  # данные не содержат символов, кроме цифр, пробелов, символов "+" и "-", количество цифр соответствует формату
        print('Invalid phone number')
        return False
    else:  # проверка соответствия номера формату (используются регулярные выражения)
        phone_format = r'[+]?([7|8])[ -]([0-9]{3})[- ]([0-9]{3})[- ]([0-9]{2})(-)?([0-9]{2})'  # подходит для всех вариантов номера, перечисленных в примере
        if fullmatch(phone_format, n)[0] == n:
            return True
        else:
            return False


def get_file_name(n: str) -> Union[str, int]:
    '''Дана строка, содержащая полное имя файла (например, C:\development\inside\test-project_management\inside\myfile.txt'). Выделите из этой строки имя файла без расширения
    Полное имя файла указывается в формате ОС Windows'''
    from os import path
    p = path.abspath(n)
    if path.isfile(p):
        return path.basename(p)
    else:
        print('File name not found')
        return -1


def swap_min_max(n: list) -> Union[int, list]:
    '''Поменять местами самый большой и самый маленький элементы списка
    Функция позволяет обрабатывать списки строк и списки чисел'''

    if isinstance(n, list) and len(n) >= 2:
        if type(n[0]) == str:
            check_all = list(map(lambda x: type(x) == str,
                                 n))  # проверка: все элементы можно сравнить с начальным (вариант с циклом менее затратный тк прерывается при нахождении 1го эл-та, не соответствующего условию, представлен в ветке ---)
        elif type(n[0]) == int or type(n[0]) == float:
            check_all = list(map(lambda x: type(x) == int or type(x) == float, n))
        else:
            print('List elements cannot be compared')
            return -1

        if all(check_all):
            min_el = min(n)
            max_el = max(n)
            res = n[:]
            res[n.index(min_el)], res[n.index(max_el)] = res[n.index(max_el)], res[
                n.index(min_el)]  # меняем местами мин и макс
            return res
        else:
            print('List elements cannot be compared')
            return -1

    else:
        print('Invalid input data (List required)')
        return -1


def most_expensive_product(n: list):
    ''' Дан список словарей: [{“наименование”: “Спички”, “цена”: 1},  {“наименование”: “Лук”, “цена”: 37},  … , {“наименование”: str, “цена”: int}]
    Найти ТОП-2 самых дорогих товаров и вывести в том же формате.'''
    res = []
    most_expensive_prod = max(n, key=lambda x: x['цена'])
    res.append(most_expensive_prod)
    ind = n.index(most_expensive_prod)
    most_expensive_prod = max(n[:ind:] + n[ind + 1::], key=lambda x: x['цена'])
    ind = n.index(most_expensive_prod)
    res.append(most_expensive_prod)
    return res


def func_time(func):
    '''Напишите декоратор func_time, который подсчитывает и выводит сколько времени выполняется функция, обернутая в него.'''
    from datetime import datetime
    from datetime import time
    def inner(*args, **kwargs):
        start_time = datetime.today()
        result = func(*args, **kwargs)
        end_time = datetime.today()
        tmp = end_time - start_time
        print(
            f'\n\n\nФункция {func.__name__} выполнялась {str(tmp.seconds // 3600).zfill(2)}:{str(tmp.seconds // 60).zfill(2)}:{str(tmp.seconds % 60).zfill(2)}.{str(tmp.microseconds).zfill(2)}')
        return result

    return inner


@func_time
def count_lucky_tickets(k):
    '''Напишите функцию, которая подсчитывает количество счастливых шестизначных билетов'''
    def new_sum_list(sum_list):
        new_len = len(sum_list) + 9
        new_sum_list = []
        for i in range(0, new_len):
            tmp = 0
            if i < 10:
                new_sum_list.append(sum(sum_list[:i + 1]))
            else:
                new_sum_list.append(sum(sum_list[i - 9:i + 1]))
        return new_sum_list

    sum_list = [1 for _ in range(10)]
    for i in range(0, k // 2 - 1):
        sum_list = new_sum_list(sum_list)
    return sum(map(lambda x: x ** 2, sum_list))


#
# Модуль os
#


def get_file_list(dir_path):
    '''Получить список файлов в папке'''
    from os import listdir
    from os.path import isfile
    from os.path import join as os_join
    file_list = list(filter(lambda x: isfile(os_join(dir_path, x)), listdir(dir_path)))
    print(f'Список файлов в папке: {file_list}')
    return file_list


'''Получить текущую директорию'''
print(f'Текущая директория {os.getcwd()}')


def create_folder(path):
    '''Создать папку'''
    try:
        os.mkdir(path)  # указать путь
        print('Папка создана')
    except FileExistsError:
        print('Невозможно создать папку, тк папка существует')


'''Склеить путь из папки и файла'''
print(os.path.join(os.getcwd(), 'tests.py'))


def count_python(path=r'C:\Python'):
    '''Посчитать сколько в каталоге установки python: 1) папок 2)файлов с расширением ".py" 3) файлов с расширением ".exe" 4) всего файлов
    Записать результаты в файл'''
    res = {'folders': 0, 'py_files': 0, 'exe_files': 0, 'files': 0}
    for i in os.walk(path):
        res['folders'] += 1
        res['files'] += len(i[2])
        res['py_files'] += len(list(filter(lambda x: x.endswith('.py'), i[2])))
        res['exe_files'] += len(list(filter(lambda x: x.endswith('.exe'), i[2])))
    with open('result.txt', 'w') as file:
        file.write(str('folders'.ljust(12) + str(res['folders'] - 1)))
        file.write(str('\nfiles'.ljust(13) + str(res['files'])))
        file.write(str('\npy_files'.ljust(13) + str(res['py_files'])))
        file.write(str('\nexe_files'.ljust(13) + str(res['exe_files'])))


#
# Модуль datetime
#


def five_days_plus():
    '''Получить текущую дату +5 дней в формате ДД.ММ.ГГ'''
    from datetime import datetime
    n = datetime.today()
    new_date = n.replace(day=n.day + 5)
    return new_date.strftime('%d.%m.%y')


def current_date():
    '''Получить текущую дату в формате ДД.ММ.ГГГГ'''
    from datetime import datetime
    return datetime.today().strftime('%d.%m.%Y')


def ten_days_plus(n):
    from datetime import datetime
    '''На входе есть строка '03.05.13' надо к этой дате прибавить 10 дней и вывести в формате ДД.ММ.ГГГГ'''
    n = datetime.strptime(n, '%d.%m.%y')
    new_date = n.replace(day=n.day + 10)
    return new_date.strftime('%d.%m.%Y')


def first_day_of_month(any_date=None):
    '''Вывести дату в формате ДД.ММ.ГГ, эта дата должна быть первым днем месяца'''
    from datetime import datetime
    if any_date != None:
        n = datetime.strptime(any_date, '%d.%m.%y')
    else:
        n = datetime.today()
    return n.replace(day=1).strftime('%d.%m.%y')


def last_day_of_month(any_date=None):
    '''Вывести дату в формате ДД.ММ.ГГ, эта дата должна быть последним днем месяца'''
    from datetime import datetime
    if any_date != None:
        n = datetime.strptime(any_date, '%d.%m.%y')
    else:
        n = datetime.today()
    new_date = n.replace(day=(n.replace(month=n.month + 1) - n).days)
    return new_date.strftime('%d.%m.%y')


def one_month_plus(any_date=None):
    '''Прибавить к любой дате 1 месяц и вывести в формате ДД.ММ.ГГГГ'''
    from datetime import datetime
    if any_date != None:
        n = datetime.strptime(any_date, '%d.%m.%y')
    else:
        n = datetime.today()
    new_date = n.replace(month=(n.month + 1) % 12, year=n.year + (n.month + 1) // 12)
    return new_date.strftime('%d.%m.%y')


def change_month(dmy, n):
    from datetime import datetime
    '''Написать функцию change_month, которая к переданной дате прибавляет/вычитает переданное кол-во месяцев.
    Например:
       change_month(’12.12.2012’, 7) -> ’12.07.13’
       change_month(’01.11.2010’, -5) -> ’01.06.10’
    '''
    dmy = datetime.strptime(dmy, '%d.%m.%Y')
    new_date = dmy.replace(month=(dmy.month + n) % 12, year=dmy.year + (n + dmy.month) // 12)

    return new_date.strftime('%d.%m.%y')


count_lucky_tickets(2)
