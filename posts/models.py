from typing import Any
from django.db import models
from users.models import CustomUser
from django.urls import reverse
from app import settings

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    for_whom = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
      return reverse('post_detail',
      args=[self.id])

    def __str__(self):
        return self.title + "\n" + self.body
    
class Comment(models.Model):
  post = models.ForeignKey(Post,
  on_delete=models.CASCADE,
  related_name='comments')
  name = models.CharField(max_length=80)
  user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='comments'
  )
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)
  
  class Meta:
    ordering = ['created']
    indexes = [
      models.Index(fields=['created']),
    ]

  def __str__(self):
    return f'Comment by {self.name} on {self.post}'