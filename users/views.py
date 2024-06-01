from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from users.forms import LoginUserForm, RegisterUserForm
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .forms import ProfileUserForm, ChangePasswordUserForm
# Create your views here.

class ProfileMain(TemplateView):
    template_name = 'profile.html'
    extra_context = {'title': 'Профиль'}





class LoginPage(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': "Авторизация", 'form': form_class}

    def get_success_url(self):
        return reverse_lazy('main_url')


class LogoutUser(LogoutView):
    next_page = reverse_lazy('main_url')



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('login')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()  # Используем модель пользователя
    form_class = ProfileUserForm  # Форма профиля пользователя
    template_name = 'profile_personalData.html'  # Шаблон для профиля пользователя
    extra_context = {'title': "Профиль пользователя"}
    # Метод для получения URL после успешного обновления профиля
    def get_success_url(self):
        return reverse_lazy('profile')

    # Метод для получения объекта текущего пользователя
    def get_object(self, queryset=None):
        return self.request.user



class ChangePasswordUser(PasswordChangeView):
    form_class = ChangePasswordUserForm
    template_name = 'password_change.html'
    extra_context = {'title': "Изменение пароля"}

    def get_success_url(self):
        return reverse_lazy('change_password_done')