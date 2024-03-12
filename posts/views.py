from django.shortcuts import render, redirect
from .forms import PostForm
# Create your views here.

def create_post(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user()
      post.save()
      return redirect("/home")
  else: 
    form = PostForm()
  return render(request, 'posts/new-post.html', {"form": form})