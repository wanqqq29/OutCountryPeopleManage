# Generated by Django 3.1.4 on 2021-05-17 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CheckIn', '0011_delete_teacherinformation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentinformation',
            options={'verbose_name': '出国信息管理', 'verbose_name_plural': '出国信息管理'},
        ),
        migrations.AlterField(
            model_name='studentinformation',
            name='S_IdWorkNum',
            field=models.CharField(max_length=20, verbose_name='学号/工号'),
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('I_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('I_name', models.CharField(max_length=10, verbose_name='姓名')),
                ('I_group', models.CharField(blank=True, choices=[('T', '教师'), ('S', '学生')], max_length=135, verbose_name='身份')),
                ('I_School', models.CharField(max_length=20, verbose_name='学院')),
                ('I_IdCardNum', models.CharField(max_length=18, verbose_name='身份证号')),
                ('I_IdWorkNum', models.CharField(max_length=20, verbose_name='学号/工号')),
                ('I_major', models.CharField(max_length=30, verbose_name='专业')),
                ('user_id', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='申请人')),
            ],
            options={
                'verbose_name': '个人信息管理',
                'verbose_name_plural': '个人信息管理',
                'db_table': 'Informations',
            },
        ),
    ]
