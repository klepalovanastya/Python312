from django.urls import path, re_path

import my_app.views as my_app

urlpatterns = [
    path('', my_app.mainpage),
    path('artwork/<slug:picture_name_slug>/', my_app.picture),
    path('product/<int:product_id>/', my_app.products),
    path('news/', my_app.page_news),
    path('books/', my_app.page_books),
    path('edit_books/<int:book_id>/', my_app.page_editBook),
    path('tasks/', my_app.page_tasks),
    path('edit_task/<int:task_id>/', my_app.page_editTask),
    path('delete_task/<int:task_id>/', my_app.page_deleteTask)

]