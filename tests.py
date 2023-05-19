import pytest
from data_for_tests import ExpectedResult as ExRes
from data_for_tests import InputData as IData
from tasks import *

# Доступные функции
#
# delete_a()
# phone_number()
# get_file_name()
# swap_min_max()
# most_expensive_product()
# count_lucky_tickets()
# func_time()
# get_file_list()
# create_folder()
# count_python()
# five_days_plus()
# current_date()
# ten_days_plus()
# first_day_of_month()
# last_day_of_month()
# one_month_plus()
# change_month()


# Встроенные функции

#####
# 1
#####
print('\nВ строке удалить все буквы "а"  и подсчитать количество удаленных символов')

delete_a_input = ('', 'iouhlkjhjkg;ljlkji', 'AAAaaaаааААА', 'jkhlkhl;aaaljlA', '1231465465', 12345)
delete_a_exp_res = (('', 0), ('iouhlkjhjkg;ljlkji', 0), ('', 12), ('jkhlkhl;ljl', 4), ('1231465465', 0), -1)

print('input:' + ' ' * 30 + 'result:' + ' ' * 30 + 'expected result')
for i in range(len(delete_a_input)):
    print(str(delete_a_input[i]).ljust(35), str(delete_a(delete_a_input[i])).ljust(35), delete_a_exp_res[i])

#####
# 2
#####

print('\n\n\nПроверить, что номера телефонов состоят только из цифр')

ph_input = ('8-999-777-1111', '+7 999 333 2222', '+7 999-555-11-11', '', '+565868', 'dfjgh', '8-999-777-1111!')
ph_exp_res = (True, True, True, False, False, False, False)
print('\ninput:' + ' ' * 30 + 'result:' + ' ' * 30 + 'expected result')
for i in range(len(ph_input)):
    print(str(ph_input[i]).ljust(35), str(phone_number(ph_input[i])).ljust(35), ph_exp_res[i])

#####
# 3
#####
print(
    '\n\n\nДана строка, содержащая полное имя файла. Выделите из этой строки имя файла без расширения. Полное имя файла указывается в формате ОС Windows')

gfn_input = [r'C:\inside\myfile.txt', r'C:\myfile', '', 'sdfg.txt']
gfn_exp_res = ['myfile', '', '', '']

print('\ninput:' + ' ' * 30 + 'result:' + ' ' * 30 + 'expected result')
for i in range(len(gfn_input)):
    print(str(gfn_input[i]).ljust(35), str(get_file_name(gfn_input[i])).ljust(35), gfn_exp_res[i])

#####
# 4
#####

print(
    '\n\n\nПоменять местами самый большой и самый маленький элементы списка. Функция позволяет обрабатывать списки строк и списки чисел')

swap_input = [[1, 2, 3, 4], [], [-5, 4], [{}, 5, 6], ['sdg', 'awer', 'a', '8767hk'], ['sdfg', 'ewft', 1]]
swap_exp_res = [[4, 2, 3, 1], -1, [4, -5], -1, ['8767hk', 'awer', 'a', 'sdg'], -1]

print('\ninput:' + ' ' * 30 + 'result:' + ' ' * 30 + 'expected result')
for i in range(len(swap_input)):
    print(str(swap_input[i]).ljust(35), str(swap_min_max(swap_input[i])).ljust(35), swap_exp_res[i])

#####
# 5
#####
print(
    '\n\n\nДан список словарей: [{“наименование”: str, “цена”: int}, ...]. Найти ТОП-2 самых дорогих товаров и вывести в том же формате.')
mep_input = [[{'наименование': 'Спички', 'цена': 1}, {'наименование': 'Лук', 'цена': 200},
              {'наименование': 'Колбаса', 'цена': 3}, {'наименование': 'Чеснок', 'цена': 2}],
             [{'наименование': 'Чеснок', 'цена': 2}],
             [{'наименование': 'Спички', 'цена': 200}, {'наименование': 'Лук', 'цена': 200},
              {'наименование': 'Колбаса', 'цена': 3}, {'наименование': 'Чеснок', 'цена': 2}],
             [{'наименование': 'Спички', 'цена': 1}, {'наименование': 'Лук', 'цена': 200},
              {'наименование': 'Колбаса', 'цена': 3}, {'наименование': 'Чеснок', 'цена': 3}],
             [{'наименование': 'Лук', 'цена': 200}, {'наименование': 'Спички', 'цена': 1}]]
mep_exp_res = [[{'наименование': 'Лук', 'цена': 200}, {'наименование': 'Колбаса', 'цена': 3}],
               [{'наименование': 'Чеснок', 'цена': 2}],
               [{'наименование': 'Спички', 'цена': 200}, {'наименование': 'Лук', 'цена': 200}],
               [{'наименование': 'Лук', 'цена': 200}, {'наименование': 'Колбаса', 'цена': 3}],
               [{'наименование': 'Лук', 'цена': 200}, {'наименование': 'Спички', 'цена': 1}]]

for i in range(len(mep_input)):
    print('-----', i, '-----')
    print('input:'.ljust(20), mep_input[i])
    print('result:'.ljust(20), most_expensive_product(mep_input[i]))
    print('expected result:'.ljust(20), mep_exp_res[i])


#####
# 6
#####
print(f'\n\n\nВсего {count_lucky_tickets()} 6 значных счастливых билетов.')

#####
# 7
#####
print('\n\n\nНапишите декоратор func_time, который подсчитывает и выводит сколько времени выполняется функция, обернутая в него.')
print('Для проверки работы декоратора изменим функцию count_lucky_tickets так, чтобы она считала количество 12-значных счастливых билетов')

count_lucky_tickets_12()

###########
# Модуль os
###########

#####
# 1
#####
print('\n\n\nПолучить список файлов в папке')
get_file_list('C:\Windows')
#####
# 2
#####
print('\n\n\n Получить текущую директорию')
print(f'Текущая директория {os.getcwd()}')
#####
# 3
#####
print('\n\n\nСоздать папку')
create_folder(os.path.join(os.getcwd(), 'папка'))
#####
# 4
#####
print('\n\n\nСклеить путь из папки и файла')
print(os.path.join(os.getcwd(), 'tests.py'))
#####
# 5
#####
print('\n\n\nПосчитать сколько в каталоге установки python: 1) папок 2)файлов с расширением ".py" 3) файлов с расширением ".exe" 4) всего файлов. Записать результаты в файл')
count_python()
print(os.path.join(os.getcwd(), "result.txt"))
