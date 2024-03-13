from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import DetailView
from .forms import PostForm
from .models import Post

@login_required(login_url="login")
# @permission_required("main.add_post", login_url="/login", raise_exception=True)
def create_post(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect("/home")
  else: 
    form = PostForm()
  return render(request, 'posts/new-post.html', {"form": form})

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post-detail.html'  # Замените на имя вашего шаблона
    context_object_name = 'post' 