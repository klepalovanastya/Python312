# Задача 
# Создайте класс Book, представляющий книгу. Реализуйте магические методы сравнения (==, !=, <, >, <=, >=) на основе сравнения года издания книги. Книги сравниваются по году издания.

#РЕШЕНИЕ

class Book(object):
    def __init__(self, title: str, author: str, year_of_publication: int):
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication

     # перегрузка оператора сравнения (==)
    def __eq__(self, other):
         return self.year_of_publication == other.year_of_publication

    # перегрузка оператора сравнения (!=)
    def __ne__(self, other):
        return self.year_of_publication != other.year_of_publication

    # перегрузка оператора сравнения (<)
    def __lt__(self, other):
        return self.year_of_publication < other.year_of_publication

    # перегрузка оператора сравнения (>)
    def __gt__(self, other):
        return self.year_of_publication > other.year_of_publication

    # перегрузка оператора сравнения (<=)
    def __le__(self, other):
        return self.year_of_publication <= other.year_of_publication

    # перегрузка оператора сравнения (>=)
    def __ge__(self, other):
        return self.year_of_publication >= other.year_of_publication

book_1 = Book('Сrime and Punishment', 'Dostoevsky', 2014)
book_2 = Book('War and Peace', 'Tolstoy', 2014)
book_3 = Book('The Hero of Our Time', 'Lermontov', 2019)

print(book_1==book_2)
print(book_1!=book_3)
print(book_1>book_3)
print(book_2<book_3)
print(book_2>=book_1)
print(book_3<=book_1)

# Задача 
# Создайте класс Complex, представляющий комплексное число. Реализуйте магические методы сложения, вычитания и умножения комплексных чисел.

class Complex:
    def __init__(self, a:int, b:int):
        self.a = a #действительная часть
        self.b = b #мнимая часть
    #магический метод сложения
    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return Complex(new_a, new_b)

    # магический метод вычитания
    def __sub__(self, other):
        new_a = self.a - other.a
        new_b = self.b - other.b
        return Complex(new_a, new_b)

    # магический метод умножения
    def __mul__(self, other):
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Complex(new_a, new_b)

    def __str__(self):
        return f"Complex({self.a}+({self.b}j))"

number_1 = Complex(1,5)
number_2 = Complex(2,4)

print(number_1+number_2)
print(number_1-number_2)
print(number_1*number_2)


