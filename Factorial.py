# Практичское задание factorial
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
# Тестирование unittest
#
# ЧАСТЬ 1
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

def fact(n):
    res = None
    try:
        if type(n) is not int:
            raise TypeError('Input argument is not integer value')
        n = int(n)
    except (ValueError, TypeError) as e:
        print('Argument "{}" is not a number. {}'.format(n, e))
    else:
        if n < 0:
            print('Argument "{}" less than 0'.format(n)) # return None
        elif n == 0:
            return 1
        else:
            res = n * fact( n -1)
            return res

print("1. {}".format(fact(10.0)))
#print("2. {}".format(fact(5)))
#print("3. {}".format(fact(3)))
#print("4. {}".format(fact(0)))
print("5. {}".format(fact(-1)))
#print("6. {}".format(fact('o')))
#print('')

assert fact(10) == 3628800, ("Факториал при n = 10 должен быть равен 3628800")
assert fact(5) == 120, "Факториал при n = 5 должен быть равен 120"
assert fact(0) == 1, "При n = 0, значение факториала равно 1"
assert fact(0.5) == None, ("При n = 0.5, значение факториала вычисляться не должно. Вернет None")
assert fact(2.7) == None, ("При n = 2.7, значение факториала вычисляться не должно. Вернет None")
assert fact(True) == None, ("При n = True, значение факториала вычисляться не должно. Вернет None")
assert fact(False) == None, ("При n = False, значение факториала вычисляться не должно. Вернет None")
assert fact(-1) == None, ("При отрицательных значениях Ф. не вычисляется, возвращаем None")
assert fact(-10) == None, ("При отрицательных значениях Ф. не вычисляется, возвращаем None")
assert fact('a') == None, ("Если n не число, то Ф. не вычисляется, возвращаем None")
assert fact([1,2,3]) == None, ("Если n не число, то Ф. не вычисляется, возвращаем None")
assert fact({1,2,3}) == None, ("Если n не число, то Ф. не вычисляется, возвращаем None")
