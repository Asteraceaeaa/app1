from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserSignUpForm, UserLogInForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView

class login_user(LoginView):
    """
    Представление для регистрации нового пользователя.
    """
    template_name = 'users/signup.html'  # Путь к вашему шаблону для формы регистрации
    form_class = UserLogInForm
    success_url = '/profile'  # URL, на который перенаправить после успешной регистрации

    def form_valid(self, form):
        # Создаем пользователя с использованием данных из формы
        form.save()
        # Аутентифицируем пользователя после регистрации
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        # Вход пользователя
        login(self.request, user)
        return super().form_valid(form)


class RegistrationView(FormView):
    """
    Представление для регистрации нового пользователя.
    """
    template_name = 'users/signup.html'  # Путь к вашему шаблону для формы регистрации
    form_class = UserSignUpForm
    success_url = '/profile'  # URL, на который перенаправить после успешной регистрации

    def form_valid(self, form):
        # Создаем пользователя с использованием данных из формы
        form.save()
        # Аутентифицируем пользователя после регистрации
        name = form.cleaned_data.get('name')
        last_name = form.cleaned_data.get('last_name')
        middle_name = form.cleaned_data.get('middle_name') 
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)
        # Вход пользователя
        login(self.request, user)
        return super().form_valid(form)

def profile(request):
  return render(request, 'users/profile.html')

def user_logout(request):
    # Ваша дополнительная логика здесь
    logout(request)
    return redirect('home')

def profileEdit(request):
  return render(request, 'users/profile-edit.html')