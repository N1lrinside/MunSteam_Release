# Generated by Django 4.2.14 on 2024-08-21 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0011_alter_gamesteam_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesteam',
            name='last_update',
            field=models.CharField(default=datetime.datetime(2024, 8, 21, 17, 58, 31, 432037, tzinfo=datetime.timezone.utc)),
        ),
    ]
