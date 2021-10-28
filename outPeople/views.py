import json
import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import outCheckin, T_info, S_info


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


## CSRTOKEN
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt


@ensure_csrf_cookie
def get_csrf_token(request):
    global csrtoken, csrtokent
    csrtoken = get_token(request)
    csrtokent = random.random()
    return JsonResponse({'csrf_token': csrtoken, "jsdlak": str(csrtokent)})


# Create your views here.
# 教师信息
@csrf_exempt
def Tinfo(request):
    # if request.method == 'GET':
    #     csrtoken = get_token(request)
    #     csrtokent = random.random()
    #     return JsonResponse({'csrf_token': csrtoken, "jsdlak": str(csrtokent)})
    if request.method == 'POST':
        if json.loads(request.body).get('tk') == str(csrtokent):
            jsondata = {'fields': {'checkfields': [], 'Tfields': [], 'visibleColumns': [], 'Columns': []}, 'data': []}
            TCheckinItems = outCheckin.objects.values().all()
            dict0 = {}
            dict1 = {}
            allinfo = {}  # 0老师信息 1出国签到信息，
            for i in TCheckinItems:
                id = i['user_id_id']
                idgroup = i['C_group']
                dict1 = i
                if idgroup == "教师":
                    info = T_info.objects.filter(user_id=id).values()
                    dict0 = info[0]
                    allinfo = Merge(dict0, dict1)
                    jsondata['data'].append(allinfo)  # 内容填充
            # 字段
            Tfields = T_info._meta.fields
            Checkfields = outCheckin._meta.fields
            for i in Checkfields:
                jsondata['fields']['checkfields'].append({'name': i.name, 'label': i.verbose_name, 'field': i.name})
                jsondata['fields']['visibleColumns'].append(i.name)
                jsondata['fields']['Columns'].append({'name': i.name, 'label': i.verbose_name, 'field': i.name})
            for i in Tfields:
                jsondata['fields']['Tfields'].append({'name': i.name, 'label': i.verbose_name, 'field': i.name})
                jsondata['fields']['visibleColumns'].append(i.name)
                jsondata['fields']['Columns'].append({'name': i.name, 'label': i.verbose_name, 'field': i.name})
            return JsonResponse(jsondata)
        else:
            return HttpResponse("加载失败")


# Create your views here.
@csrf_exempt
def Sinfo(request):
    if request.method == 'POST':
        if json.loads(request.body).get('tk') == str(csrtokent):
            jsondata = {'fields': {'checkfields': [], 'Sfields': [], 'visibleColumns': [], 'Columns': []}, 'data': []}
            SCheckinItems = outCheckin.objects.values().all()
            dict0 = {}
            dict1 = {}
            allinfo = {}  # 0学生信息 1出国签到信息，
            for i in SCheckinItems:
                id = i['user_id_id']
                idgroup = i['C_group']
                if idgroup == "学生":
                    dict1 = i
                    info = S_info.objects.filter(user_id=id).values()
                    dict0 = info[0]
                    allinfo = Merge(dict0, dict1)
                    jsondata['data'].append(allinfo)  # 内容填充
            # 字段
            Sfields = S_info._meta.fields
            Checkfields = outCheckin._meta.fields
            for i in Checkfields:
                jsondata['fields']['checkfields'].append({'name': i.name, 'label': i.verbose_name, 'field': i.name})
                jsondata['fields']['visibleColumns'].append(i.name)
                jsondata['fields']['Columns'].append({'name': i.name, 'label': i.verbose_name, 'field': i.name})
            for i in Sfields:
                jsondata['fields']['Sfields'].append({'name': i.name, 'label': i.verbose_name, 'field': i.name})
                jsondata['fields']['visibleColumns'].append(i.name)
                jsondata['fields']['Columns'].append({'name': i.name, 'label': i.verbose_name, 'field': i.name})
            return JsonResponse(jsondata)
        else:
            return HttpResponse("加载失败")