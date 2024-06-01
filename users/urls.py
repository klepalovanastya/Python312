from django.urls import path, re_path
from django.contrib.auth.views import PasswordChangeDoneView
import users.views as users
urlpatterns = [

    path('login/', users.LoginPage.as_view(), name="login"),
    path('logout/', users.LogoutUser.as_view(), name="logout"),
    path('register/', users.RegisterUser.as_view(), name="register"),
    path('profile/', users.ProfileMain.as_view(), name="profile"),
    path('profile/personal-information/', users.ProfileUser.as_view(), name="profile_persData"),
    path('password-change/', users.ChangePasswordUser.as_view(), name="change_password"),
    path('password-change-done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name="change_password_done"),
]