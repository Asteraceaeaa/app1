from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser):
   
    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True, default=None)
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


