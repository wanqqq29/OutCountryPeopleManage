import re
import time

from django.contrib.auth.decorators import permission_required, login_required
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
# Create your views here.
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from pkg_resources import require
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView

from outpeopleCheckin.content_processors import detailid
from outpeopleCheckin.models import Tinfo, Sinfo, Cinfo, SCinfo


def index(request):
    return render(request, 'index.html')


def success(request):
    return render(request, 'success.html')


def notfound(request):
    return render(request, 'notfound.html')


class Tinfo_Createview(LoginRequiredMixin, CreateView):
    # 教师信息填写页面
    template_name = 'Tinfo_form.html'

    success_url = '/success/'
    model = Tinfo

    fields = ["username", "T_jobid", "T_namePy", "T_Sex", "T_oldname", "T_old", "T_Country", "T_idnum", "T_idtype",
              "T_greenCard", "T_idlocal", "T_idfrom", "T_idgroup", "T_GAT", "T_Wedding", "T_zfgroup",
              "T_birthday_confirm", "T_birthday", "T_workdate", "T_zfjoindate", "T_teacherType", "T_currentType",
              "T_fromSchool", "T_fromClass", "T_ttype", "T_tfrom", "T_InLiveAddress", "T_QQ", "T_WX", "T_InPhone",
              "Test"]

    # 与当前登录用户关联
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class DeatilView(LoginRequiredMixin, DetailView):
    model = Tinfo
    template_name = 'Tdetail.html'


class Tinfo_editview(LoginRequiredMixin, UpdateView):
    # 教师信息编辑页面
    template_name = 'edit.html'
    success_url = '/success/'
    model = Tinfo
    fields = ["username", "T_jobid", "T_namePy", "T_Sex", "T_oldname", "T_old", "T_Country", "T_idnum", "T_idtype",
              "T_greenCard", "T_idlocal", "T_idfrom", "T_idgroup", "T_GAT", "T_Wedding", "T_zfgroup",
              "T_birthday_confirm", "T_birthday", "T_workdate", "T_zfjoindate", "T_teacherType", "T_currentType",
              "T_fromSchool", "T_fromClass", "T_ttype", "T_tfrom", "T_InLiveAddress", "T_QQ", "T_WX", "T_InPhone",
              "Test"]

    # 与当前登录用户关联
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class Sinfo_Createview(LoginRequiredMixin, CreateView):
    # 学生信息填写页面
    template_name = 'Sinfo_form.html'

    success_url = '/success/'
    model = Sinfo

    fields = ["S_jobid", "S_name", "S_namePy", "S_Sex", "S_oldname", "S_old", "S_Country",
              "S_idnum", "S_idtype", "S_greenCard", "S_idlocal", "S_idfrom", "S_idgroup", "S_GAT", "S_Wedding",
              "S_zfgroup", "S_birthday_confirm", "S_birthday", "S_workdate", "S_fromSchool", "S_fromClass",
              "S_InLiveAddress", "S_QQ", "S_WX", "S_InPhone", "Test"]

    # 与当前登录用户关联
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class SDeatilView(LoginRequiredMixin, DetailView):
    model = Sinfo
    template_name = 'Sdetail.html'


class Sinfo_editview(LoginRequiredMixin, UpdateView):
    # 学生信息编辑页面
    template_name = 'edit.html'
    success_url = '/success/'
    model = Sinfo
    fields = ["S_jobid", "S_name", "S_namePy", "S_Sex", "S_oldname", "S_old", "S_Country",
              "S_idnum", "S_idtype", "S_greenCard", "S_idlocal", "S_idfrom", "S_idgroup", "S_GAT", "S_Wedding",
              "S_zfgroup", "S_birthday_confirm", "S_birthday", "S_workdate", "S_fromSchool", "S_fromClass",
              "S_InLiveAddress", "S_QQ", "S_WX", "S_InPhone", "Test"]

    # 与当前登录用户关联
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class Cinfo_Createview(LoginRequiredMixin, CreateView):
    # 出国信息填写页面
    template_name = 'Cinfo_form.html'

    success_url = '/success/'
    model = Cinfo

    fields = ["C_ToCountry", "C_ToTime", "C_ArrTime", "C_ToMajor", "C_JoinProject",
              "C_OutPhone", "C_EName", "C_EPhone", "C_Other"]

    # 与当前登录用户关联
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        if Tinfo.objects.filter(applicant=self.request.user).exists():
            self.object.C_group = '教师'
            self.object.name = Tinfo.objects.filter(applicant=self.request.user).first().username
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render('success.html')




class SCinfo_Createview(LoginRequiredMixin, CreateView):
    # 学生出国信息填写页面
    template_name = 'Cinfo_form.html'

    success_url = '/success/'
    model = SCinfo

    fields = ["name","C_ToCountry", "C_ToTime", "C_ArrTime", "C_ToMajor", "C_JoinProject",
              "C_OutPhone", "C_EName", "C_EPhone", "C_Other"]

    # 与当前登录用户关联
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        if Sinfo.objects.filter(applicant=self.request.user).exists():
            self.object.C_group = '学生'
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render('success.html')


# 教师出国登记查询
@login_required
def Cinfo_query(request):
    if request.user == 'AnonymousUser':
        pass
    else:
        Sflag = Sinfo.objects.filter(applicant=request.user).exists()
        Tflag = Tinfo.objects.filter(applicant=request.user).exists()

        if Tflag:
            info_list = Cinfo.objects.all().filter(applicant=request.user).oredr_by('created_date')
            fields = Cinfo._meta.fields
            group = True
        elif Sflag:
            info_list = SCinfo.objects.all().filter(applicant=request.user)
            fields = SCinfo._meta.fields
            group = False
        else:
            info_list = ''
            fields = ''
        return render(request, 'query.html', {'group': group, 'data': info_list, 'fields': fields})


class Cinfo_editview(LoginRequiredMixin, UpdateView):
    # 出国信息编辑页面
    template_name = 'edit.html'
    success_url = '/success/'
    model = Cinfo
    fields = ["name","C_ToCountry", "C_ToTime", "C_ArrTime", "C_ToMajor", "C_JoinProject",
              "C_OutPhone", "C_EName", "C_EPhone", "C_Other"]

    # 与当前登录用户关联
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        if Tinfo.objects.filter(applicant=self.request.user).exists():
            self.object.C_group = '教师'
        elif Sinfo.objects.filter(applicant=self.request.user).exists():
            self.object.C_group = '学生'
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class SCinfo_editview(LoginRequiredMixin, UpdateView):
    # 出国信息编辑页面
    template_name = 'edit.html'
    success_url = '/success/'
    model = SCinfo
    fields = ["name","C_ToCountry", "C_ToTime", "C_ArrTime", "C_ToMajor", "C_JoinProject",
              "C_OutPhone", "C_EName", "C_EPhone", "C_Other"]

    # 与当前登录用户关联
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        if Tinfo.objects.filter(applicant=self.request.user).exists():
            self.object.C_group = '教师'
        elif Sinfo.objects.filter(applicant=self.request.user).exists():
            self.object.C_group = '学生'
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())