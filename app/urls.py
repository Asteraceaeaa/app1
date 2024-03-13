from django.contrib import admin
from django.urls import path, include
# from announcements import views as announcements_view
from main import urls as main_urls
from main.views import home 
from posts import urls as posts_urls

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('', include(main_urls)),
    path('posts/', include(posts_urls))
] 
