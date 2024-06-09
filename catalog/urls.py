from django.urls import path, re_path
import catalog.views as catalog


urlpatterns = [

    path('', catalog.MainPage.as_view(), name='main_url'),
    path('about-us/', catalog.AboutUs.as_view(), name='about_us'),
    path('sections/', catalog.Sections.as_view(), name='sections'),
    path('sections/<slug:slug>/', catalog.Categories.as_view(), name='categories'),
    # path("categories/<slug:slug>/", catalog.Category.as_view(), name="categories"),
    # path('catalog/', catalog.Catalog.as_view(), name='catalog'),
    # path('book/<int:book_id>/', catalog.AboutBook.as_view(), name='book'),
]
