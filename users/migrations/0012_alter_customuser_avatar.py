# Generated by Django 4.1.13 on 2024-03-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default-user-avatar.png', null=True, upload_to='avatars/'),
        ),
    ]
