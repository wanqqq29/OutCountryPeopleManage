from .models import outCheckin, T_info, S_info
from django.contrib import admin
from import_export.admin import ExportMixin

# Register your models here.
from .resource import infoResources, TResources, SResources

admin.site.site_title = '出国人员登记系统'
admin.site.site_header = '出国人员登记系统'


# class outCheckinAdmin(admin.ModelAdmin):
# class Tinfo:
#     def Tinfo(self, obj):
#         return [Tinfo for Tinfo in obj.T_Model.all()]


class outCheckinAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = infoResources
    list_display = (
        'C_id', 'user_id', "C_group", "C_ToCountry", "C_ToTime", "C_ArrTime", "C_ToMajor", "C_JoinProject",
        "C_OutPhone", "C_EName", "C_EPhone", "C_Other")

    list_editable = ()
    readonly_fields = ('C_id', 'user_id')
    search_fields = ()
    empty_value_display = 'Null'
    list_filter = ()
    fieldsets = (
        ('出国信息登记', {'fields': ("C_group",
                               ("C_ToCountry", "C_ToTime", "C_ArrTime", "C_ToMajor", "C_JoinProject"),
                               ("C_OutPhone", "C_EName", "C_EPhone", "C_Other"),)}),
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
        "T_jobid", "T_name", "T_namePy", "T_Sex", "T_oldname", "T_old", "T_Country", "T_idnum", "T_idtype",
        "T_InLiveAddress", "T_QQ", "T_WX", "T_InPhone",
        "T_greenCard", "T_idlocal", "T_idfrom", "T_idgroup", "T_GAT", "T_Wedding", "T_zfgroup", "T_birthday_confirm",
        "T_birthday", "T_workdate", "T_zfjoindate", "T_teacherType", "T_currentType", "T_fromSchool", "T_fromClass",
        "T_ttype", "T_tfrom", "Test")
    list_editable = ()
    search_fields = ('T_name',)
    empty_value_display = 'Null'
    list_filter = ('T_fromSchool', 'T_ttype')
    fieldsets = (
        ('教师信息登记', {'fields': (
            "user_id", "T_jobid", "T_name", "T_namePy", "T_Sex", "T_oldname", "T_old", "T_Country", "T_idnum",
            "T_InLiveAddress", "T_QQ", "T_WX", "T_InPhone",
            "T_idtype", "T_greenCard", "T_idlocal", "T_idfrom", "T_idgroup", "T_GAT", "T_Wedding", "T_zfgroup",
            "T_birthday_confirm", "T_birthday", "T_workdate", "T_zfjoindate", "T_teacherType", "T_currentType",
            "T_fromSchool", "T_fromClass", "T_ttype", "T_tfrom", "Test")
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
        "user_id", "S_jobid", "S_name", "S_namePy", "S_Sex", "S_oldname", "S_old", "S_Country", "S_InLiveAddress",
        "S_idnum", "S_QQ", "S_WX", "S_InPhone",
        "S_idtype", "S_greenCard", "S_idlocal", "S_idfrom", "S_idgroup", "S_GAT", "S_Wedding", "S_zfgroup",
        "S_birthday_confirm", "S_birthday", "S_workdate", "S_fromSchool", "S_fromClass", "Test")
    list_editable = ()
    search_fields = ('S_name',)
    empty_value_display = 'Null'
    list_filter = ('S_fromSchool', 'S_fromClass')
    fieldsets = (
        ('教师信息登记', {'fields': (
            "user_id", "S_jobid", "S_name", "S_namePy", "S_Sex", "S_oldname", "S_old", "S_Country", "S_InLiveAddress",
            "S_idnum", "S_QQ", "S_WX", "S_InPhone",
            "S_idtype", "S_greenCard", "S_idlocal", "S_idfrom", "S_idgroup", "S_GAT", "S_Wedding", "S_zfgroup",
            "S_birthday_confirm", "S_birthday", "S_workdate", "S_fromSchool", "S_fromClass", "Test")
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
