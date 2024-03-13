from typing import Any
from django.db import models
from users.models import CustomUser
from django.urls import reverse


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
    