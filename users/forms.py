from django import forms
from .models import CustomUser

class UserSignUpForm(forms.Form):
  
  name = forms.CharField(
      max_length=100,
      error_messages={'required': 'Поле "Имя" должно быть заполнено'},
      required=True,
      widget=forms.TextInput(attrs={'placeholder': 'Имя'})
  )
  last_name = forms.CharField(
      max_length=100,
      error_messages={'required': 'Поле "Фамилия" должно быть заполнено'},
      required=True,
      widget=forms.TextInput(attrs={'placeholder': 'Фамилия'})
  )
  middle_name = forms.CharField(max_length=100, 
                                required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Отчество'})
                                )
  email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Придумайте пароль', 'type': 'password'}),
                              required=True,
                              )
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтверждение пароля', 'type': 'password'}),
                                required=True
                                )
  class Meta: 
    model = CustomUser

  def clean(self):
      cleaned_data = super().clean()
      password = cleaned_data.get('password')
      password1 = cleaned_data.get('password1')
      # Проверка, что пароли совпадают
      if password != password1:
          raise forms.ValidationError('Пароли не совпадают')

  def save(self, commit=True):
        cleaned_data = self.cleaned_data

        # Создаем экземпляр модели CustomUser
        user = CustomUser(
            name=cleaned_data['name'],
            last_name=cleaned_data['last_name'],
            middle_name=cleaned_data.get('middle_name'),
            email=cleaned_data['email'],
            password = cleaned_data['password']
        )
        # user.set_password(cleaned_data['password'])

        if commit:
            user.save()
        return user
class UserLogInForm(forms.Form):

  email = forms.CharField(label='Почта', max_length=100)
  password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

  class Meta:
        model = CustomUser
        fields = ['email', 'password']