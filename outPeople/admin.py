from django.contrib import admin
from .models import StudentInformation

# Register your models here.

admin.site.site_title = '出国人员登记系统'
admin.site.site_header = '出国人员登记系统'



class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "S_name", "S_group","S_School", "S_IdCardNum", "S_Sex", "S_IdWorkNum", "S_major", "S_ToCountry", "S_ToTime", "S_ArrTime",
        "S_ToMajor", "S_InLiveAddress", "S_JoinProject", "S_InPhone", "S_OutPhone", "S_QQ", "S_WX", "S_EName",
        "S_EPhone", "S_Face", "S_Other",)
    list_editable = ()
    readonly_fields = ('S_id','user_id')
    search_fields = ('S_name',)
    empty_value_display = 'Null'
    list_filter = ('S_School','S_group')
    fieldsets = (
        ('出国信息', {'fields': (
            ("S_name", "S_group", "S_School", "S_IdCardNum"), ("S_Sex", "S_IdWorkNum", "S_major"),
            ("S_ToCountry", "S_ToTime", "S_ArrTime"), ("S_ToMajor", "S_InLiveAddress", "S_JoinProject"),
            ("S_InPhone", "S_OutPhone", "S_QQ", "S_WX"), ("S_EName", "S_EPhone", "S_Face", "S_Other"),)}),
    )
    def get_queryset(self, request):
        qs = super(StudentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_id=request.user)
    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request,obj,form,change)

admin.site.register(StudentInformation, StudentAdmin)


