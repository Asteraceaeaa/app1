from django import forms
from .models import CustomUser

class UserSignUpForm(forms.Form):
  
  name = forms.CharField(
      max_length=100,
      error_messages={'required': 'Поле "Имя" должно быть заполнено'}
  )
  last_name = forms.CharField(
      max_length=100,
      error_messages={'required': 'Поле "Фамилия" должно быть заполнено'}
  )
  middle_name = forms.CharField(max_length=100)
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput())

  class Meta:
    model = CustomUser

  def clean(self):
      cleaned_data = super().clean()
      password = cleaned_data.get('password')

      # Проверка, что пароль не пустой
      if not password:
            raise forms.ValidationError('Пароль не может быть пустым')

  def save(self, commit=True):
        cleaned_data = self.cleaned_data

        # Создаем экземпляр модели CustomUser
        user = CustomUser(
            name=cleaned_data['name'],
            last_name=cleaned_data['last_name'],
            middle_name=cleaned_data.get('middle_name'),
            email=cleaned_data['email']
        )
        user.set_password(cleaned_data['password'])

        if commit:
            user.save()
        return user
class UserLogInForm(forms.Form):

  email = forms.CharField(label='Почта', max_length=100)
  password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

  class Meta:
        model = CustomUser
        fields = ['email', 'password']