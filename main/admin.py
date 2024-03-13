from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth.models import Group
from django.db.models.signals import post_save

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        def add_to_default_group(sender, **kwargs):
            user = kwargs["instance"]
            if kwargs['created']:
                group, _ = Group.objects.get_or_create(name="Пользователи")
                group.user_set.add(user)

        post_save.connect(add_to_default_group, sender=settings.AUTH_USER_MODEL)

        # /media/users/avatars/default-user-avatar.png
        # /media/users/avatars/default-user-avatar.png