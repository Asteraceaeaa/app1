from typing import Any
from django.db import models
from users.models import CustomUser
from django.urls import reverse
from app import settings

class Post(models.Model):
    author = settings.AUTH_USER_MODEL
    for_whom = models.CharField(max_length=200)
    title = models.CharField(max_length=100, null=True, blank=True, default=None)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
      return reverse('post_detail',
      args=[self.id])

    def __str__(self):
        if self.title is not None:
            return self.title + "\n" + self.body
        else:
          return self.body
          
