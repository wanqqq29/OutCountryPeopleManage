# Generated by Django 3.1.14 on 2021-12-13 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outpeopleCheckin', '0003_sinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinfo',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='创建日期'),
        ),
        migrations.AddField(
            model_name='sinfo',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='修改日期'),
        ),
    ]
