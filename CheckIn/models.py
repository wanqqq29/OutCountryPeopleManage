from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
# Create your models here.


group = [
    ("T", "教师"),
    ("S", "学生"),
]

# 表结构
class StudentInformation(models.Model):
    S_id = models.AutoField(primary_key=True, verbose_name=("序号"))
    #user_id = models.ForeignKey(User,verbose_name=("用户id"),blank=True,on_delete=models.SET_NULL)
    user_id = models.ForeignKey(User, verbose_name=_("申请人"), null=True, on_delete=models.SET_NULL, db_constraint=False)
    S_name = models.CharField(max_length=10, blank=False, verbose_name=("姓名"))
    S_group = models.CharField(max_length=135,choices=group,blank=True,verbose_name=("身份"))
    S_School = models.CharField(max_length=20, blank=False, verbose_name=("学院"))
    S_IdCardNum = models.CharField(max_length=18, blank=False, verbose_name=("身份证号"))
    S_Sex = models.CharField(max_length=100, blank=False, verbose_name=("性别"))
    S_IdWorkNum = models.CharField(max_length=20, blank=False, verbose_name=("学号"))
    S_major = models.CharField(max_length=30, blank=False, verbose_name=("专业"))
    S_ToCountry = models.CharField(max_length=250, blank=False, verbose_name=("去往外方学校"))
    S_ToTime = models.DateTimeField(verbose_name=("出国机票时间"), blank=False)
    S_ArrTime = models.DateTimeField(verbose_name=("回国抵达海关时间"), null=True,blank=True)
    S_ToMajor = models.CharField(max_length=30, blank=False, verbose_name=("国外学习专业"))
    S_InLiveAddress = models.TextField(max_length=1024, blank=False, verbose_name=("国内家庭住址"))
    S_JoinProject = models.CharField(max_length=1024, blank=False, verbose_name=("参加项目"))
    S_InPhone = models.CharField(max_length=11, blank=False, verbose_name=("国内手机"))
    S_OutPhone = models.CharField(max_length=15, blank=False, verbose_name=("国外手机"))
    S_QQ = models.CharField(max_length=10, blank=False, verbose_name=("QQ号"))
    S_WX = models.CharField(max_length=10, blank=False, verbose_name=("微信号"))
    S_EName = models.CharField(max_length=15, blank=False, verbose_name=("紧急联系人姓名"))
    S_EPhone = models.CharField(max_length=15, blank=False, verbose_name=("紧急联系人手机号"))
    S_Face = models.CharField(max_length=15, blank=False, verbose_name=("政治面貌"))
    S_Other = models.CharField(max_length=1024, blank=False, verbose_name=("其他（是否在国内读网课）"))
    class Meta:
        db_table = 'S_Things'
        verbose_name = '出国信息管理'
        verbose_name_plural = '出国信息管理'
