from django import forms
from .models import Post
from .models import Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "for_whom", "body"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "body"
        ]  # Убрал user и post, так как их значения будут получены автоматически

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)  # Извлекаем пользователя из kwargs
        post = kwargs.pop("post", None)  # Извлекаем пост из kwargs
        super().__init__(*args, **kwargs)
        if user:
            self.fields["user"].initial = (
                user  # Устанавливаем пользователя в качестве начального значения
            )
        if post:
            self.fields["post"].initial = (
                post  # Устанавливаем пост в качестве начального значения
            )
