from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

# from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from posts.forms import PostForm
from posts.models import Post


# Create your views here.
@login_required(login_url="login")
def home(request):
    posts = Post.objects.all()
    for post in posts:
        print(post)
    if request.method == "POST":
        post.delete()

    return render(request, "main/home.html", {"posts": posts})
