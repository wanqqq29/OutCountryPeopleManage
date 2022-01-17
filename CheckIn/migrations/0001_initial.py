# Generated by Django 3.1.7 on 2021-04-25 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInformation',
            fields=[
                ('S_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('S_name', models.CharField(max_length=10, verbose_name='姓名')),
                ('S_School', models.CharField(max_length=20, verbose_name='学院')),
                ('S_IdCardNum', models.TextField(max_length=18, verbose_name='身份证号')),
                ('S_Sex', models.CharField(max_length=100, verbose_name='性别')),
                ('S_IdWorkNum', models.TextField(max_length=20, verbose_name='学号')),
                ('S_major', models.TextField(max_length=30, verbose_name='专业')),
                ('S_ToCountry', models.TextField(max_length=250, verbose_name='去往外方学校')),
                ('S_ToTime', models.DateTimeField(verbose_name='出国机票时间')),
                ('S_ArrTime', models.DateTimeField(verbose_name='回国抵达海关时间')),
                ('S_ToMajor', models.TextField(max_length=30, verbose_name='国外学习专业')),
                ('S_InLiveAddress', models.TextField(max_length=1024, verbose_name='国内家庭住址')),
                ('S_JoinProject', models.TextField(max_length=1024, verbose_name='参加项目')),
                ('S_InPhone', models.TextField(max_length=11, verbose_name='国内手机')),
                ('S_OutPhone', models.TextField(max_length=15, verbose_name='国外手机')),
                ('S_QQ', models.TextField(max_length=10, verbose_name='QQ号')),
                ('S_WX', models.TextField(max_length=10, verbose_name='微信号')),
                ('S_EName', models.TextField(max_length=15, verbose_name='紧急联系人姓名')),
                ('S_EPhone', models.TextField(max_length=15, verbose_name='紧急联系人手机号')),
                ('S_Face', models.TextField(max_length=15, verbose_name='政治面貌')),
                ('S_Other', models.TextField(max_length=1024, verbose_name='其他（是否在国内读网课）')),
            ],
            options={
                'db_table': 'S_Things',
            },
        ),
        migrations.CreateModel(
            name='TeacherInformation',
            fields=[
                ('T_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('T_name', models.CharField(max_length=10, verbose_name='姓名')),
                ('T_School', models.CharField(max_length=20, verbose_name='学院')),
                ('T_IdCardNum', models.TextField(max_length=18, verbose_name='身份证号')),
                ('T_Sex', models.CharField(max_length=100, verbose_name='性别')),
                ('T_IdWorkNum', models.TextField(max_length=20, verbose_name='职工号')),
                ('T_major', models.TextField(max_length=30, verbose_name='专业')),
                ('T_ToCountry', models.TextField(max_length=250, verbose_name='去往外方学校')),
                ('T_ToTime', models.DateTimeField(verbose_name='出国机票时间')),
                ('T_ArrTime', models.DateTimeField(verbose_name='回国抵达海关时间')),
                ('T_ToMajor', models.TextField(max_length=30, verbose_name='国外学习专业')),
                ('T_InLiveAddress', models.TextField(max_length=1024, verbose_name='国内家庭住址')),
                ('T_JoinProject', models.TextField(max_length=1024, verbose_name='参加项目')),
                ('T_InPhone', models.TextField(max_length=11, verbose_name='国内手机')),
                ('T_OutPhone', models.TextField(max_length=15, verbose_name='国外手机')),
                ('T_QQ', models.TextField(max_length=10, verbose_name='QQ号')),
                ('T_WX', models.TextField(max_length=10, verbose_name='微信号')),
                ('T_EName', models.TextField(max_length=15, verbose_name='紧急联系人姓名')),
                ('T_EPhone', models.TextField(max_length=15, verbose_name='紧急联系人手机号')),
                ('T_Face', models.TextField(max_length=15, verbose_name='政治面貌')),
                ('T_Other', models.TextField(max_length=1024, verbose_name='其他（是否在国内读网课）')),
            ],
            options={
                'db_table': 'T_Things',
            },
        ),
    ]