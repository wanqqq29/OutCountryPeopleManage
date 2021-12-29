from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, db_constraint=False)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


group = [
    ("教师", "教师"),
    ("学生", "学生"),
    ("汉办出国人员", "汉办出国人员"),
]
sex = [
    ("男", "男"),
    ("女", "女"),
]
Sbool = [
    ("是", "是"),
    ("否", "否"),
]


class Tinfo(models.Model):
    username = models.CharField(max_length=135, verbose_name=u'姓名')
    applicant = models.ForeignKey(User, verbose_name='用户名', null=True, on_delete=models.SET_NULL,unique=True)
    T_jobid = models.CharField(max_length=20, blank=False, verbose_name=("职工号"))
    T_namePy = models.CharField(max_length=10, blank=False, verbose_name=("姓名拼音"))
    T_Sex = models.CharField(max_length=100, choices=sex, blank=False, verbose_name=("性别"))
    T_oldname = models.CharField(max_length=10, blank=False, verbose_name=("曾用名"))
    T_old = models.IntegerField(blank=False, verbose_name=("年龄"))
    T_Country = models.CharField(max_length=10, blank=False, verbose_name=("国家"))
    T_idnum = models.CharField(max_length=20, blank=False, verbose_name=("身份证号"))
    T_idtype = models.CharField(max_length=20, blank=False, verbose_name=("身份证件类型"))
    T_greenCard = models.CharField(max_length=20, choices=Sbool, blank=False, verbose_name=("是否持有绿卡"))
    T_idlocal = models.CharField(max_length=30, blank=False, verbose_name=("户口所在地"))
    T_idfrom = models.CharField(max_length=30, blank=False, verbose_name=("籍贯"))
    T_idgroup = models.CharField(max_length=30, blank=False, verbose_name=("民族"))
    T_GAT = models.CharField(max_length=30, blank=False, verbose_name=("港澳台侨"))
    T_Wedding = models.CharField(max_length=30, choices=Sbool, blank=False, verbose_name=("婚姻状态"))
    T_zfgroup = models.CharField(max_length=20, blank=False, verbose_name=("政治面貌"))
    T_birthday_confirm = models.DateTimeField(blank=False, verbose_name=("组织确认出生日期"))
    T_birthday = models.DateTimeField(blank=False, verbose_name=("出生日期"))
    T_workdate = models.DateTimeField(blank=False, verbose_name=("参加工作日期"))
    T_zfjoindate = models.DateTimeField(blank=False, verbose_name=("参加党派日期"))
    T_teacherType = models.CharField(max_length=20, blank=False, verbose_name=("教职工类别"))
    T_currentType = models.CharField(max_length=20, choices=Sbool, blank=False, verbose_name=("当前状态（是否在职）"))
    T_fromSchool = models.CharField(max_length=20, blank=False, verbose_name=("所在学院"))
    T_fromClass = models.CharField(max_length=20, blank=False, verbose_name=("所在专业"))
    T_ttype = models.CharField(max_length=20, blank=False, verbose_name=("教师类型"))
    T_tfrom = models.CharField(max_length=20, blank=False, verbose_name=("教师来源"))
    T_InLiveAddress = models.TextField(max_length=1024, blank=False, verbose_name=("国内家庭住址"))
    T_QQ = models.CharField(max_length=10, blank=False, verbose_name=("QQ号"))
    T_WX = models.CharField(max_length=10, blank=False, verbose_name=("微信号"))
    T_InPhone = models.CharField(max_length=11, blank=False, verbose_name=("国内手机"))
    Test = models.CharField(max_length=255, blank=False, verbose_name=("备注"))
    created_date = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改日期", default=datetime.now)

    class Meta:
        verbose_name = u'教师信息'
        verbose_name_plural = u'教师信息列表'

    def __unicode__(self):
        return self.name, self.T_jobid

    def __str__(self):
        return "%s"%(self.username)

