from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from django.contrib.auth.models import Permission
        add_post_perm = Permission.objects.get_or_create(codename='add_post', name='Can add post')