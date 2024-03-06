from django import forms
from .models import User

class UderSignUpForm(forms.ModelForm):
  class Meta:
        model = User
        fields = ['name', 'last_name', 'middle_name', 'email', 'password', 'type']