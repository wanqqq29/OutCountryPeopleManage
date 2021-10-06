from .models import outCheckin, T_info, S_info
from django.contrib import admin
from import_export.admin import ExportMixin

# Register your models here.
from .resource import infoResources, TResources, SResources

admin.site.site_title = '出国人员登记系统'
admin.site.site_header = '出国人员登记系统'


# class outCheckinAdmin(admin.ModelAdmin):
class outCheckinAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = infoResources
    list_display = (
        "C_name", "C_group", "C_School", "C_idCardNum", "C_Sex", "C_idWorkNum", "C_major", "C_ToCountry",
        "C_ToTime", "C_ArrTime",
        "C_ToMajor", "C_InLiveAddress", "C_JoinProject", "C_InPhone", "C_OutPhone", "C_QQ", "C_WX", "C_EName",
        "C_EPhone", "C_Face", "C_Other",)
    list_editable = ()
    readonly_fields = ('C_id', 'user_id')
    search_fields = ('C_name',)
    empty_value_display = 'Null'
    list_filter = ('C_School', 'C_group')
    fieldsets = (
        ('出国信息登记', {'fields': (
            ("C_name", "C_group", "C_School", "C_idCardNum"), ("C_Sex", "C_idWorkNum", "C_major"),
            ("C_ToCountry", "C_ToTime", "C_ArrTime"), ("C_ToMajor", "C_InLiveAddress", "C_JoinProject"),
            ("C_InPhone", "C_OutPhone", "C_QQ", "C_WX"), ("C_EName", "C_EPhone", "C_Face", "C_Other"),)}),
    )

    def get_queryset(self, request):
        qs = super(outCheckinAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_id=request.user)

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


admin.site.register(outCheckin, outCheckinAdmin)


class T_infoAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = TResources
    list_display = (
        "user_id", "T_jobid", "T_name", "T_namePy", "T_Sex", "T_oldname", "T_old", "T_Country", "T_idnum", "T_idtype",
        "T_greenCard", "T_idlocal", "T_idfrom", "T_idgroup", "T_GAT", "T_Wedding", "T_zfgroup", "T_birthday_confirm",
        "T_birthday", "T_workdate", "T_zfjoindate", "T_teacherType", "T_currentType", "T_fromSchool", "T_fromClass",
        "T_ttype", "T_tfrom")
    list_editable = ()
    readonly_fields = ('T_id', 'user_id')
    search_fields = ('T_name',)
    empty_value_display = 'Null'
    list_filter = ('T_fromSchool', 'T_ttype')
    fieldsets = (
        ('教师信息登记', {'fields': (
            "user_id", "T_jobid", "T_name", "T_namePy", "T_Sex", "T_oldname", "T_old", "T_Country", "T_idnum",
            "T_idtype", "T_greenCard", "T_idlocal", "T_idfrom", "T_idgroup", "T_GAT", "T_Wedding", "T_zfgroup",
            "T_birthday_confirm", "T_birthday", "T_workdate", "T_zfjoindate", "T_teacherType", "T_currentType",
            "T_fromSchool", "T_fromClass", "T_ttype", "T_tfrom")
        }),
    )

    def get_queryset(self, request):
        qs = super(T_infoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_id=request.user)

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


admin.site.register(T_info, T_infoAdmin)


class S_infoAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = SResources
    list_display = (
        "user_id", "S_jobid", "S_name", "S_namePy", "S_Sex", "S_oldname", "S_old", "S_Country", "S_idnum",
        "S_idtype", "S_greenCard", "S_idlocal", "S_idfrom", "S_idgroup", "S_GAT", "S_Wedding", "S_zfgroup",
        "S_birthday_confirm", "S_birthday", "S_workdate", "S_fromSchool", "S_fromClass")
    list_editable = ()
    readonly_fields = ('S_id', 'user_id')
    search_fields = ('S_name',)
    empty_value_display = 'Null'
    list_filter = ('S_fromSchool', 'S_fromClass')
    fieldsets = (
        ('教师信息登记', {'fields': (
            "user_id", "S_jobid", "S_name", "S_namePy", "S_Sex", "S_oldname", "S_old", "S_Country", "S_idnum",
            "S_idtype", "S_greenCard", "S_idlocal", "S_idfrom", "S_idgroup", "S_GAT", "S_Wedding", "S_zfgroup",
            "S_birthday_confirm", "S_birthday", "S_workdate", "S_fromSchool", "S_fromClass")
        }),
    )

    def get_queryset(self, request):
        qs = super(S_infoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_id=request.user)

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


admin.site.register(S_info, S_infoAdmin)
