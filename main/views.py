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
    post_id = request.POST.get("post-id")
    user_id = request.POST.get("user-id")

    if post_id:
      post = Post.objects.filter(id=post_id).first()
      if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
        post.delete()
    elif user_id:
      user = User.objects.filter(id=user_id).first()
      if user and request.user.is_staff:
        try:
          group = Group.objects.get(name='default')
          group.user_set.remove(user)
        except:
          pass

      try:
        group = Group.objects.get(name='mod')
        group.user_set.remove(user)
      except:
        pass

  return render(request, 'main/home.html', {"posts": posts})

