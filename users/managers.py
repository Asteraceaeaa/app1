from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, name, last_name, middle_name, email, password=None):
        if not email:
            raise ValueError('Email is required')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            last_name=last_name,
            middle_name=middle_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
            name='',
            last_name='',
            middle_name=''
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
