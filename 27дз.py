# Разработайте систему классов для управления рестораном. Создайте базовый класс "Блюдо" с общими характеристиками (например, название, цена). Затем создайте подклассы для различных типов блюд, таких как "Завтрак" и "Ужин", добавляя специфичные свойства и методы. Реализуйте метод для расчета общей стоимости заказа.


#Решение
from abc import ABC, abstractmethod
class Dish(ABC): #абстрактный класс Блюдо
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        
    @abstractmethod
    def display_info():
        pass


class Pizza(Dish):
    def __init__(self, name: str, price: float, centimeters:int, dough:str, cooking_time: int):
        super().__init__(name, price)
        self.centimeters = centimeters
        self.dough = dough
        self.cooking_time = cooking_time
        
    def display_info(self):
        print(f"Название: {self.name}, Тип теста: {self.dough}, См: {self.centimeters}, Время приготовления: {self.cooking_time} минут, Цена: {self.price}")

    def take_it_with_you(self, buyer):
        print(f"Пицца '{self.name}' будет запакована в коробку. Выдать покупателю с именем {buyer}")

class Soup(Dish):
    def __init__(self, name: str, price: float, cooking_time: int, grams: int):
        super().__init__(name, price)
        self.cooking_time = cooking_time
        self.grams = grams
    
    def display_info(self):
        print(f"Название: {self.name}, Время приготовления: {self.cooking_time} минут, Цена: {self.price}")


class Dessert(Dish):
    def __init__(self, name: str, price: float, type: str, grams: int):
        super().__init__(name, price)
        self.type = type
        self.grams = grams

    def display_info(self):
        print(f"Название: {self.name}, Грамм: {self.grams}, Тип(холодный, горячий): {self.type}, Цена: {self.price}")    

class Salad(Dish):
    def __init__(self, name:str, price: float, cooking_time: int, grams: int, type: str):
        super().__init__(name, price)
        self.cooking_time = cooking_time
        self.grams = grams
        self.type = type

    def display_info(self):
        print(f"Название: {self.name}, Тип(мясной, рыбный, фруктовый, овощной): {self.type}, Грамм: {self.grams}, Время приготовления: {self.cooking_time} минут, Цена: {self.price}")


class Garnish(Dish):
    def __init__(self, name: str, price: float, grams: int):
        super().__init__(name, price)
        self.grams = grams

    def display_info(self):
        print(f"Название: {self.name}, Грамм: {self.grams}, Цена: {self.price}")

    def add_sauce(self, name_of_sauce):
        if name_of_sauce in ['кетчуп', 'сырный соус', 'чесночный соус']:
            print(f"Добавть к горниру соус'{name_of_sauce}'")
        else:
            print("Данный соус отсутсвует в меню")


class Order:
    def __init__(self, buyer):
        self.dishes = []
        self.buyer = buyer

    def add_dish_to_order(self, dish):
        self.dishes.append(dish)

    def display_order(self):
        for dish in self.dishes:
            dish.display_info()

    def remove_dish_from_order(self, name:str):
        flag = True
        for dish in self.dishes:
            if dish.name == name:
                self.dishes.remove(dish)
                print(f"Из заказа Было удалено блюдо с названием '{name}'")
                flag = False
        if flag:
            print(f"Ошибка! Данное блюдо '{name}' отсутвует в заказе")
    
    def cost_of_order(self):
        cost = 0
        for dish in self.dishes:
            cost += dish.price
        return cost

#Создание экземпляров
dish_1 = Pizza('Ветчина-грибы', 670, 33, 'классическое', 30)
dish_2 = Soup('Борщ', 250, 75, 260)
dish_3 = Dessert('"Торт "Наполеон"', 235, 'холодный', 170)
dish_4 = Salad('Греческий', 250, 15, 240, 'овощной')
dish_5 =  Garnish('Картофель фри', 200, 200)

#Вызов методов
dish_1.display_info()
dish_2.display_info()
dish_3.display_info()
dish_4.display_info()
dish_5.display_info()

dish_1.take_it_with_you("Иван")
dish_5.add_sauce('кетчуп')

new_order = Order('Мария')

#Добавление блюд в новый заказ
new_order.add_dish_to_order(dish_1)
new_order.add_dish_to_order(dish_2)
new_order.add_dish_to_order(dish_3)
new_order.add_dish_to_order(dish_4)
new_order.add_dish_to_order(dish_5)


#Итоговый список блюд заказа полсе их добавления
print("Блюда в заказе:")
new_order.display_order()

#Удаление блюда из заказа
new_order.remove_dish_from_order("Греческий")
print("Список блюд заказа после удаления:")
new_order.display_order()

#Расчет общей стоимости заказа
print(f"Общая стоимость заказа: {new_order.cost_of_order()}")



