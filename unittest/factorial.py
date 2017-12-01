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
    if type(n) is not int:
        raise TypeError
    try:
        n = int(n)
    except (ValueError, TypeError) as e:
        print('Argument "{}" is not a number '.format(n))
    else:
        if n < 0:
            raise ValueError
        elif n == 0:
            return 1
        else:
            res = n * fact(n - 1)
            return res

#print("3. {}".format(fact(3)))
#print("4. {}".format(fact(0)))
#print("5. {}".format(fact(-1)))
#print("6. {}".format(fact('o')))
#print('')


#assert fact(5) == 120, "Факториал при n = 5 должен быть равен 120"
#assert fact(0.5) == None, ("При n = 0.5, значение факториала вычисляться не должно. Вернет None")
#assert fact(-5) == None, ("При отрицательных значениях Ф. не вычисляется, возвращаем None")
