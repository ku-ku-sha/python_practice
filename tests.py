import pytest
from data_for_tests import ExpectedResult as ExRes
from data_for_tests import InputData as IData
from tasks import BuildInFunctions


def test_delete_a():
    for i in range(len(IData.delete_a)):
        print(f'test #{i}')
        assert BuildInFunctions.delete_a(IData.delete_a[i]) == ExRes.delete_a[i]


