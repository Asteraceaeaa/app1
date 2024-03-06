# Generated by Django 4.1.13 on 2024-03-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_options_alter_user_email_alter_user_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('учитель', 'Учитель'), ('ученик', 'Ученик')], default=None, max_length=20),
        ),
    ]