# Практичское задание the star
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
# Задание со звездочкой
#
# ЧАСТЬ 2
#
# Есть два списка разной длины. В первом содержатся ключи, а во втором значения.
# Напишите функцию, которая создаёт из этих ключей и значений словарь.
# Если ключу не хватило значения, в словаре должно быть значение None.
# Значения, которым не хватило ключей, нужно игнорировать.
#
# Напишите с использованием пакета Py.test и модуля hypothesis тесты,
# которые проверяли бы работу этой программы.
#
# Для проверки с помощью гипотез вам потребуется использовать стратегии (strategies).
# Примеры их использования смотри в официальной документации: https://hypothesis.readthedocs.io/

from Task_with_star_test import *

import pytest

@pytest.mark.parametrize("key ,value, expected", [
    ([1, 2, 3, 4, 5], ['h', 'e', 'l', 'l', 'o'], {1:'h', 2:'e', 3:'l', 4:'l', 6:'o'}),
    (['M', 'a', 'y'], ['J', 'u', 'n', 'e'], {'M':'J', 'a':'u', 'y':'n'})])

def test_dic(value,expected):
    assert(dic(key, value) == expected)


import hypothesis.strategies as st
from hypothesis import given


@given(st.lists(st.integers()), st.lists(st.integers()))
def test_hyp(x, y):
    assert len(dic(x, y)) == len(dict.fromkeys(x, None))

@given(st.lists(st.text()), st.lists(st.none()))
def test_hyp_hyp_none(x, y):
    assert dic(x, y) == dict.fromkeys(x, None)
