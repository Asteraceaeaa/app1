from django.contrib import admin
from .models import Post, Comment
# Register your models here.
@admin.register(Post)
class Post(admin.ModelAdmin):
  list_display = ['author', 'title', 'body', 'for_whom']
  search_fields  = ['author', 'title', 'body', 'for_whom']
  


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('post__title', 'user__username', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)