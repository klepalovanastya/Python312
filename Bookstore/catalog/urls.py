from django.urls import path, re_path

import catalog.views as catalog


urlpatterns = [
    path('', catalog.mainpage),
    ]