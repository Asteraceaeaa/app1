from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser):
    avatar = models.ImageField(upload_to='users/avatars/', null=True, blank=True, default='users/avatars/default-user-avatar.png')
    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    password  =models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class AdditionalUserInfo(models.Model):

  user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
  # image = models.ImageField(upload_to='users/', default='users/default-user-avatar.png')

