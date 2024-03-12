from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserSignUpForm, UserLogInForm

def login_user(request):
    form = UserLogInForm()
    message = ''
    if request.method == 'POST':
        form = UserLogInForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            print(user)
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
    return render(
        request, 'users/login.html', context={'form': form, 'message': message})


def sign_up(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                print(user)
                login(request, user)
                return redirect('/profile')
                # Перенаправление на страницу успешной регистрации или другую страницу
            except IntegrityError:
                # Обработка ошибки, когда email уже существует в базе данных
                # Можно добавить сообщение об ошибке в форму или передать его в контекст шаблона
                form.add_error('email', 'Данный email уже зарегистрирован')
    else:
        form = UserSignUpForm()
    return render(request, 'users/signup.html', {"form": form})

def profile(request):
  return render(request, 'users/profile.html')

def user_logout(request):
    # Ваша дополнительная логика здесь
    logout(request)
    return redirect('home')

def profileEdit(request):
  return render(request, 'users/profile-edit.html')