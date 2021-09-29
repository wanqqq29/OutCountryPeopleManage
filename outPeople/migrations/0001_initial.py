# Generated by Django 3.2.7 on 2021-09-25 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInformation',
            fields=[
                ('S_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('S_name', models.CharField(max_length=10, verbose_name='姓名')),
                ('S_group', models.CharField(blank=True, max_length=135, verbose_name='身份')),
                ('S_School', models.CharField(max_length=20, verbose_name='学院')),
                ('S_IdCardNum', models.CharField(max_length=18, verbose_name='身份证号')),
                ('S_Sex', models.CharField(max_length=100, verbose_name='性别')),
                ('S_IdWorkNum', models.CharField(max_length=20, verbose_name='学号')),
                ('S_major', models.CharField(max_length=30, verbose_name='专业')),
                ('S_ToCountry', models.CharField(max_length=250, verbose_name='去往外方学校')),
                ('S_ToTime', models.DateTimeField(verbose_name='出国机票时间')),
                ('S_ArrTime', models.DateTimeField(blank=True, null=True, verbose_name='回国抵达海关时间')),
                ('S_ToMajor', models.CharField(max_length=30, verbose_name='国外学习专业')),
                ('S_InLiveAddress', models.TextField(max_length=1024, verbose_name='国内家庭住址')),
                ('S_JoinProject', models.CharField(max_length=1024, verbose_name='参加项目')),
                ('S_InPhone', models.CharField(max_length=11, verbose_name='国内手机')),
                ('S_OutPhone', models.CharField(max_length=15, verbose_name='国外手机')),
                ('S_QQ', models.CharField(max_length=10, verbose_name='QQ号')),
                ('S_WX', models.CharField(max_length=10, verbose_name='微信号')),
                ('S_EName', models.CharField(max_length=15, verbose_name='紧急联系人姓名')),
                ('S_EPhone', models.CharField(max_length=15, verbose_name='紧急联系人手机号')),
                ('S_Face', models.CharField(max_length=15, verbose_name='政治面貌')),
                ('S_Other', models.CharField(max_length=1024, verbose_name='其他（是否在国内读网课）')),
                ('user_id', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='申请人')),
            ],
            options={
                'verbose_name': '出国信息管理',
                'verbose_name_plural': '出国信息管理',
                'db_table': 'S_Things',
            },
        ),
    ]