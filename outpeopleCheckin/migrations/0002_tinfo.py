# Generated by Django 3.1.14 on 2021-12-12 05:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('outpeopleCheckin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=135, verbose_name='姓名')),
                ('T_jobid', models.CharField(max_length=20, verbose_name='职工号')),
                ('T_namePy', models.CharField(max_length=10, verbose_name='姓名拼音')),
                ('T_Sex', models.CharField(choices=[('男', '男'), ('女', '女')], max_length=100, verbose_name='性别')),
                ('T_oldname', models.CharField(max_length=10, verbose_name='曾用名')),
                ('T_old', models.IntegerField(verbose_name='年龄')),
                ('T_Country', models.CharField(max_length=10, verbose_name='国家')),
                ('T_idnum', models.CharField(max_length=20, verbose_name='身份证号')),
                ('T_idtype', models.CharField(max_length=20, verbose_name='身份证件类型')),
                ('T_greenCard', models.CharField(choices=[('是', '是'), ('否', '否')], max_length=20, verbose_name='是否持有绿卡')),
                ('T_idlocal', models.CharField(max_length=30, verbose_name='户口所在地')),
                ('T_idfrom', models.CharField(max_length=30, verbose_name='籍贯')),
                ('T_idgroup', models.CharField(max_length=30, verbose_name='民族')),
                ('T_GAT', models.CharField(max_length=30, verbose_name='港澳台侨')),
                ('T_Wedding', models.CharField(choices=[('是', '是'), ('否', '否')], max_length=30, verbose_name='婚姻状态')),
                ('T_zfgroup', models.CharField(max_length=20, verbose_name='政治面貌')),
                ('T_birthday_confirm', models.DateTimeField(verbose_name='组织确认出生日期')),
                ('T_birthday', models.DateTimeField(verbose_name='出生日期')),
                ('T_workdate', models.DateTimeField(verbose_name='参加工作日期')),
                ('T_zfjoindate', models.DateTimeField(verbose_name='参加党派日期')),
                ('T_teacherType', models.CharField(max_length=20, verbose_name='教职工类别')),
                ('T_currentType', models.CharField(choices=[('是', '是'), ('否', '否')], max_length=20, verbose_name='当前状态（是否在职）')),
                ('T_fromSchool', models.CharField(max_length=20, verbose_name='所在学院')),
                ('T_fromClass', models.CharField(max_length=20, verbose_name='所在专业')),
                ('T_ttype', models.CharField(max_length=20, verbose_name='教师类型')),
                ('T_tfrom', models.CharField(max_length=20, verbose_name='教师来源')),
                ('T_InLiveAddress', models.TextField(max_length=1024, verbose_name='国内家庭住址')),
                ('T_QQ', models.CharField(max_length=10, verbose_name='QQ号')),
                ('T_WX', models.CharField(max_length=10, verbose_name='微信号')),
                ('T_InPhone', models.CharField(max_length=11, verbose_name='国内手机')),
                ('Test', models.CharField(max_length=255, verbose_name='测试')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建日期')),
                ('modified_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改日期')),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='申请人')),
            ],
            options={
                'verbose_name': '教师信息',
                'verbose_name_plural': '教师信息列表',
            },
        ),
    ]