#Задача 1: Управление банковским счетом
#Реализуйте класс BankAccount, который представляет банковский счет.
# Класс должен содержать атрибуты balance (баланс) и методы deposit (положить деньги на счет) и withdraw (снять деньги со счета).
#Создайте собственный класс исключения InsufficientFundsError, который будет возбуждаться при попытке снятия суммы, превышающей текущий баланс.

class BankAccount:
    def __init__(self, balance: float):
        self.__balance = balance

    @staticmethod
    def is_money(money):
        if not ((type(money) in [float, int]) and money > 0):
            raise "Передаваемая сумма должна быть int или float"
        if money < 0:
            raise "Передаваемая сумма меньше 0"

    @property
    def balance(self):
        return self.__balance

    def deposit(self, money: float): #Положить деньги на счет
        self.is_money(money)
        self.__balance += money
        return self.__balance
    

    def withdraw(self, money: float): #Снять деньги со счета
        self.is_money(money)
        if money > self.__balance:
            raise InsufficientFundsError
        
        self.__balance -= money
        return self.__balance

class InsufficientFundsError(Exception): #Класс исключения
    def __str__(self):
        return f'сумма снятия не должна превышать текущий баланс'
    
bank_account_1 = BankAccount(25000)
print(bank_account_1.balance)
bank_account_1.deposit(1500)
print(bank_account_1.balance)
bank_account_1.withdraw(5000)
print(bank_account_1.balance)
# bank_account_1.withdraw(30000)
# Задача 2: Работа с геометрическими фигурами
# Реализуйте класс Rectangle, представляющий прямоугольник. В классе должны быть атрибуты width и height, а также методы calculate_area (вычисление площади) и calculate_perimeter (вычисление периметра). Создайте собственный класс исключения InvalidDimensionsError, который будет возбуждаться при создании прямоугольника с неположительной шириной или высотой.


class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise InvalidDimensionsError
        
        self.width = self.isValidValue(width)
        self.height = self.isValidValue(height)

    @staticmethod
    def isValidValue(value):
        if type(value) in [float, int]:
            return value
        raise "значение должно быть int или float"

    def calculate_area(self): #Вычисление площади
        area = self.width * self.height
        return area
    
    def calculate_perimeter(self): #Вычисление периметра
        perimeter = 2 * (self.width + self.height)
        return perimeter
    
class InvalidDimensionsError(Exception): #Класс исключения
    def __str__(self):
        return f'высота/ширина должна быть положительным числом'

rectangle_1 = Rectangle(15, 10)
# rectange_2 = Rectangle(-15, -10)
print(f"Площадь прямоугольника: {rectangle_1.calculate_area()}")
print(f"Периметр прямоугольника: {rectangle_1.calculate_perimeter()}")