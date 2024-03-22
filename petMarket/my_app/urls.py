from django.urls import path, re_path

import my_app.views as my_app

urlpatterns = [
    path('', my_app.mainpage),
    # path('mona-liza/', my_app.pictire1),
    # path('rozhdenie-venery/', my_app.pictire2),
    # path('poslednij-den-pompei/', my_app.pictire3),
    path('<slug:picture_name_slug>/', my_app.picture),
]