# Generated by Django 4.2.14 on 2024-09-02 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0046_alter_gamesteam_last_update_news_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesteam',
            name='last_update_news',
            field=models.DateField(default=datetime.datetime(2024, 9, 2, 16, 46, 41, 589253)),
        ),
        migrations.AlterField(
            model_name='gamesteam',
            name='last_update_players',
            field=models.CharField(default=datetime.datetime(2024, 9, 2, 13, 46, 41, 589165, tzinfo=datetime.timezone.utc)),
        ),
    ]
