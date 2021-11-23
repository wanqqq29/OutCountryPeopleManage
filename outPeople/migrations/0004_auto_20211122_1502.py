# Generated by Django 3.2.7 on 2021-11-22 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outPeople', '0003_remove_outcheckin_c_face'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=135, verbose_name='用户名')),
                ('LoginKey', models.CharField(max_length=135, verbose_name='密码')),
            ],
            options={
                'db_table': 'login',
            },
        ),
        migrations.AlterField(
            model_name='outcheckin',
            name='C_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='出国申请序号'),
        ),
    ]