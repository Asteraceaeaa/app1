from django.urls import path

from users.views import RegistrationView, login_user, profile, user_logout

urlpatterns = [

    path('sign-up', RegistrationView.as_view(), name='sign_up'),
    path('login', login_user.as_view(), name='login'),
    path('profile', profile, name='profile'),
    path('logout', user_logout, name='logout'),

]