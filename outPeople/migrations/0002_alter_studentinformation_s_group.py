# Generated by Django 3.2.7 on 2021-09-25 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outPeople', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinformation',
            name='S_group',
            field=models.CharField(blank=True, choices=[('T', '教师'), ('S', '学生')], max_length=135, verbose_name='身份'),
        ),
    ]