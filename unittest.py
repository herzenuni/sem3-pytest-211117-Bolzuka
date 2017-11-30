# Практичское задание factorial
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
# Тестирование unittest
#
# ЧАСТЬ 2
#
# Использование unittest
#
# Реализовать вычисление факториала так, чтобы вычисление происходило для случаев,
# когда пользователь ввел натуральное число от 0 до n (где, n — целое, натуральное
# число, помещающееся в переменную целого числа).
#
# Для всех других случаев функция должна поднимать исключение TypeError или ValueError.
#
# Протестируйте работу этой функции с помощью unittest.
# Учтите ситуации, для которых должно подниматься исключения и
# найдите в документации модуля unittest как эту ситуацию обработать.

from Factorial import *

import pytest

@pytest.mark.parametrize("value,expected", [
    (0, 1),
    (5, 120),
    (10, 3628800),
    (2,2)])
def test_fact(value,expected):
	assert(fact(value) == expected)

def test_error():
    try:
        fact(-100500)
    except (ValueError, TypeError) as e:
        pass

import math
import hypothesis.strategies as st
from hypothesis import given

@given(st.lists(st.integers()))
def test_hyp(x):    assert fact(x) == math.factorial(x)

