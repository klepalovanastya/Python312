# Создать класс "Product" с атрибутами "name", "price", "quantity" и методами для чтения и записи данных всех трех атрибутов, 
# а также реализовать валидацию для атрибута "price":
# ●	должно быть положительным целым или дробным числом

#РЕШЕНИЕ

class Product:
    def __init__(self,name:str, price, quantity:int):
        self.__name = name
        self.__price = self.validate_price(price)
        self.__quantity = quantity

   
    @staticmethod 
    def validate_price(price):
        if type(price) != int and type(price) != float:
                return "price must be int or float" 
        if price < 0:
            return "price must be positive number"
        
        return price
    

    #ГЕТТЕРЫ
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @property
    def quantity(self):
        return self.__quantity
    
    #СЕТТЕРЫ
    @name.setter
    def name(self, name):
         self.__name = name

    @price.setter
    def price(self, price):
         self.__price = self.validate_price(price)

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity



new_product = Product(name='milk', price=78, quantity=120)

#ВЫЗОВ ГЕТТЕРОВ
print(new_product.name) 
print(new_product.price)
print(new_product.quantity)

#ВЫЗОВ СЕТТЕРОВ
new_product.name='water'
print(new_product.name) 

new_product.price=90
print(new_product.price)

new_product.quantity=100
print(new_product.quantity)



