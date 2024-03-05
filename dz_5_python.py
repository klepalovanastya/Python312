# Задание №2
# Создать таблицу "Продукты" с полями: Название, Цена, Количество.

import sqlite3 as sq

with sq.connect("products.db") as con:
     cur = con.cursor() # для исполнения запроса 

     cur.execute("""CREATE TABLE IF NOT EXISTS products (
     product_id INTEGER PRIMARY KEY AUTOINCREMENT,
     name TEXT NOT NULL,
     price INTEGER NOT NULL,
    amount INTEGER NOT NULL
    )""")
     
def add_product(cur, name, price, amount):
     cur.execute(f'INSERT INTO products (name, price, amount) VALUES ("{name}", {price}, {amount})')
    
name = input("Введите название продукта:")
price = int(input("Введите цену продукта:"))
amount = int(input("Введите количество продукта:"))   
with sq.connect("products.db") as con:
     cur = con.cursor()
     add_product(cur, name, price, amount)


# ЗАДАНИЕ № 8
# Создать таблицу "Фильмы" с полями: Название, Режиссер, Год выпуска, Жанр.
with sq.connect("movies.db") as con:
     cur = con.cursor() # для исполнения запроса 

     cur.execute("""CREATE TABLE IF NOT EXISTS movies (
     movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
     title TEXT,
     director TEXT,
    year_of_release INTEGER, 
    genre TEXT
    )""")
     
def add_movie(cur, title, director, year_of_release, genre):
     cur.execute(f'INSERT INTO movies (title, director, year_of_release, genre) VALUES ("{title}", "{director}", {year_of_release}, "{genre}")')
    
title = input("Введите название фильма:")
director = input("Введите режиссера фильма:")
year_of_release = int(input("Введите год выпуска фильма:")) 
genre = input("Введите жанр фильма:")

with sq.connect("movies.db") as con:
     cur = con.cursor()
     add_movie(cur, title, director, year_of_release, genre)