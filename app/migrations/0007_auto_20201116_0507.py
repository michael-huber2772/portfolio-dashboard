# Generated by Django 3.1.3 on 2020-11-16 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201031_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='productprice',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 16, 5, 7, 53, 23971), null=True),
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('tag', models.ManyToManyField(to='app.MTag')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='raw_material',
            field=models.ManyToManyField(to='app.RawMaterial'),
        ),
    ]
