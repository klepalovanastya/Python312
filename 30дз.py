# задача
# напиши тестовые сценарии для данной функции и протестируйте ее 
def calculate_average(numbers: list[float]) -> float:
    """
    Вычисляет среднее значение списка чисел.

    :param numbers: Список чисел
    :return: Среднее значение
    """
    if not numbers:
        raise ValueError("Список чисел не должен быть пустым")

    return sum(numbers) / len(numbers)
#Валидные значения параметра: [1, 2, 3, 4, 5]
#Не валидные значения параметра: []

# ---- test case 1 ------#
# expected result: calculate_average([1, 2, 3, 4, 5]) -> 3.0
# actual result:  calculate_average([1, 2, 3, 4, 5]) -> 3.0
numbers = [1, 2, 3, 4, 5]
print(f"numbers = {numbers}, calculate_average(numbers) -> {calculate_average(numbers)}")

# --------- result - > test passed----------------#

# ---- test case 2 ------#
# expected result: calculate_average([0]) -> 5.23333333333
# actual result:  calculate_average([0]) -> 5.23333333333
numbers = [1.4, 6.3, 8.0]
print(f"numbers = {numbers}, calculate_average(numbers) -> {calculate_average(numbers)}")

# --------- result - > test passed----------------#

# ---- test case 3 ------#
# expected result: calculate_average([1]) -> 1.0
# actual result:  calculate_average([1]) -> 1.0
numbers = [1]
print(f"numbers = {numbers}, calculate_average(numbers) -> {calculate_average(numbers)}")

# ---- test case 4 ------#
# expected result: calculate_average([]) -> ValueError
# actual result:  calculate_average([]) -> ValueError
numbers = []
try:
    calculate_average(numbers)
except ValueError:
    print("get exeption ValueError")

# --------- result - > test passed----------------#


# задача
# напиши тестовые сценарии для данной функции и протестируйте ее 
def is_even(number: int) -> bool:
    """
    Проверяет, является ли число четным.

    :param number: Проверяемое число
    :return: True, если число четное, иначе False
    """
    return number % 2 == 0

#Валидные значения: 10, 0, -10
#НЕ валидные значения: 3, 1.5

# ---- test case 1 ------#
# expected result: is_even(10) -> True
# actual result:  is_even(10) -> True
number = 10
print(f"number = {number}, is_even(number) -> {is_even(number)}")

# --------- result - > test passed----------------#

# ---- test case 2 ------#
# expected result: is_even(0) -> True
# actual result:  is_even(0) -> True
number = 0
print(f"number = {number}, is_even(number) -> {is_even(number)}")

# --------- result - > test passed----------------#

# ---- test case 3 ------#
# expected result: is_even(-10) -> True
# actual result:  is_even(-10) -> True
number = -10
print(f"number = {number}, is_even(number) -> {is_even(number)}")

# --------- result - > test passed----------------#

# ---- test case 4 ------#
# expected result: is_even(3) -> False
# actual result:  is_even(3) -> False

number = 3
print(f"number = {number}, is_even(number) -> {is_even(number)}")

# --------- result - > test passed----------------#


# ---- test case 5 ------#
# expected result: is_even(1.5) -> False
# actual result:  is_even(1.5) -> False

number = 1.5
print(f"number = {number}, is_even(number) -> {is_even(number)}")

# --------- result - > test passed----------------#






# задача
# напиши тестовые сценарии для данной функции и протестируйте ее


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
    
#Валидные значения: 2, 7
#НЕ валидные значения: 1, -1, 4, 0, -7, 2.5
    

# ---- test case 1 ------#
# expected result: is_prime(2) -> True
# actual result:  is_prime(2) -> True
number = 2
print(f"number = {number}, is_prime(number) -> {is_prime(number)}")

# --------- result - > test passed----------------#

# ---- test case 2 ------#
# expected result: is_prime(7) -> True
# actual result:  is_prime(7) -> True
number = 7
print(f"number = {number}, is_prime(number) -> {is_prime(number)}")

# ---- test case 3 ------#
# expected result: is_prime(1) -> False
# actual result:  is_prime(1) -> False
number = 1
print(f"number = {number}, is_prime(number) -> {is_prime(number)}")

# --------- result - > test passed----------------#

# ---- test case 4 ------#
# expected result: is_prime(-1) -> False
# actual result:  is_prime(-1) -> False
number = -1
print(f"number = {number}, is_prime(number) -> {is_prime(number)}")

# --------- result - > test passed----------------#

# ---- test case 5 ------#
# expected result: is_prime(4) -> False
# actual result:  is_prime(4) -> False
number = 4
print(f"number = {number}, is_prime(number) -> {is_prime(number)}")

# --------- result - > test passed----------------#

# ---- test case 6 ------#
# expected result: is_prime(0) -> False
# actual result:  is_prime(0) -> False
number = 0
print(f"number = {number}, is_prime(number) -> {is_prime(number)}")

# --------- result - > test passed----------------#

# ---- test case 7 ------#
# expected result: is_prime(-7) -> False
# actual result:  is_prime(-7) -> False
number = -7
print(f"number = {number}, is_prime(number) -> {is_prime(number)}")

# --------- result - > test passed----------------#

# ---- test case 8 ------#
# expected result: is_prime(2.5) -> False
# actual result:  is_prime(2.5) -> True
number = 2.5
print(f"number = {number}, is_prime(number) -> {is_prime(number)}")

# --------- result - > test failed----------------#















