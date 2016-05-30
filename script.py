# coding: utf-8


def fizz_buzz(number):
    """
    Функция принимает int.
    Возвращает Fizz если число делиться на 3,
    Возвращает Buzz если число делиться на 5.
    Возвращает FizzBuzz если число делиться на 3 и 5.
    """
    if number <= 0:
        return 'SmallInt'

    if type(number) is str:
        return 'StringError'

    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'

    elif number % 3 == 0:
        return 'Fizz'

    elif number % 5 == 0:
        return 'Buzz'

print "Hello world!"
