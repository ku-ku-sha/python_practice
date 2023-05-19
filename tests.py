import pytest
from data_for_tests import ExpectedResult as ExRes
from data_for_tests import InputData as IData
from tasks import *



def test_delete_a():
    for i in range(len(IData.delete_a)):
        print(f'test #{i}')
        assert delete_a(IData.delete_a[i]) == ExRes.delete_a[i]

#
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
# print_current_directory()
# create_folder()
# get_full_path()
# count_python()
# five_days_plus()
# current_date()
# ten_days_plus()
# first_day_of_month()
# last_day_of_month()
# one_month_plus()
# change_month()

