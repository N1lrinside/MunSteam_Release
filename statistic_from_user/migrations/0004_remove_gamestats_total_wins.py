# Generated by Django 4.2.14 on 2024-08-26 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistic_from_user', '0003_remove_gamestats_user_gamestats_user_steam_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamestats',
            name='total_wins',
        ),
    ]
