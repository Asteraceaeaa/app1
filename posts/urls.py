from django.urls import path
from .views import create_post, PostDetailView

urlpatterns = [
    path('create-post', create_post, name='create_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]