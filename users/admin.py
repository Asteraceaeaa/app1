from django.contrib import admin
from users.models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'middle_name', 'last_name', 'email', 'password']
  search_fields  = ['id', 'name', 'last_name', 'email' ]