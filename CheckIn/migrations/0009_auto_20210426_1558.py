# Generated by Django 3.1.3 on 2021-04-26 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CheckIn', '0008_auto_20210426_1557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentinformation',
            options={'verbose_name': '个人信息', 'verbose_name_plural': '个人信息'},
        ),
        migrations.AddField(
            model_name='studentinformation',
            name='S_group',
            field=models.CharField(blank=True, choices=[(0, '教师'), (1, '学生')], max_length=135, verbose_name='身份'),
        ),
    ]
