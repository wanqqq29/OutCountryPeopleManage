from django.contrib import admin
from outpeopleCheckin.models import Tinfo, Cinfo, SCinfo, Sinfo
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

# Register your models here.
from outpeopleCheckin.resource import SabroadResource, abroadResource, TinfoR, SinfoR

admin.site.site_title = '出国人员登记系统'
admin.site.site_header = '出国人员登记系统'


class Tinfo_form(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = (
        'username', 'applicant', 'T_jobid', 'T_namePy', 'T_Sex', 'T_oldname', 'T_old', 'T_Country', 'T_idnum',
        'T_idtype',
        'T_greenCard', 'T_idlocal', 'T_idfrom', 'T_idgroup', 'T_GAT', 'T_Wedding', 'T_zfgroup', 'T_birthday_confirm',
        'T_birthday', 'T_workdate', 'T_zfjoindate', 'T_teacherType', 'T_currentType', 'T_fromSchool', 'T_fromClass',
        'T_ttype', 'T_tfrom', 'T_InLiveAddress', 'T_QQ', 'T_WX', 'T_InPhone', 'Test', 'created_date', 'modified_date')
    readonly_fields = ('applicant', 'created_date', 'modified_date')
    resource_class = TinfoR

    fieldsets = (
        ('教师信息登记', {'fields': (
            'applicant', ('username', 'T_jobid', "T_namePy", "T_Sex", "T_oldname", "T_old", "T_Country", "T_idnum",
                          "T_InLiveAddress", "T_QQ", "T_WX", "T_InPhone",
                          "T_idtype", "T_greenCard", "T_idlocal", "T_idfrom", "T_idgroup", "T_GAT", "T_Wedding",
                          "T_zfgroup",
                          "T_birthday_confirm", "T_birthday", "T_workdate", "T_zfjoindate", "T_teacherType",
                          "T_currentType",
                          "T_fromSchool", "T_fromClass", "T_ttype", "T_tfrom", "Test"
                          ),)}),
    )

    def save_model(self, request, obj, form, change):
        obj.applicant = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Tinfo, Tinfo_form)


class Sinfo_form(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = (
        "S_name", 'applicant', "S_jobid", "S_namePy", "S_Sex", "S_oldname", "S_old", "S_Country",
        "S_idnum", "S_idtype", "S_greenCard", "S_idlocal", "S_idfrom", "S_idgroup", "S_GAT",
        "S_Wedding",
        "S_zfgroup", "S_birthday_confirm", "S_birthday", "S_workdate", "S_fromSchool", "S_fromClass",
        "S_InLiveAddress", "S_QQ", "S_WX", "S_InPhone", "Test", 'created_date', 'modified_date')
    readonly_fields = ('applicant', 'created_date', 'modified_date')
    resource_class = SinfoR

    fieldsets = (
        ('学生信息登记', {'fields': (
            'applicant', ("S_name", "S_jobid", "S_namePy", "S_Sex", "S_oldname", "S_old", "S_Country",
                          "S_idnum", "S_idtype", "S_greenCard", "S_idlocal", "S_idfrom", "S_idgroup", "S_GAT",
                          "S_Wedding",
                          "S_zfgroup", "S_birthday_confirm", "S_birthday", "S_workdate", "S_fromSchool", "S_fromClass",
                          "S_InLiveAddress", "S_QQ", "S_WX", "S_InPhone", "Test"
                          ),)}),
    )

    def save_model(self, request, obj, form, change):
        obj.applicant = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Sinfo, Sinfo_form)


# 教师出国信息
class Tabroad(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ("get_name", "C_ToCountry", "C_ToTime", "C_ArrTime", "C_ToMajor", "C_JoinProject",
                    "C_OutPhone", "C_EName", "C_EPhone", "C_Other")
    resource_class = abroadResource

    def get_name(self, obj):
        return obj.name.username

    get_name.short_description = '姓名'


admin.site.register(Cinfo, Tabroad)


# 学生出国信息
class Sabroad(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ("get_name", "C_ToCountry", "C_ToTime", "C_ArrTime", "C_ToMajor", "C_JoinProject",
                    "C_OutPhone", "C_EName", "C_EPhone", "C_Other")
    resource_class = SabroadResource

    def get_name(self, obj):
        return obj.name.S_name

    get_name.short_description = '姓名'


admin.site.register(SCinfo, Sabroad)
