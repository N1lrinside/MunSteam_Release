# Generated by Django 4.2.14 on 2024-08-24 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0003_remove_gameuser_user_gameuser_user_steam_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameachievement',
            name='user',
        ),
        migrations.AddField(
            model_name='gameachievement',
            name='user_steam_id',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
