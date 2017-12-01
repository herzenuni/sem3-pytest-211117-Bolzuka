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

if __name__ == '__main__':
    import unittest


    class TestFactorialMethods(unittest.TestCase):
        def test_normal_values(self):
            self.assertEqual(fact(5), 120)
            self.assertEqual(fact(0.5), None)
            self.assertEqual(fact(-5), None)

        def test_except_ValueError(self):
            with self.assertRaises(ValueError):
                fact(-1)

        def test_except_TypeError(self):
            with self.assertRaises(TypeError):
                fact([0, 1])
            with self.assertRaises(TypeError):
                fact('hello')
            with self.assertRaises(TypeError):
                fact(0.5)


unittest.main()
