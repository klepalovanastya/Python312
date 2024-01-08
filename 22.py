# 	Класс SantaClaus
# ●	Атрибуты: имя, возраст, количество подарков.
# ●	Методы: give_gifts(), update_age().
# ●	НЕОБЯЗАТЕЛЬНО: Интерфейс для отправки подарков и обновления возраста.

#РЕШЕНИЕ
class SantaClause:
    def __init__(self, name:str, age:int, number_of_gifts:int):
        self.__name = name
        self.age = age
        self.number_of_gifts = number_of_gifts

    def give_gifts(self):
        print(f"Подарок отправлен: кому- {self.__name}, возраст- {self.age} в количестве {self.number_of_gifts} шт.")

    def update_age(self, new_age:int):
        self.age = new_age
        print(f"Был обновлен возраст {self.__name}: новый возраст - {self.age}")


first_child = SantaClause(name='Alice',age=12, number_of_gifts=2)
second_child = SantaClause(name='Mike', age=8, number_of_gifts=3)
third_child = SantaClause(name='Lily', age =3, number_of_gifts=1)

first_child.give_gifts()
second_child.update_age(9)


# реализовать класс
# 	Класс ChristmasTree
# ●	Атрибуты: высота, количество игрушек.
# ●	Методы: decorate_tree(new_decorations), grow_tree(new_height).
# ●	НЕОБЯЗАТЕЛЬНО: Интерфейс для украшения ёлки и изменения её высоты.

#РЕШЕНИЕ
class ChristmasTree:
    def __init__(self, height:float, number_of_decoration:int):
        self.height = height
        self.number_of_decoration = number_of_decoration

    def grow_tree(self, changing_the_length:float):
        self.height += changing_the_length
        print(f'Новая длина елки: {self.height}')

    def decorate_tree(self, new_decorations:int):
        self.number_of_decoration += new_decorations
        print(f"Елку украсили новыми игрушками в количестве: {new_decorations}. Всего украшений на елке: {self.number_of_decoration} шт.")


new_tree = ChristmasTree(height=1.55,number_of_decoration=3)

new_tree.grow_tree(0.2)

new_tree.decorate_tree(7)
