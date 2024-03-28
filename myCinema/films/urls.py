from django.urls import path, re_path

import films.views as films

urlpatterns = [
    path('', films.mainpage),
    path('<int:film_id>/', films.page_about_film)

]