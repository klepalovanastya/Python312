from django.urls import path, re_path

import catalog.views as catalog


urlpatterns = [

    path('', catalog.mainpage, name="main_url"),
    path('section/slug:section_name/', catalog.sections, name="section"),
    path("books/<slug:cat_name>/", catalog.show_books, name="books"),
    path("book/<int:book_id>/", catalog.show_book, name="book"),
]
