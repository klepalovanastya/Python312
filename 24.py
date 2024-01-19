# задача
# Определите класс Animal с атрибутами name (имя животного) и sound (звук, который издает животное) и методом make_sound(), который выводит сообщение о звуке, издаваемом животным.
# Создайте дочерний класс Bird, который наследует от класса Animal. Добавьте атрибут flight_altitude (высота полета) и метод fly(), который выводит сообщение о полете птицы.
# Пример использования:
# # Создание объектов
# lion = Animal("Lion", "Roar")
# parrot = Bird("Parrot", "Squawk", 100)

# # Вызов методов
# lion.make_sound()  # Выводит сообщение о звуке льва
# parrot.make_sound()  # Выводит сообщение о звуке попугая
# parrot.fly()  # Выводит сообщение о полете птицы


#РЕШЕНИЕ

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    
    def make_sound(self):
        print(f'Животное издает звук: {self.sound}')
    

class Bird(Animal): #дочерний класс
    def __init__(self,name, sound, flight_altitude:int):
        super().__init__(name, sound)
        self.flight_altitude = flight_altitude
    
    
    def fly(self):
        print(f'Полет птицы: {self.flight_altitude}')


#Создание объетов
pig = Animal("Pig", 'oink-oink')
duck = Bird("Duck","quack-quack",150)
#Вызов методов
pig.make_sound()
duck.make_sound()
duck.fly()
