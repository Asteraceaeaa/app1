from django import forms
from .models import Post

class PostForm(forms.Form):
  title = forms.CharField(max_length=100)
  for_whom = forms.CharField(max_length=200, widget=forms.TextInput())
  description = forms.CharField(widget=forms.Textarea())

  class Meta:
    model = Post
    fields = ["title", "for_whom", "description"]