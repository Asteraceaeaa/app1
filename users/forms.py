from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class UserSignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтверждение пароля', 'type': 'password'}),
                                label='Подтверждение пароля')
    class Meta:
        model = CustomUser
        fields = ['name', 'last_name', 'middle_name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Отчество'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Придумайте пароль', 'type': 'password'}),
        }
        error_messages = {
            'password1': {
                'required': 'Поле "Подтверждение пароля" должно быть заполнено'
            }
        }

    def clean_password1(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password and password1 and password != password1:
            raise forms.ValidationError('Пароли не совпадают')
        return password1
class UserLogInForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email'
        self.fields['password'].label = 'Пароль'
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Email' })
        self.fields['password'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Пароль'})
        self.fields['password'].error_messages = {'required': 'Поле обязательно к заполнению'}
        self.fields['username'].error_messages = {'required': 'Поле обязательно к заполнению'}