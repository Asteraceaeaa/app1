from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserSignUpForm, UserLogInForm

def login(request):
    if request.method == 'POST':
        form = UserLogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('')
            else:
                return render(request, 'users/login.html', {'form': form, 'error_message': 'Invalid email or password'})
    else:
        form = UserLogInForm()
    return render(request, 'users/login.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = UserSignUpForm()

    return render(request, 'users/signup.html', {"form": form})

# def signup(request):
#     if request.method == 'POST':
#         form = UserSignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect('login')
#     else:
#         form = UserSignUpForm()
#     return render(request, 'users/signup.html', {'form': form})

def profile(request):
  return render(request, 'users/profile.html')

def user_logout(request):
    # Ваша дополнительная логика здесь
    logout(request)
    return redirect('home')

def profileEdit(request):
  return render(request, 'users/profile-edit.html')