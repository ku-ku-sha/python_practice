# Встроенные функции python

def delete_a(n: str) -> tuple:
    '''В строке удалить все буквы "а"  и подсчитать количество удаленных символов'''
    len_n = len(n)
    n.replace('a', '')  # eng
    n.replace('A', '')
    n.replace('а', '')  # rus
    n.replace('А', '')
    return n, len_n - len(n)

n = input()
print()
# 2) Проверить, что номера телефонов состоят только из цифр. Они могут начинаться с «+», цифры могут быть разделены пробелами и дефисами «-»
# Например: 8-999-777-1111, +7 999 333 2222, +7 999-555-11-11
# 3) Дана строка, содержащая полное имя файла (например, C:\development\inside\test-project_management\inside\myfile.txt'). Выделите из этой строки имя файла без расширения
# 4) Поменять местами самый большой и самый маленький элементы списка
# 5) Дан список словарей:
# [{“наименование”: “Спички”, “цена”: 1},  {“наименование”: “Лук”, “цена”: 37},  … , {“наименование”: str, “цена”: int}]
# Найти ТОП-2 самых дорогих товаров и вывести в том же формате.
# 6) Напишите функцию, которая подсчитывает количество счастливых шестизначных билетов. Билеты начинаются с 000000 и заканчиваются 999999. Счастливым считается билет, если сумма первых трех значений, равна сумме вторых трёх (Например: 927864, 123006, 002110 и т.д.)
# 7) Напишите декоратор func_time, который подсчитывает и выводит сколько времени выполняется функция, обернутая в него.
# @func_time
# def some_func():
# some_code
# >>> Функция some_func выполнялась 0.0001 сек
