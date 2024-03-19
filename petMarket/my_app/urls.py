from django.urls import path, re_path

import my_app.views as my_app

urlpatterns = [
    path('my_app/', my_app.page1)
]