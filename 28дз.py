# Задача 
# создать систему для управления библиотекой. Вам нужно реализовать следующие классы:
# 	Book (Книга):
# ●	Свойства: название, автор, год издания, жанр, количество экземпляров.
# ●	Методы: вывод информации о книге, уменьшение/увеличение количества экземпляров.
# 	Library (Библиотека):
# ●	Свойства: список книг, список пользователей.
# ●	Методы: добавление/удаление книг, регистрация/удаление пользователя, выдача/возврат книги пользователю, вывод списка доступных книг.
# 	User (Пользователь):
# ●	Свойства: имя, ID, список взятых книг.
# ●	Методы: вывод информации о пользователе, взятие/возврат книги.
# 	Transaction (Транзакция):
# ●	Свойства: дата, тип (выдача/возврат), книга, пользователь.
# ●	Методы: запись транзакции, вывод информации о транзакции.
# Требования:
# ●	Каждый класс должен иметь конструктор для инициализации объектов.
# ●	Методы классов должны быть реализованы так, чтобы обеспечивать безопасность данных и взаимодействие между объектами.
# ●	Классы должны взаимодействовать друг с другом в рамках системы управления библиотекой.


class Book:
    def __init__(self, title: str, author: str, year_of_publication: int, genre: str, count: int):
        self.__title = title
        self.__author = author
        self.__year_of_publication = year_of_publication
        self.__genre = genre
        self.__count = count

        
    @staticmethod
    def isValudeCount(count):
        if type(count) == int:
            return True
        return False
    @property
    def title(self):
        return self.__title
    @property #геттер
    def count(self):
        return self.__count

    def display_info(self): #Метод вывода информации о книге
        print(f"Название: {self.__title}, Автор: {self.__author}, Год издания: {self.__year_of_publication}, Жанр: {self.__genre}, Количество экземпляров: {self.__count}")

    def decrease_count(self, count_of_books): #Метод уменьшения количества экземпляров
        if self.count != 0: 
            if self.isValudeCount(count_of_books):
                if self.__count >= count_of_books:
                    self.__count -= count_of_books
                else:
                    print("В библиотеке в данный момент нет такого количества экземпляров книги")
            else:
                print('count must be integer')
        else:
            print("Данной книги нет в наличии")

    def increase_count(self, count_of_books): #Метод увеличения количества экземпляров
                if self.isValudeCount(count_of_books):
                    self.__count += count_of_books
                else:
                    print('count must be integer')

    def checking_count(self):
        if self.__count == 0:
            return False
        return True

class User:
    def __init__(self, name: str, ID: int):
        self.__name = name
        self.__ID = self.isValidID(ID)
        self.__list_of_books_taken = []

    @property
    def list_of_books_taken(self):
        return self.__list_of_books_taken
    @property
    def name(self):
        return self.__name
    
    @staticmethod
    def isValidID(ID):
        if type(ID) != int:
            print('ID must be an integer')
        
        if len(str(ID)) != 6:
            print("len of ID must be 6")
        
        return ID
                
    def taking_book(self, name): #ВЫДАЧА КНИГИ
        self.__list_of_books_taken.append(name) 

    def refund(self, name): #ВОЗВРАТ КНИГИ
        self.__list_of_books_taken.remove(name)
        
    def display_info_about_user(self):
        print(f"Имя: {self.__name}, ID: {self.__ID} Cписок взятых книг:{self.__list_of_books_taken}")

