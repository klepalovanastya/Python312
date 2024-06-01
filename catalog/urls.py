from django.urls import path, re_path
from django.views.generic import TemplateView
import catalog.views as catalog


urlpatterns = [

    path('', catalog.MainPage.as_view(), name='main_url'),
    path("categories/<slug:slug>/", catalog.Category.as_view(), name="categories"),
    path('catalog/', catalog.Catalog.as_view(), name='catalog'),
    path('book/<int:book_id>/', catalog.AboutBook.as_view(), name='book'),
]
