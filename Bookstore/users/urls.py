from django.urls import path, re_path

import users.views as users
urlpatterns = [

    path('login/', users.LoginPage.as_view(), name="login"),
    path('logout/', users.LogoutUser.as_view(), name="logout"),
]