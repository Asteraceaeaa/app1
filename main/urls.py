from django.urls import path

from users.views import sign_up, login_user, profile, user_logout

urlpatterns = [

    path('sign-up', sign_up, name='sign_up'),
    path('login', login_user.as_view(), name='login'),
    path('profile', profile, name='profile'),
    path('logout', user_logout, name='logout'),
    # path('create-post', views.create_post, name='create_post'),
]