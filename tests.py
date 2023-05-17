import pytest
from data_for_tests import ExpectedResult as ExRes
from data_for_tests import InputData as IData
import tasks



def test_delete_a():
    for i in range(len(IData.delete_a)):
        print(f'\ntest #{i}')
        assert tasks.delete_a(IData.delete_a[i]) == ExRes.delete_a[i]

def test_phone_number():
    pass


def test_get_file_name():
    pass


