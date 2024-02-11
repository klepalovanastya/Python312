# задача
# напиши тестовые сценарии для данной функции и протестируйте ее при помощи pytest

def is_even(number: int) -> bool:
    """
    Проверяет, является ли число четным.

    :param number: Проверяемое число
    :return: True, если число четное, иначе False
    """
    return number % 2 == 0


def test_is_even_base():
    expected_result = True
    actual_result = is_even(10)
    assert expected_result == actual_result

def test_is_even_zero():
    expected_result = True
    actual_result = is_even(0)
    assert expected_result == actual_result

def test_is_even_negative_num():
    expected_result = True
    actual_result = is_even(-10)
    assert expected_result == actual_result

def test_is_even_base_negative():
    expected_result = False
    actual_result = is_even(3)
    assert expected_result == actual_result

def test_is_even_float_num():
    expected_result = False
    actual_result = is_even(1.5)
    assert expected_result == actual_result


# задача
# напиши тестовые сценарии для данной функции и протестируйте ее при помощи pytest

def is_prime(number: int) -> bool:
    """
    Проверяет, является ли число простым.

    :param number: Проверяемое число
    :return: True, если число простое, иначе False
    """
    if number <= 1:
        # Числа меньше или равные 1 не являются простыми
        return False
    elif number == 2:
        # 2 - единственное четное простое число
        return True
    elif number % 2 == 0:
        # Все другие четные числа не являются простыми
        return False
    else:
        # Проверяем делители от 3 до квадратного корня из числа
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True
    
def test_is_prime_num2():
    expected_result = True
    actual_result = is_prime(2)
    assert expected_result == actual_result

def test_is_prime_base():
    expected_result = True
    actual_result = is_prime(7)
    assert expected_result == actual_result

def test_is_prime_num1():
    expected_result = False
    actual_result = is_prime(1)
    assert expected_result == actual_result

def test_is_prime_negative_num():
    expected_result = False
    actual_result = is_prime(-1)
    assert expected_result == actual_result

def test_is_prime_base_negative():
    expected_result = False
    actual_result = is_prime(4)
    assert expected_result == actual_result

def test_is_prime_zero():
    expected_result = False
    actual_result = is_prime(0)
    assert expected_result == actual_result

def test_is_prime_negative_valid_num():
    expected_result = False
    actual_result = is_prime(-7)
    assert expected_result == actual_result

def test_is_prime_float_num():
    expected_result = False
    actual_result = is_prime(2.5)
    assert expected_result == actual_result




