# Generated by Django 3.1.2 on 2020-10-27 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201027_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productprice',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2999, 12, 31, 18, 0), null=True),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 27, 5, 18, 1, 697415), null=True),
        ),
    ]
