from tasks import *

# Встроенные функции


# 1

print('\nВ строке удалить все буквы "а"  и подсчитать количество удаленных символов')

delete_a_input = ('', 'iouhlkjhjkg;ljlkji', 'AAAaaaаааААА', 'jkhlkhl;aaaljlA', '1231465465', 12345)
delete_a_exp_res = (('', 0), ('iouhlkjhjkg;ljlkji', 0), ('', 12), ('jkhlkhl;ljl', 4), ('1231465465', 0), -1)

print('input:' + ' ' * 30 + 'result:' + ' ' * 30 + 'expected result:')
for i in range(len(delete_a_input)):
    print(str(delete_a_input[i]).ljust(35), str(delete_a(delete_a_input[i])).ljust(35), delete_a_exp_res[i])

# 2


print('\n\n\nПроверить, что номера телефонов состоят только из цифр')

ph_input = ('8-999-777-1111', '+7 999 333 2222', '+7 999-555-11-11', '', '+565868', 'dfjgh', '8-999-777-1111!')
ph_exp_res = (True, True, True, False, False, False, False)
print('\ninput:' + ' ' * 30 + 'result:' + ' ' * 30 + 'expected result:')
for i in range(len(ph_input)):
    print(str(ph_input[i]).ljust(35), str(phone_number(ph_input[i])).ljust(35), ph_exp_res[i])

# 3

print(
    '\n\n\nДана строка, содержащая полное имя файла. Выделите из этой строки имя файла без расширения. Полное имя файла указывается в формате ОС Windows')

gfn_input = [r'C:\Python', r'C:\Python\python.exe', r'C:/Python/python.exe', 'C:\Python\python']
gfn_exp_res = [-1, 'python.exe', 'python.exe', '-1']

print('\ninput:' + ' ' * 30 + 'result:' + ' ' * 30 + 'expected result:')
for i in range(len(gfn_input)):
    print(str(gfn_input[i]).ljust(35), str(get_file_name(gfn_input[i])).ljust(35), gfn_exp_res[i])

# 4


print(
    '\n\n\nПоменять местами самый большой и самый маленький элементы списка. Функция позволяет обрабатывать списки строк и списки чисел')

swap_input = [[1, 2, 3, 4], [], [-5, 4], [{}, 5, 6], ['sdg', 'awer', 'a', '8767hk'], ['sdfg', 'ewft', 1]]
swap_exp_res = [[4, 2, 3, 1], -1, [4, -5], -1, ['8767hk', 'awer', 'a', 'sdg'], -1]

print('\ninput:' + ' ' * 30 + 'result:' + ' ' * 30 + 'expected result:')
for i in range(len(swap_input)):
    print(str(swap_input[i]).ljust(35), str(swap_min_max(swap_input[i])).ljust(35), swap_exp_res[i])

# 5

print(
    '\n\n\nДан список словарей: [{“наименование”: str, “цена”: int}, ...]. Найти ТОП-2 самых дорогих товаров и вывести в том же формате.')
mep_input = [[{'наименование': 'Спички', 'цена': 1}, {'наименование': 'Лук', 'цена': 200},
              {'наименование': 'Колбаса', 'цена': 3}, {'наименование': 'Чеснок', 'цена': 2}],
             [{'наименование': 'Спички', 'цена': 200}, {'наименование': 'Лук', 'цена': 200},
              {'наименование': 'Колбаса', 'цена': 3}, {'наименование': 'Чеснок', 'цена': 2}],
             [{'наименование': 'Спички', 'цена': 1}, {'наименование': 'Лук', 'цена': 200},
              {'наименование': 'Колбаса', 'цена': 3}, {'наименование': 'Чеснок', 'цена': 3}],
             [{'наименование': 'Лук', 'цена': 1}, {'наименование': 'Спички', 'цена': 200}]]
mep_exp_res = [[{'наименование': 'Лук', 'цена': 200}, {'наименование': 'Колбаса', 'цена': 3}],
               [{'наименование': 'Спички', 'цена': 200}, {'наименование': 'Лук', 'цена': 200}],
               [{'наименование': 'Лук', 'цена': 200}, {'наименование': 'Колбаса', 'цена': 3}],
               [{'наименование': 'Спички', 'цена': 200}, {'наименование': 'Лук', 'цена': 1}]]