class Library:
    def __init__(self):
        self.__list_of_books = []
        self.__list_of_users = []

    @property
    def list_of_books(self):
        return self.__list_of_books
    
    @property
    def list_of_users(self):
        return self.__list_of_users
    
    def add_book(self, book):
        return self.__list_of_books.append(book)
        
    
    def remove_book(self, name: str):
        flag = True
        for book in self.__list_of_books:
            if book.title == name:
                self.__list_of_books.remove(book)
                print(f"Из списка книг библиотеки была удалена книга '{name}'")
                flag = False
        if flag:
            print(f"Ошибка! В библиотике отсутсвует данная книга")

    def add_user(self, user):
            return self.__list_of_users.append(user)
    
    def remove_user(self, username):
        flag = True
        for user in self.__list_of_users:
            if user.name == username:
                self.__list_of_users.remove(user)
                print(f"Из списка пользоватей был удален пользователь с именем '{username}'")
                flag = False

        if flag:
            print(f"Ошибка! В списке пользователей отсутсвует пользователь с именем '{username}'")

    def does_user_exist(self, username): #проверка на существование пользователя в списке пользователей библиотеки
        for user in self.__list_of_users:
            if user.name == username:
                return True
        return False
    
    def does_book_exist(self, name): #проверка на существование книги в списке книг библиотеки
        for book in self.__list_of_books:
            if book.title == name:
                return True
        return False

    def book_distribution(self, name_of_book, user_name): #ВЫДАЧА КНИГИ ПОЛЬЗОВАТЕЛЮ
        flag = True
        for book in self.__list_of_books:
            if book.title == name_of_book:
                if self.does_user_exist(user_name):
                    book.decrease_count(1)
                    for user in self.__list_of_users:
                        if user.name == user_name:
                            user.taking_book(name_of_book)
                    print(f"Пользователю '{user_name}' выдана книга '{name_of_book}'")
                    flag = False
                    

        if flag:
            print("Неправильно введено название книги")

    def return_of_books(self, name_of_book, user_name): #ВОЗВРАТ КНИГИ ПОЛЬЗОВАТЕЛЕМ
        flag = True
        for book in self.__list_of_books:
            if book.title == name_of_book:
                if self.does_user_exist(user_name):
                    book.increase_count(1)
                    for user in self.__list_of_users:
                        if user.name == user_name:
                            user.refund(name_of_book)

                    print(f"Пользователь '{user_name}' вернул книгу '{name_of_book}'")
                    flag = False

        if flag:
            print("Неправильно введено название книги")

    def available_books(self): #ДОСТУПНЫЕ КНИГИ(те, у которых количестов экземпляров больше 0)
        print("Доступные книги")
        for book in self.__list_of_books:
            if book.checking_count():
                book.display_info()
    

class Transaction:
    def __init__(self, data: str, type: str, name_of_book: str, username: str):
        self.__data = data
        self.__type = self.isValidtype(type)
        self.__name_of_book = name_of_book
        self.__username = username
    
    @staticmethod
    def isValidtype(type):
        if type in ['выдача', 'возврат']:
            return type
        else:
            print("Ошибка! Существующие типы: 'выдача' и 'возврат'")


    def display_info_about_translation(self):
        print(f"Дата: {self.__data}, Тип: {self.__type}, Название книги: {self.__name_of_book}, Пользователь: {self.__username}")

    def make_a_record(self):
        with open('transactions.txt', "a+", encoding='utf-8') as f:
            f.write(f"Дата: {self.__data}, Тип: {self.__type}, Название книги: {self.__name_of_book}, Пользователь: {self.__username}\n")
            print("Транзакция успешно записана")



#Создание экземпляров класса КНИГА
        
book_1 = Book('Анна Каренина', 'Лев Толстой', 2001, 'роман', 3 )
book_2 = Book('Гарри Поттер', 'Джоан Роулинг', 2019, 'фэнтези', 2)
book_3 = Book('Убийство в Восточном экспрессе', 'Агата Кристи', 'детектив', 2011, 4)
book_4 = Book('Сияние', 'Стивен Кинг', 'ужасы', 2021, 1 )

#Вызов методов
print("Информация о книгах:")
book_1.display_info()
book_2.display_info()
book_3.display_info()
book_4.display_info()

print("Уменьшение и увеличение экземпляров книг")

book_1.decrease_count(1)
book_1.display_info()

book_2.decrease_count(4)
book_2.display_info()

book_3.increase_count(2)
book_3.display_info()


book_4.increase_count('1')
book_4.display_info()


#Создание экземпляра класса БИБЛИОТЕКА
library = Library()

#Добавление книг в библиотеку
library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)
library.add_book(book_4)

#Удаление книги из списка
library.remove_book('Анна Каренина')
library.remove_book('Капитанская дочка')

#Вывод доступных книг
book_4.decrease_count(1)
library.available_books()

#Создание экземпляров класса Пользователь

user_1 = User('Мария', 123456)
user_2 = User('Михаил', 234567)
user_3 = User('Анна', 777777)
user_4 = User('Илья', 454545)


user_1.display_info_about_user()
user_2.display_info_about_user()
user_3.display_info_about_user()
user_4.display_info_about_user()

#Добавление пользователей в список пользователей библиотеки

library.add_user(user_1)
library.add_user(user_2)
library.add_user(user_3)
library.add_user(user_4)

#Удаление пользователя
library.remove_user('Мария')
library.remove_user('Полина')

#Выдача книги пользователю
library.book_distribution('Гарри Поттер', 'Михаил')
user_2.display_info_about_user()

#Возврат книги пользователем
library.return_of_books('Гарри Поттер', 'Михаил')
user_2.display_info_about_user()


#Создание экземпляров класса Транзакция

transaction_1 = Transaction('25.01.24','выдача', 'Убийство в Восточном экспрессе', 'Анна')
transaction_2 = Transaction('01.02.24','возврат', 'Убийство в Восточном экспрессе', 'Анна')

transaction_1.display_info_about_translation()
transaction_2.display_info_about_translation()

transaction_1.make_a_record()
transaction_2.make_a_record()

