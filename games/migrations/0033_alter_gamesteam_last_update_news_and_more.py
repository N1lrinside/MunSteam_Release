# Generated by Django 4.2.14 on 2024-08-30 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0032_alter_gamesteam_last_update_news_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesteam',
            name='last_update_news',
            field=models.DateField(default=datetime.datetime(2024, 8, 30, 15, 25, 20, 217970)),
        ),
        migrations.AlterField(
            model_name='gamesteam',
            name='last_update_players',
            field=models.CharField(default=datetime.datetime(2024, 8, 30, 12, 25, 20, 217970, tzinfo=datetime.timezone.utc)),
        ),
    ]
