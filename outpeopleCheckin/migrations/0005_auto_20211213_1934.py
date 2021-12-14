# Generated by Django 3.1.14 on 2021-12-13 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('outpeopleCheckin', '0004_auto_20211213_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinfo',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='tinfo',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
        migrations.CreateModel(
            name='Cinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_group', models.CharField(blank=True, choices=[('教师', '教师'), ('学生', '学生')], max_length=135, verbose_name='身份')),
                ('C_ToCountry', models.CharField(max_length=250, verbose_name='去往外方学校')),
                ('C_ToTime', models.DateTimeField(verbose_name='出国机票时间')),
                ('C_ArrTime', models.DateTimeField(blank=True, null=True, verbose_name='回国抵达海关时间')),
                ('C_ToMajor', models.CharField(max_length=30, verbose_name='国外学习专业')),
                ('C_JoinProject', models.CharField(max_length=1024, verbose_name='参加项目')),
                ('C_OutPhone', models.CharField(max_length=15, verbose_name='国外手机')),
                ('C_EName', models.CharField(max_length=15, verbose_name='紧急联系人姓名')),
                ('C_EPhone', models.CharField(max_length=15, verbose_name='紧急联系人手机号')),
                ('C_Other', models.CharField(max_length=1024, verbose_name='其他（是否在国内读网课）')),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '出国信息',
                'verbose_name_plural': '出国信息列表',
                'db_table': 'Cinfo',
            },
        ),
    ]
