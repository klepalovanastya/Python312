# задача
# Класс Книга должен содержать информацию о названии, авторе и жанре книги.

#Решение


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


my_new_book = Book(author='Лев Толстой', title='Анна Каренина', genre='роман')

print(f'My book: title - {my_new_book.title}, author - {my_new_book.author}, genre - {my_new_book.genre}.')

# задача
# Класс БанковскийАккаунт должен хранить информацию о владельце, балансе

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

my_bank_account = BankAccount(owner='Клепалова Анастасия Александровна', balance=1250)

print(f"My Bank Account: owner - {my_bank_account.owner}, balance - {my_bank_account.balance} руб.")

# задача
# Класс Авиабилет должен содержать данные о рейсе, дате, месте и стоимости. Методы должны позволять бронировать билеты, отменять бронь и просматривать доступные рейсы.

class AirTicket:
    def __init__(self, where_started, where_land, date, seat, cost):
        self.where_started = where_started
        self.where_land = where_land
        self.date = date
        self.seat = seat
        self.cost = cost

    def show(self):
        print(f"where_started:{self.where_started} where_land: {self.where_land} date: {self.date} seat: {self.seat} cost: {self.cost}")


    def booking(self):
        print(f"Вы забронировали билет: where_started: {self.where_started} where_land: {self.where_land} date: {self.date} seat: {self.seat} cost:{self.cost}")

    def cancellation_of_booking(self):
        print(f"Вы отменили бронь билета: where_started: {self.where_started} where_land: {self.where_land} date: {self.date} seat: {self.seat} cost: {self.cost}")

my_air_ticket = AirTicket(where_started='Ivanovo', where_land='Anapa', date='14.07.2023', seat='A7', cost=7600)

my_air_ticket.show()
my_air_ticket.booking()
my_air_ticket.cancellation_of_booking()