for i in range(len(mep_input)):
    print('-----', i, '-----')
    print('input:'.ljust(20), mep_input[i])
    print('result:'.ljust(20), most_expensive_product(mep_input[i]))
    print('expected result:'.ljust(20), mep_exp_res[i])

# 6, 7
print('Функция подсчитывает количество n-значных счастливых билетов (n - четное), функция обенрнута в декоратор func_time, который вычисляет время работы функции ')

print(f'\nВсего {count_lucky_tickets(50)} 50-значных счастливых билетов.')
print(f'\nВсего {count_lucky_tickets(100)} 100-значных счастливых билетов.')
print(f'\nВсего {count_lucky_tickets(200)} 200-значных счастливых билетов.')




# Модуль os


# 1

print('\n\n\nПолучить список файлов в папке')
get_file_list('C:\Windows')

# 2

print('\n\n\nПолучить текущую директорию')
print(f'Текущая директория: {os.getcwd()}')

# 3

print('\n\n\nСоздать папку')
create_folder(os.path.join(os.getcwd(), 'папка'))

# 4

print('\n\n\nСклеить путь из папки и файла')
print(os.path.join(os.getcwd(), 'tests.py'))

# 5

print(
    '\n\n\nПосчитать сколько в каталоге установки python: 1) папок 2)файлов с расширением ".py" 3) файлов с расширением ".exe" 4) всего файлов. Записать результаты в файл')
count_python()
print(os.path.join(os.getcwd(), "result.txt"))

# Модуль datetime


# 1

print('\n\n\nПолучить текущую дату +5 дней в формате ДД.ММ.ГГ')
print(five_days_plus())

# 2

print('\n\n\nПолучить текущую дату в формате ДД.ММ.ГГГГ')
print(current_date())

# 3

print('\n\n\nНа входе есть строка "03.05.13" надо к этой дате прибавить 10 дней и вывести в формате ДД.ММ.ГГГГ (-> 13.05.2013)')
print(ten_days_plus("03.05.13"))

# 4

print('\n\n\nВывести дату в формате ДД.ММ.ГГ, эта дата должна быть первым днем месяца')

fd_input = [None, '12.10.24']
fd_exp_res = ['Первый день текущего месяца', '01.10.24']

print('\ninput:' + ' ' * 12 + 'result:' + ' ' * 12 + 'expected result:')
for i in range(len(fd_input)):
    print(str(fd_input[i]).ljust(17), str(first_day_of_month(fd_input[i])).ljust(18), fd_exp_res[i])

# 5

print('\n\n\nВывести дату в формате ДД.ММ.ГГ, эта дата должна быть последним днем месяца')

ld_input = [None, '01.02.23', '01.02.24']
ld_exp_res = ['Последний день текущего месяца', '28.02.23', '29.02.24']

print('\ninput:' + ' ' * 12 + 'result:' + ' ' * 12 + 'expected result:')
for i in range(len(ld_input)):
    print(str(ld_input[i]).ljust(17), str(last_day_of_month(ld_input[i])).ljust(18), ld_exp_res[i])

# 6

print('\n\n\nПрибавить к любой дате 1 месяц и вывести в формате ДД.ММ.ГГГГ')

omp_input = [None, '20.12.23']
omp_exp_res = ['Текущая дата + 1 месяц', '20.01.24']

print('\ninput:' + ' ' * 12 + 'result:' + ' ' * 12 + 'expected result:')
for i in range(len(omp_input)):
    print(str(omp_input[i]).ljust(17), str(one_month_plus(omp_input[i])).ljust(18), omp_exp_res[i])

# 7

print('\n\n\nНаписать функцию change_month, которая к переданной дате прибавляет/вычитает переданное кол-во месяцев.')

cm_input = [('12.12.2012', 7), ('01.11.2010', -5)]
cm_exp_res = ['12.07.13', '01.06.10']

print('\ninput:' + ' ' * 20 + 'result:' + ' ' * 12 + 'expected result:')
for i in range(len(cm_input)):
    print(str(cm_input[i]).ljust(25), str(change_month(*cm_input[i])).ljust(18), cm_exp_res[i])
