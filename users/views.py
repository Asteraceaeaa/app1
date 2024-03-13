from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserSignUpForm, UserLogInForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView


class login_user(LoginView):
    """
    Представление для входа в систему с использованием пользовательской формы аутентификации.
    """

    authentication_form = UserLogInForm
    template_name = "users/login.html"  # Путь к вашему шаблону для формы входа
    success_url = "home"  # URL, на который перенаправить после успешного входа


class RegistrationView(FormView):
    """
    Представление для регистрации нового пользователя.
    """

    template_name = "users/signup.html"  # Путь к вашему шаблону для формы регистрации
    form_class = UserSignUpForm
    success_url = "home/"  # URL, на который перенаправить после успешной регистрации

    def form_valid(self, form):
        # Создаем пользователя с использованием данных из формы
        user = form.save(commit=False)
        password = form.cleaned_data["password"]
        user.set_password(password)
        user.save()
        # Аутентифицируем пользователя после регистрации
        email = form.cleaned_data["email"]
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def profile(request):
    print(request.user.avatar.url)
    return render(request, "users/profile.html")


def user_logout(request):
    # Ваша дополнительная логика здесь
    logout(request)
    return redirect("home")


def profileEdit(request):
    return render(request, "users/profile-edit.html")
