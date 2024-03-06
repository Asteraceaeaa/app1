from django.shortcuts import render, redirect
from .forms import UderSignUpForm
# Create your views here.

def login(request):
  return render(request, 'users/login.html')


def signup(request):
  if request.method == 'POST':
    form = UderSignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login') # Перенаправление на страницу списка продуктов
  else:
    form = UderSignUpForm()
  return render(request, 'users/signup.html', {'form': form})

def profile(request):
  return render(request, 'users/profile.html')

def profileEdit(request):
  return render(request, 'users/profile-edit.html')