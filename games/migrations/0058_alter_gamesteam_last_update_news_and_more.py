# Generated by Django 4.2.14 on 2024-09-03 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0057_alter_gamesteam_last_update_news_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesteam',
            name='last_update_news',
            field=models.DateField(default=datetime.datetime(2024, 9, 3, 16, 23, 21, 451660)),
        ),
        migrations.AlterField(
            model_name='gamesteam',
            name='last_update_players',
            field=models.CharField(default=datetime.datetime(2024, 9, 3, 13, 23, 21, 451556, tzinfo=datetime.timezone.utc)),
        ),
    ]
