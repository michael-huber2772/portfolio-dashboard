# Generated by Django 3.1.2 on 2020-10-27 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201027_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productprice',
            name='current_flag',
            field=models.CharField(choices=[('Y', 'Y'), ('N', 'N')], max_length=1),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 27, 5, 45, 32, 249116), null=True),
        ),
    ]