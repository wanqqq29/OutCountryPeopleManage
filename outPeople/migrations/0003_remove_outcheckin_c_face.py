# Generated by Django 3.2.7 on 2021-10-10 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outPeople', '0002_auto_20211010_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outcheckin',
            name='C_Face',
        ),
    ]