class Sinfo(models.Model):
    applicant = models.ForeignKey(User, verbose_name='用户名', null=True, on_delete=models.SET_NULL,unique=True)
    S_jobid = models.CharField(max_length=20, blank=False, verbose_name=("学号"))
    S_name = models.CharField(max_length=10, blank=False, verbose_name="姓名")
    S_namePy = models.CharField(max_length=10, blank=False, verbose_name="姓名拼音")
    S_Sex = models.CharField(max_length=100, choices=sex, blank=False, verbose_name=("性别"))
    S_oldname = models.CharField(max_length=10, blank=False, verbose_name=("曾用名"))
    S_old = models.IntegerField(blank=False, verbose_name=("年龄"))
    S_Country = models.CharField(max_length=10, blank=False, verbose_name=("国家"))
    S_idnum = models.CharField(max_length=20, blank=False, verbose_name=("身份证号"))
    S_idtype = models.CharField(max_length=20, blank=False, verbose_name=("身份证件类型"))
    S_greenCard = models.CharField(max_length=20, choices=Sbool, blank=False, verbose_name=("是否持有绿卡"))
    S_idlocal = models.CharField(max_length=30, blank=False, verbose_name=("户口所在地"))
    S_idfrom = models.CharField(max_length=30, blank=False, verbose_name=("籍贯"))
    S_idgroup = models.CharField(max_length=30, blank=False, verbose_name=("民族"))
    S_GAT = models.CharField(max_length=30, blank=False, verbose_name=("港澳台侨"))
    S_Wedding = models.CharField(max_length=30, choices=Sbool, blank=False, verbose_name=("婚姻状态"))
    S_zfgroup = models.CharField(max_length=20, blank=False, verbose_name=("政治面貌"))
    S_birthday_confirm = models.DateTimeField(blank=False, verbose_name=("组织确认出生日期"))
    S_birthday = models.DateTimeField(blank=False, verbose_name=("出生日期"))
    S_workdate = models.DateTimeField(blank=False, verbose_name=("入学日期"))
    S_fromSchool = models.CharField(max_length=20, blank=False, verbose_name=("所在学院"))
    S_fromClass = models.CharField(max_length=20, blank=False, verbose_name=("专业"))
    S_InLiveAddress = models.TextField(max_length=1024, blank=False, verbose_name=("国内家庭住址"))
    S_QQ = models.CharField(max_length=10, blank=False, verbose_name=("QQ号"))
    S_WX = models.CharField(max_length=10, blank=False, verbose_name=("微信号"))
    S_InPhone = models.CharField(max_length=11, blank=False, verbose_name=("国内手机"))
    Test = models.CharField(max_length=11, blank=False, verbose_name=("备注"))
    created_date = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改日期", default=datetime.now)
    class Meta:
        verbose_name = u'学生信息'
        verbose_name_plural = u'学生信息列表'

    def __unicode__(self):
        return self.name, self.S_jobid
    def __str__(self):
        return "%s"%(self.S_name)

class Cinfo(models.Model):
    applicant = models.ForeignKey(User, verbose_name='用户名', null=True, on_delete=models.SET_NULL)
    name = models.ForeignKey('Tinfo',verbose_name='教师姓名',blank=True,on_delete=models.CASCADE)
    C_group = models.CharField(max_length=135, choices=group, blank=True, verbose_name=("身份"))
    C_ToCountry = models.CharField(max_length=250, blank=False, verbose_name=("去往外方学校"))
    C_ToTime = models.DateTimeField(verbose_name=("出国机票时间"), blank=False)
    C_ArrTime = models.DateTimeField(verbose_name=("回国抵达海关时间"), null=True, blank=True)
    C_ToMajor = models.CharField(max_length=30, blank=False, verbose_name=("国外学习专业"))
    C_JoinProject = models.CharField(max_length=1024, blank=False, verbose_name=("参加项目"))
    C_OutPhone = models.CharField(max_length=15, blank=False, verbose_name=("国外手机"))
    C_EName = models.CharField(max_length=15, blank=False, verbose_name=("紧急联系人姓名"))
    C_EPhone = models.CharField(max_length=15, blank=False, verbose_name=("紧急联系人手机号"))
    C_Other = models.CharField(max_length=1024, blank=False, verbose_name=("其他（是否在国内读网课）"))

    class Meta:
        verbose_name = u'教师出国信息'
        verbose_name_plural = u'教师出国信息列表'

    def __unicode__(self):
        return self.name, self.C_idWorkNum, self.C_idStudyNum

class SCinfo(models.Model):
    applicant = models.ForeignKey(User, verbose_name='用户名', null=True, on_delete=models.SET_NULL)
    name = models.ForeignKey('Sinfo', verbose_name='学生姓名', blank=True, on_delete=models.CASCADE)
    C_group = models.CharField(max_length=135, choices=group, blank=True, verbose_name=("身份"))
    C_ToCountry = models.CharField(max_length=250, blank=False, verbose_name=("去往外方学校"))
    C_ToTime = models.DateTimeField(verbose_name=("出国机票时间"), blank=False)
    C_ArrTime = models.DateTimeField(verbose_name=("回国抵达海关时间"), null=True, blank=True)
    C_ToMajor = models.CharField(max_length=30, blank=False, verbose_name=("国外学习专业"))
    C_JoinProject = models.CharField(max_length=1024, blank=False, verbose_name=("参加项目"))
    C_OutPhone = models.CharField(max_length=15, blank=False, verbose_name=("国外手机"))
    C_EName = models.CharField(max_length=15, blank=False, verbose_name=("紧急联系人姓名"))
    C_EPhone = models.CharField(max_length=15, blank=False, verbose_name=("紧急联系人手机号"))
    C_Other = models.CharField(max_length=1024, blank=False, verbose_name=("其他（是否在国内读网课）"))

    class Meta:
        verbose_name = u'学生出国信息'
        verbose_name_plural = u'学生出国信息列表'

    def __unicode__(self):
        return self.name, self.C_idWorkNum, self.C_idStudyNum

