from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    # def has_perm(self, perm, obj=None):
    #     return True

    # def has_module_perms(self, app_label):
    #     return True

    @property
    def is_staff(self):
        return self.is_admin


"""
class User(models.Model):



  #Tables of data in db

  name = models.CharField(max_length = 20)
  middle_name = models.CharField(max_length = 20, default=None)
  last_name = models.CharField(max_length = 20)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length = 100)
  reg_date = models.DateTimeField(default=timezone.now)
  
  #Meta-data for db
  class Meta:
          db_table = 'user'
          verbose_name = 'Пользователя'
          verbose_name_plural = 'Пользователи'


class AdditionalUserInfo(models.Model):
    GRADES = (
        
    )

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='users/', default='users/default-user-avatar.png')

"""