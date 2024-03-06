from django.db import models
from django.utils import timezone


class User(models.Model):

  #Types of User
  TYPES = (
      ('учитель', 'Учитель'),
      ('ученик', 'Ученик')
  )

  #Tables of data in db
  name = models.CharField(max_length = 20)
  middle_name = models.CharField(max_length = 20, default=None)
  last_name = models.CharField(max_length = 20)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length = 100)
  type = models.CharField(max_length = 20, choices=TYPES, default=None)
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

