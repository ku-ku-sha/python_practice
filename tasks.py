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
    num = '0123456789+- '
    try:
        if len(n) == 0 or n.strip(
                num) != 0:  # проверка того, что ввод непустой и не содержит символов, кроме цифр, пробелов, символов "+" и "-" - блок удовлетворяет условию задания
            print('Invalid phone number')
            return False
        else:  # проверка соответствия номера формату (используются регулярные выражения)
            regex = r''

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
    '''Поменять местами самый большой и самый маленький элементы списка'''
    if isinstance(n, list):
        type_n = type(n[0])
        match str(type_n):
            case 'str':
                pass
            case 'int' | 'float':
                pass
            case _:
                print('List elements cannot be compared')
                return -1

    else:
        print('Invalid input type (List required)')
        return -1

# 4)
# 5) Дан список словарей:
# [{“наименование”: “Спички”, “цена”: 1},  {“наименование”: “Лук”, “цена”: 37},  … , {“наименование”: str, “цена”: int}]
# Найти ТОП-2 самых дорогих товаров и вывести в том же формате.
# 6) Напишите функцию, которая подсчитывает количество счастливых шестизначных билетов. Билеты начинаются с 000000 и заканчиваются 999999. Счастливым считается билет, если сумма первых трех значений, равна сумме вторых трёх (Например: 927864, 123006, 002110 и т.д.)
# 7) Напишите декоратор func_time, который подсчитывает и выводит сколько времени выполняется функция, обернутая в него.
# @func_time
# def some_func():
# some_code
# >>> Функция some_func выполнялась 0.0001 сек
