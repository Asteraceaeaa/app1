from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class Post(admin.ModelAdmin):
  list_display = ['author', 'title', 'body', 'for_whom']
  search_fields  = ['author', 'title', 'body', 'for_whom']
  
