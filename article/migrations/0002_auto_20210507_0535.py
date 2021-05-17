# Generated by Django 3.2.1 on 2021-05-07 03:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='disp_date_limit',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='article',
            name='viewable_admin',
            field=models.BooleanField(default=True),
        ),
    ]
