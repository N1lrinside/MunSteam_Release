# Generated by Django 4.2.14 on 2024-08-22 23:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0016_remove_gamesteam_last_update_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesteam',
            name='last_update_news',
            field=models.DateField(default=datetime.datetime(2024, 8, 23, 2, 0, 47, 973122)),
        ),
        migrations.AlterField(
            model_name='gamesteam',
            name='last_update_players',
            field=models.CharField(default=datetime.datetime(2024, 8, 22, 23, 0, 47, 973075, tzinfo=datetime.timezone.utc)),
        ),
    ]