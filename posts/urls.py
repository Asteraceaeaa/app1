from django.urls import path
from .views import create_post, PostDetailView, delete_post, create_comment

urlpatterns = [
    path('create-post', create_post, name='create_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('delete/<int:pk>/', delete_post, name='delete_post'),
    path('post/write-comment', create_comment, name='create_comment'),
]