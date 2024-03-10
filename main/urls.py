from django.urls import path
from . import views
from users.views import sign_up, login, profile, user_logout

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up', sign_up, name='sign_up'),
    path('login', login, name='login'),
    path('profile', profile, name='profile'),
    path('logout', user_logout, name='logout'),
    # path('create-post', views.create_post, name='create_post'),
]